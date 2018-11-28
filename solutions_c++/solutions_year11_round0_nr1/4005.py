//
//  main.cpp
//  ClosingTheLoop
//
//  Created by Oliver Foggin on 15/04/2011.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int moveBotToButton(int currLoc, int destLoc)
{
    if (currLoc == destLoc)
        return currLoc;
    if (currLoc < destLoc)
        return ++currLoc;
    if (currLoc > destLoc)
        return --currLoc;
    
    return 0;
}

int main (int argc, const char * argv[])
{
    char c;
    int numCases, caseNum;
    
    ifstream infile;
    infile.open("/Users/oliver/Documents/Google Code Jam/TrustBot/TrustBot/large.in");
    
    ofstream outfile;
    outfile.open("/Users/oliver/Documents/Google Code Jam/TrustBot/TrustBot/output.txt");
    
    infile >> numCases;
    infile.ignore(256, '\n');
    
    int orangeLoc(1), blueLoc(1), numButtonPresses(0), buttonNum(0), timeTaken(0), buttonsPressed(0), oButtonsPressed(0), bButtonsPressed(0);
    vector<int> orangeButtons, blueButtons;
    vector< pair<char, int> > instructionSet;
    
    for (caseNum = 1; caseNum <= numCases; caseNum++)
    {
        outfile << "Case #" << caseNum << ": ";
        
      //  cout << "Case #" << caseNum << '\n';
        
        infile >> numButtonPresses;
        infile.ignore(1);
        
        for (int i = 1; i <= numButtonPresses; i++)
        {
            c = infile.get();
            infile.ignore(1);
            infile >> buttonNum;
            infile.ignore(1);
            
            instructionSet.push_back(make_pair(c, buttonNum));
            
            if (c == 'O')
                orangeButtons.push_back(buttonNum);
            else
                blueButtons.push_back(buttonNum);
        }
        
        while (buttonsPressed < numButtonPresses)
        {
            timeTaken++;
            
            pair<char, int> currentInstruction = instructionSet.at(buttonsPressed);
            
      //      cout << "Target button : " << currentInstruction.first << currentInstruction.second << " Orange Loc : " << orangeLoc << " Blue Loc : " << blueLoc << " Time Taken : " << timeTaken << '\n';
            
            bool orangeDone(false), blueDone(false);
            
            if (currentInstruction.first == 'O' && orangeLoc == currentInstruction.second)
            {
                buttonsPressed++;
                oButtonsPressed++;
                orangeDone = true;
            }
            else if (currentInstruction.first == 'B' && blueLoc == currentInstruction.second)
            {
                buttonsPressed++;
                bButtonsPressed++;
                blueDone = true;
            }
            
            if (!orangeDone && orangeButtons.size() > 0 && oButtonsPressed < orangeButtons.size())
                orangeLoc = moveBotToButton(orangeLoc, orangeButtons.at(oButtonsPressed));
            if (!blueDone && blueButtons.size() > 0 && bButtonsPressed < blueButtons.size())
                blueLoc = moveBotToButton(blueLoc, blueButtons.at(bButtonsPressed));
        }
        
        outfile << timeTaken << '\n';
        
        orangeButtons.clear();
        blueButtons.clear();
        instructionSet.clear();
        orangeLoc = 1;
        blueLoc = 1;
        buttonsPressed = 0;
        oButtonsPressed = 0;
        bButtonsPressed = 0;
        timeTaken = 0;
    }
    
    infile.close();
    outfile.close();
}

