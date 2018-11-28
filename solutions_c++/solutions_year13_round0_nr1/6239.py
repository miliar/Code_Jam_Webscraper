/*
 * main.cpp
 *
 *  Created on: Apr 12, 2013
 *      Author: Matt
 */

#include <iostream>
#include <fstream>

using namespace std;

static const char* PLAYERX   = "X won";
static const char* PLAYERO   = "O won";
static const char* DRAW      = "Draw";
static const char* NCOMPLETE = "Game has not completed";

static const int SIZE = 4;

static char matrix[SIZE][SIZE];

void clear_matrix() {
	for(int row=0; row < SIZE; row++) {
		for(int col=0; col < SIZE; col++)
			matrix[row][col] = '.';
	}
}

bool verify_win(const char& token) {
	int row = 0;
	int col = 0;

	int count = 0;

	//Horizontal Wins
	for(row = 0; row < SIZE; row++) {
		for(col=0; col < SIZE; col++) {
			if((matrix[row][col] == token) || (matrix[row][col] == 'T')) {
				count++;
			}
			else
				break;
		}

		if(count == SIZE)
			return true;
		else
			count = 0;
	}

	//Vertical Wins
	for(col = 0; col < SIZE; col++) {
		for(row=0; row < SIZE; row++) {
			if((matrix[row][col] == token) || (matrix[row][col] == 'T')) {
				count++;
			}
			else
				break;
		}

		if(count == SIZE)
			return true;
		else
			count = 0;
	}

	//Left Diagonal Win
	row = 0;
	col = 0;

	while((row < SIZE) && (col < SIZE)) {
		if((matrix[row][col] == token) || (matrix[row][col] == 'T')) {
			count++;
		}
		else
			break;

		row++;
		col++;
	}

	if(count == SIZE)
		return true;
	else
		count = 0;

	//Right Diagonal Win
	row = 0;
	col = (SIZE - 1);

	while((row < SIZE) && (col >= 0)) {
		if((matrix[row][col] == token) || (matrix[row][col] == 'T')) {
			count++;
		}
		else
			break;

		row++;
		col--;
	}

	if(count == SIZE)
		return true;
	else
		return false;
}

int count_spaces() {
	int count = 0;

	for(int row=0; row < SIZE; row++) {
		for(int col=0; col < SIZE; col++)
			if(matrix[row][col] == '.')
				count++;
	}

	return count;
}

const char* determine_winner() {
	bool playerA = verify_win('X');
	bool playerB = verify_win('O');

	if(playerA)
		return PLAYERX;

	else if(playerB)
		return PLAYERO;

	else {
		if(count_spaces() == 0)
			return DRAW;
		else
			return NCOMPLETE;
	}
}

int main(int argc, char** argv) {

	ifstream ifile("large.in", ios::in);

	ofstream ofile("output.txt", ios::out);

	int numOfTests = 0;

	int row = 0;
	int col = 0;

	ifile >> numOfTests;

	for(int index=0; index < numOfTests; index++) {
		for(row=0; row < SIZE; row++)
			for(col=0; col < SIZE; col++)
				ifile >> matrix[row][col];

		cout << "Case #" << (index+1) << ": " << determine_winner() << endl;
		ofile << "Case #" << (index+1) << ": " << determine_winner() << endl;

		clear_matrix();
	}


	ofile.flush();
	ofile.close();

	ifile.close();

	return 0;
}


