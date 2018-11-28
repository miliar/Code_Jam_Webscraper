//
//  bot_trust.cpp
//  code_jam
//
//  Created by Paul O'Neil on 5/7/11.
//  Copyright 2011 Paul O'Neil. All rights reserved.
//

#include <iostream>
#include <list>
#include <fstream>
using namespace std;

#define min(a, b) ( (a) < (b) ? (a) : (b) )

struct instruction {
  char bot;
  char pos;
  int step_num;
  
  instruction(char b, char l, int s) : bot(b), pos(l), step_num(s) { }
};

struct bot {
  list<instruction> steps;
  int pos;
  bot() : steps(), pos(1) { }
  
  int dist_from_button() throw() {
    if( !steps.size() ) {
      return 0;
    }
    
    return abs(steps.front().pos - pos);
  }
  
  bool atStep(int s) throw() {
    if( !steps.size() ) {
      return false;
    }
    return steps.front().step_num == s;
  }
  
  // the direction to the next step
  int dir() throw() {
    if( !steps.size() || steps.front().pos == pos ) {
      return 0;
    }
    else if( steps.front().pos > pos ) {
      return 1;
    }
    else if( steps.front().pos < pos ) {
      return -1;
    }
  }
};

inline static int bot_idx(char idx) throw(char) {
  switch(idx) {
    case 'O':
      return 0;
    case 'B':
      return 1;
    default:
      throw idx;
  }
}

int do_trial(istream &input) throw();

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
    cout << "Case #" << i << ": " << result << endl;
  }
  
  if( argc > 1 ) {
    delete in;
  }
  return 0;
}

// true if steps remaining for a bot
bool bot_with_next_step(bot bots[2], int s, bot ** next, bot ** bkg) {
  if( bots[0].atStep(s) ) {
    (*next) = &bots[0];
    (*bkg) = &bots[1];
    return true;
  }
  else if( bots[1].atStep(s) ) {
    (*next) = &bots[1];
    (*bkg) = &bots[0];
    return true;
  }
  else { // assume that neither of the bots have any steps left
    (*next) = (*bkg) = NULL;
    return false;
  }
}

int do_trial(istream & input) throw() {
  bot bots[2];
  int stepCount;
  input >> stepCount;
  for( int i = 1; i <= stepCount; i++ ) {
    char botChar;
    int buttonLoc;
    input >> botChar >> buttonLoc;
    bots[bot_idx(botChar)].steps.push_back(instruction(botChar, buttonLoc, i));
  }
  
  int moveCount = 0;
  bot * next; // the bot that presses the next button
  bot * bkg;  // the bot advancing in the background
  for( int curStep = 1; curStep <= stepCount; curStep++ ) {
    bot_with_next_step(bots, curStep, &next, &bkg);
    
    int to_complete_step = next->dist_from_button(); // move to the button
    next->pos = next->steps.front().pos;
    to_complete_step += 1; // push the button
    
    bkg->pos += min(to_complete_step, bkg->dist_from_button())  * bkg->dir();
    next->steps.pop_front();
    
    moveCount += to_complete_step;
  }
  return moveCount;
}
