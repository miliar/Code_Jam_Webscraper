// -*- C++ -*-
// Copyright (c) Calypto Design Systems 2010-2011 
/// @(#)bt.cc
///
///
/// @date   05/07/11 11:15:39
/// @author Srihari Yechangunja (syechan@calypto.com)
///
/// @brief  
/// *** DELETE THIS LINE AFTER ADDING COMMENTS HERE ****
/// 
/// $Id$

#include <iostream>
#include <string>

//#define DEBUG

inline unsigned SABS (int num) {
    return (unsigned)((num<0)?(-num):num);
}

using namespace std;

void doTest(int test) {
    unsigned currTime = 0U;
    unsigned N = 0U;
    string currRobot;
    unsigned nextPosition;

    unsigned orangeLastPosition = 1U, blueLastPosition = 1U;
    unsigned orangePrevTime = 0U, bluePrevTime = 0U;
    bool isOrange = false;

    cin >> N;
#ifdef DEBUG
    cerr << "Test " << test << " : N = " << N << endl;
#endif
    for (int n=0; n<N; ++n) {
        cin >> currRobot;
#ifdef DEBUG
        cerr << n << " : currRobot = '" << currRobot << "'" << ends;
#endif
        // Which robot should move now..
        if (currRobot.find('O') != string::npos) {
            isOrange = true;
        } else {
            assert(currRobot.find('B') != string::npos);
            isOrange = false;
        }

        // To where
        cin >> nextPosition;
#ifdef DEBUG
        cerr << ", nextPosition = " << nextPosition << endl;
#endif

        unsigned &lastPos = (isOrange)?orangeLastPosition:blueLastPosition;
        unsigned &prevTime = (isOrange)?orangePrevTime:bluePrevTime;
#ifdef DEBUG
        cerr << "isOrange = " << isOrange << ", lastPos " << lastPos << ", prevTime " << prevTime << endl;
#endif

        unsigned diffPos = SABS((int)(nextPosition - lastPos));
        unsigned diffTime = SABS((int)(currTime - prevTime));
#ifdef DEBUG
        cerr << "diffPos = " << diffPos << ", diffTime " << diffTime << endl;
#endif
        if (diffPos > diffTime) {
            // move to Position
            currTime = currTime + (diffPos-diffTime);
        }
#ifdef DEBUG
        cerr << "Moved " << currRobot << " to pos " << nextPosition << " : currTime = " << currTime << endl;
        cerr << " Orange: lastPos = " << orangeLastPosition  << ", prevTime = " << orangePrevTime << endl;
        cerr << " Blue: lastPos = " << blueLastPosition  << ", prevTime = " << bluePrevTime << endl;
#endif

        // press button
        ++currTime; lastPos = nextPosition; prevTime = currTime;

#ifdef DEBUG
        cerr << "After Button Press: currTime = " << currTime << endl;
        cerr << " Orange: lastPos = " << orangeLastPosition  << ", prevTime = " << orangePrevTime << endl;
        cerr << " Blue: lastPos = " << blueLastPosition  << ", prevTime = " << bluePrevTime << endl;
#endif
    }

    cout << "Case #" << test << ": " << currTime << endl;
}

int main() {
    int T = 0;

    cin >> T;
#ifdef DEBUG
    cerr << "T = " << T << endl;
#endif

    for (int t=1; t<=T; ++t) {
        doTest(t);
    }

    return 0;
}

