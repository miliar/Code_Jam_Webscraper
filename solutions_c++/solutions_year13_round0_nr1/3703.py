//
//  main.cpp
//  GoogleCodeJam2013_TicTacToe
//
//  Created by Surasak Sermluxananon on 4/13/56 BE.
//  Copyright (c) 2556 Surasak Sermluxananon. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <set>
using namespace std;

typedef set<float>        CBoardSet;
CBoardSet   mXset = CBoardSet();
CBoardSet   mOset = CBoardSet();

void printSet(const CBoardSet &mSet, const string &sKey)
{
    CBoardSet::iterator itSet = mSet.begin();
    while (itSet != mSet.end())
    {
        cout << sKey << " : " << *itSet << endl;
        ++itSet;
    }
}

int main(int argc, const char * argv[])
{
    string input_line;
    ifstream input_file;
    ofstream output_file;
    
    input_file.open (argv[1]);
    output_file.open(argv[2]);
    if (input_file.is_open())
    {
        int iCase = 0, iTotalCase = 0, iCount = 0;
        bool XBingo = false, OBingo = false, bDot = false;
        while (input_file.good())
        {
            getline (input_file, input_line);
            if(iTotalCase == 0)
            {
                iTotalCase = atoi(input_line.c_str());
                iCase = iTotalCase;
            }
            else if(input_line != "")
            {
                int iXRowCount = 0, iORowCount = 0;
                for(int i = 0; i < 4;++i)
                {
                    float fKey = (float)iCount + ((float)i/10);
                    switch (input_line[i])
                    {
                        case 'X': { mXset.insert(fKey); ++iXRowCount; break; }
                        case 'O': { mOset.insert(fKey); ++iORowCount; break; }
                        case 'T':
                        {
                            mXset.insert(fKey);
                            mOset.insert(fKey);
                            ++iORowCount;
                            ++iXRowCount;
                            break;
                        }
                        case '.': bDot = true;
                        default: break;
                    }
                }
                
                //Verify Row
                if(iXRowCount > 3)   { XBingo = true; }
                if(iORowCount > 3)   { OBingo = true; }
                
                if(iCount > 2 && !XBingo && !OBingo)
                {
                    //Verify Column
                    for(int i = 0;i < 4;++i)
                    {
                        bool bX = true, bO = true;
                        for(int j = 0; j < 4;++j)
                        {
                            bX &= mXset.find((float)iCount - j + ((float)i/10)) != mXset.end();
                            bO &= mOset.find((float)iCount - j + ((float)i/10)) != mOset.end();
                        }
                        if((XBingo = bX))     break;
                        if((OBingo = bO))     break;
                    }
                    
                    //Verify Diagonal
                    if((mXset.find(0) != mXset.end() && mXset.find(1.1) != mXset.end() &&
                       mXset.find(2.2) != mXset.end() && mXset.find(3.3) != mXset.end()) ||
                       (mXset.find(0.3) != mXset.end() && mXset.find(1.2) != mXset.end() &&
                        mXset.find(2.1) != mXset.end() && mXset.find(3) != mXset.end()))
                    {
                        XBingo = true;
                    }
                    if((mOset.find(0) != mOset.end() && mOset.find(1.1) != mOset.end() &&
                        mOset.find(2.2) != mOset.end() && mOset.find(3.3) != mOset.end()) ||
                       (mOset.find(0.3) != mOset.end() && mOset.find(1.2) != mOset.end() &&
                        mOset.find(2.1) != mOset.end() && mOset.find(3) != mOset.end()))
                    {
                        OBingo = true;
                    }
                }
                
                ++iCount;
            }
            else
            {
                if(iCase > 0)
                {
                    //printSet(mXset, "X");
                    //printSet(mOset, "O");
                    string sOutput = "Game has not completed";
                    if(!bDot && !XBingo && !OBingo)  { sOutput = "Draw";  }
                    else if(XBingo)                  { sOutput = "X won"; }
                    else if(OBingo)                  { sOutput = "O won"; }
                    
                    --iCase;
                    cout << "Case #" << iTotalCase - iCase << ": " << sOutput << endl;
                    output_file << "Case #" << iTotalCase - iCase << ": " << sOutput << endl;
                    iCount = 0;
                    bDot = false;
                    XBingo = false;
                    OBingo = false;
                    mXset.clear();
                    mOset.clear();
                }
            }
        }
    }
    input_file.close();
    output_file.close();
    return 0;
}

