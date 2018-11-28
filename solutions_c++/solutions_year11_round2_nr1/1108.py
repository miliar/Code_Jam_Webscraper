//
//  code_jam
//
//  Created by Paul O'Neil on 5/20/11.
//  Copyright 2011 Paul O'Neil. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

enum game_result {
  DIDNT_PLAY = 2,
  WON = 1,
  LOST = 0,
};

struct team_t {
  int win_count;
  int game_count;
  game_result * results; // 0 if not played, 1 if lost, 2 if won
  double opponent_win_percent;
  double oo_win_percent;
  
  team_t() : win_count(0), game_count(0), results(NULL),
    opponent_win_percent(0.0), oo_win_percent(0.0)
  { }
  
  ~team_t() {
    if( results ) {
      delete [] results;
    }
  }
  
  double win_percentage() const throw() {
    return ((double)win_count)/((double)game_count);
  }
  
  int wins_without_team( int team_idx ) {
    return win_count - results[team_idx];
  }
  
  double win_percent_without_team( int team_idx ) {
    return ((double)wins_without_team(team_idx))/((double)game_count - 1.0);	
  }
  
  double rpi() {
    return 0.25 * win_percentage() + 0.5 * opponent_win_percent + 0.25 * oo_win_percent;
  }
};

void find_opponent_win_percent(int team_idx, team_t * teams, int team_count) {
  team_t * cur_team = &teams[team_idx];
  cur_team->opponent_win_percent = 0.0;
  for( int other_idx = 0; other_idx < team_count; other_idx++ ) {
    if( other_idx == team_idx ) {
      continue;
    }
    if( cur_team->results[other_idx] == DIDNT_PLAY ) {
      continue;
    }
    cur_team->opponent_win_percent += teams[other_idx].win_percent_without_team(team_idx);
  }
  cur_team->opponent_win_percent /= (double)cur_team->game_count;
}

void find_oo_win_percent(int team_idx, team_t * teams, int team_count) {
  team_t * cur_team = &teams[team_idx];
  cur_team->oo_win_percent = 0.0;
  for( int other_idx = 0; other_idx < team_count; other_idx++ ) {
    if( other_idx == team_idx ) {
      continue;
    }
    if( cur_team->results[other_idx] == DIDNT_PLAY ) {
      continue;
    }
    cur_team->oo_win_percent += teams[other_idx].opponent_win_percent;
  }
  cur_team->oo_win_percent /= (double)cur_team->game_count;
}

#define SKIP_CHAR '.'
#define WIN_CHAR  '1'
#define LOSE_CHAR '0'

void do_trial(istream & input) throw() {
  int team_count;
  input >> team_count;
  
  team_t * teams = new team_t[team_count];
  for( int row = 0; row < team_count; row++ ) {
    team_t * cur_team = teams + row;
    cur_team->results = new game_result[team_count];
    for( int col = 0; col < team_count; col++ ) {
      char ch;
      input >> ch;
      switch( ch ) {
        case SKIP_CHAR:
          cur_team->results[col] =  DIDNT_PLAY;
          break;
        case WIN_CHAR:
          cur_team->win_count ++;
          cur_team->results[col] = WON;
          cur_team->game_count++;
          break;
        case LOSE_CHAR:
          cur_team->game_count ++;
          cur_team->results[col] = LOST;
          break;
      }
    }
  }
  
  for( int i = 0; i < team_count; i++ ) {
    find_opponent_win_percent(i, teams, team_count);
  }
  for( int i = 0; i < team_count; i++ ) {
    find_oo_win_percent(i, teams, team_count);
  }
  for( int i = 0; i < team_count; i++ ) {
    cout << teams[i].rpi() << endl;
  }
  delete []teams;
}

int main (int argc, const char * argv[])
{
  int trialCount;
  istream * in;
  if( argc == 1 ) {
    in = &cin;
  }
  else {
    in = new ifstream(argv[1]);
  }
  istream & input = *in;
  input >> trialCount;
  
  for( int i = 1; i <= trialCount; i ++ ) {
    cout << "Case #" << i << ":\n";
    do_trial(input);
  }
  
  if( argc > 1 ) {
    delete in;
  }
  return 0;
}
