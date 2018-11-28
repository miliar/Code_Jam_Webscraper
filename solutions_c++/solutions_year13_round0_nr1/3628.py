#include "board.hpp"

#include <cassert>
#include <stdexcept>
#include <iostream>


board::board(const string_list& lines){
	assert(lines.size() == board_size);
	for(int y=0; y < board_size; ++y){
		// std::cout << lines.at(y) << ": " << y << std::endl;
		for(int x=0; x < board_size; ++x){
			switch(lines.at(y).at(x)){
				case 'X':
					fields[y][x] = field_state::X;
					break;
				case 'O':
					fields[y][x] = field_state::O;
					break;
				case 'T':
					fields[y][x] = field_state::joker;
					break;
				case '.':
					fields[y][x] = field_state::empty;
					break;
				default:
					throw std::invalid_argument("invalid field");
			}
		}
	}
}


board::game_state board::get_state() const {
	player winner = check_rows();
	if(winner != player::none){
		return winner_to_state(winner);
	}
	winner = check_cols();
	if(winner != player::none){
		return winner_to_state(winner);
	}
	winner = check_diagonal();
	if(winner != player::none){
		return winner_to_state(winner);
	}
		
	for(const auto& row: fields){
		for(const auto& field: row){
			if(field == field_state::empty){
				return game_state::unfinished;
			}
		}
	}
	return game_state::tie;
}

//rows:
board::player board::check_rows() const {
	for(const auto& row: fields){
		auto tmp = winner(row[0], row[1], row[2], row[3]);
		if(tmp.first){
			return tmp.second;
		}
	}
	return player::none;
}

//cols:
board::player board::check_cols() const {
	for(int x = 0; x < board_size; ++x){
		auto tmp = winner(fields[0][x], fields[1][x], fields[2][x], fields[3][x]);
		if(tmp.first){
			return tmp.second;
		}
	}
	return player::none;
}

//diagonal:
board::player board::check_diagonal() const {
	auto tmp = winner(0,0,  1,1,  2,2,  3,3);
	if(tmp.first) return tmp.second;
	tmp = winner(0,3,  1,2,  2,1,  3,0);
	if(tmp.first) return tmp.second;
	
	else return player::none;
}

board::player board::from_field(field_state field) const{
	switch(field){
		case field_state::X:
			return player::X;
		case field_state::O:
			return player::O;
		default:
			return player::none;
	}
}

board::test_state board::winner(field_state f1, field_state f2, field_state f3, field_state f4) const{
	if(f1 == field_state::empty) return {false, player::none};
	field_state reference;
	if(f1 == field_state::joker){
		if(f2 == field_state::empty){
			return {false, player::none};
		}
		reference = f2;
	}
	else {
		reference = f1;
		if(f2 != reference && f2 != field_state::joker){
			return {false, player::none};
		}
	}
	
	if((f3 != reference && f3 != field_state::joker)
			||(f4 != reference && f4 != field_state::joker)){
		return {false, player::none};
	}
	
	return {true, from_field(reference)};
}

board::test_state board::winner(int y1, int x1, int y2, int x2, int y3, int x3, int y4, int x4) const {
	return winner(fields[y1][x1], fields[y2][x2], fields[y3][x3], fields[y4][x4]);
}


board::game_state board::winner_to_state(player winner) const {
	switch(winner){
		case player::X:
			return game_state::x_won;
		case player::O:
			return game_state::o_won;
		default:
			throw std::invalid_argument("winner must not be none");
	}
}
