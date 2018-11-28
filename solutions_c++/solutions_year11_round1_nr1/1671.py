//
//  code_jam
//
//  Created by Paul O'Neil on 5/20/11.
//  Copyright 2011 Paul O'Neil. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

//#define PRINT(exp) cout << #exp << " = " << (exp) << endl
#define PRINT(exp)

int gcd(int a, int b) {
  if( b == 0) {
    return a;
  }
  return gcd(b, a % b);
}

bool do_trial(istream & input) throw() {
  int max_today, today_win_percent, total_win_percent;
  input >> max_today >> today_win_percent >> total_win_percent;
  
  // compute games won today, for each possible number of games played
  bool broken = true;
  if( total_win_percent == 0 ) {
    if( today_win_percent > 0 ) {
      return false;
    }
    else {
      return true;
    }
  }
  if( total_win_percent == 100 ) {
    if( today_win_percent != 100 ) {
      return false;
    }
  }
  for( int games_played_today = 1; games_played_today <= max_today && broken; games_played_today++ ) {
    int games_won_today = today_win_percent * games_played_today;
    if( (games_won_today) % 100 != 0 ) {
      continue;
    }
    games_won_today /= 100;
    
    int b = total_win_percent * games_played_today - 100 * games_won_today;
    PRINT(b);
    if( b == 0 ) {
      broken = total_win_percent != today_win_percent;
      continue;
    }
    b *= -1;
    while( b < 0 ) {
      b += 100;
    }
    int d = gcd(total_win_percent, 100);
    PRINT(games_played_today);
    PRINT(games_won_today);
    PRINT(total_win_percent);
    PRINT(b);
    PRINT(d);
    broken = ((b % d) != 0);
  }
  
  return !broken;
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
    int result = do_trial(input);
    cout << "Case #" << i << ": " << (result ? "Possible" : "Broken") << endl;
  }
  
  if( argc > 1 ) {
    delete in;
  }
  return 0;
}
