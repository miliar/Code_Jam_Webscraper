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
#include <map>

using namespace std;

char combine(map< pair<char, char>, char> combine , char first, char second)
{
    char result;
    
    if (first < second)
        result = combine[make_pair(first, second)];
    else
        result = combine[make_pair(second, first)];
    
    if (! result)
        result = ' ';
    
  //  cout << "Combining: " << first << " and " << second << " result: " << result << '\n';
    
    return result;
}

bool oppose(map< pair<char, char> , int> oppose, char first, char second)
{
    if (first < second && oppose[make_pair(first, second)] > 0)
    {
  //      cout << first << " and " << second << " are opposed" << '\n';
        return true;
    }
    
    if (second < first && oppose[make_pair(second, first)] > 0)
    {
 //       cout << first << " and " << second << " are opposed" << '\n';
        return true;
    }
    
  //  cout << first << " and " << second << " are NOT opposed" << '\n';
    return false;
}

int main (int argc, const char * argv[])
{
    char a, b, c;
    int numCases, caseNum;
    
    ifstream infile;
    infile.open("/Users/oliver/Documents/Google Code Jam/Magicka/Magicka/Magicka/B-small-attempt0.in");
    
    ofstream outfile;
    outfile.open("/Users/oliver/Documents/Google Code Jam/Magicka/Magicka/Magicka/output.txt");
    
    infile >> numCases;
    infile.ignore(256, '\n');
    
    map< pair<char, char>, char> combineMap;
    map< pair<char,char>, int > opposeMap;
    vector<char> final;
    
    char lastLetter, combinedLetter;
    
    int numCombine(0), numOppose(0), numLetters(0);
    
    bool opposed;
    
    for (caseNum = 1; caseNum <= numCases; caseNum++)
    {
        outfile << "Case #" << caseNum << ": ";
        
      //  cout << "Case " << caseNum << '\n';
        
        infile >> numCombine;
        infile.ignore(1);
        
       // cout << numCombine << '\n';
        
        for (int i = 1; i <= numCombine; i++)
        {
            a = infile.get();
            b = infile.get();
            c = infile.get();
            infile.ignore(1);
            
            if (a < b)
                combineMap[make_pair(a,b)] = c;
            else
                combineMap[make_pair(b,a)] = c;
        }
        
        infile >> numOppose;
        infile.ignore(1);
        
       // cout << numOppose << '\n';
        
        for (int i = 1; i <= numOppose; i++)
        {
            a = infile.get();
            b = infile.get();
            infile.ignore(1);
            
            if (a < b)
                ++opposeMap[make_pair(a,b)];
            else
                ++opposeMap[make_pair(b,a)];
        }
        
        infile >> numLetters;
        infile.ignore(1);
        
        for (int i = 1; i <= numLetters; i++)
        {
            c = infile.get();
            
            if (final.size() > 0)
            {
                lastLetter = final.at(final.size() - 1);
                combinedLetter = combine(combineMap, lastLetter, c);
                
                if (combinedLetter != ' ')
                {
                    final.pop_back();
                    final.push_back(combinedLetter);
                }
                else
                {
                    opposed = false;
                    
                    for (vector<char>::const_iterator it = final.begin(); it < final.end() && opposed == false; it++)
                    {
                        if (oppose(opposeMap, *it, c))
                        {
                            opposed = true;
                        }
                    }
                    
                    if(opposed)
                        final.clear();
                    else
                        final.push_back(c);
                }
            }
            else
            {
              //  cout << "Adding " << c << " to the list" << '\n';
                final.push_back(c);
            }
        }
        
        infile.ignore(256, '\n');
        
        if (final.size() == 0)
            outfile << "[]" << '\n';
        else
        {
            outfile << "[";
            
            for (vector<char>::const_iterator it = final.begin(); it < final.end(); it++)
            {
                if (it == final.begin())
                    outfile << *it;
                else
                    outfile << ", " << *it;
            }
            
            outfile << "]" << '\n';
        }
        
        final.clear();
        opposeMap.clear();
        combineMap.clear();
    }
    
    infile.close();
    outfile.close();
}

