/*
 * =====================================================================================
 *
 *       Filename:  alienLanguage.cpp
 *
 *    Description:
 *           
 *            How to run:   ./a.out inputfile outputfile
 *
 *        Version:  1.0
 *        Created:  09/03/2009 09:26:33 PM
 *       Revision:  none
 *       Compiler:  g++
 *
 *         Author:  Mehul Rathod ( rathodmehul@gmail.com )
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <set>

using namespace std;


void solveAProblem(int no, int wordLength, vector<string> &dictionary, ifstream &din, ofstream &dout)
{    

    string line;
    getline(din,line);

    
    vector<set<char> > messageData(wordLength);
    set<char>::iterator it;


    int groupingOn = 0;
    int currPos    = 0;

    for(int i=0; i < line.size(); i++)
    {

        switch(line[i])
        {
            case '(':
                {
                    groupingOn = 1;
                    break;
                }
            case ')':
                {
                    groupingOn = 0;
                    currPos++;
                    break;
                }
            case '\n':
                {
                    break;
                }    
            default:
                {
                    messageData[currPos].insert(line[i]);    

                    if(groupingOn == 0)
                        currPos++;
                    break; 
                }
        }
    }    

    int matches = 0;

    for(unsigned int i=0; i<dictionary.size(); i++)
    {
        string word(dictionary[i]);
       

        int possible = 1;    

        for(int j=0; j < wordLength; j++)
        {
            it = messageData[j].find(word[j]);


            if(it == messageData[j].end())
            {
                possible = 0;
            } 
            
        }    

        if(possible==1)
            matches++;
    }    
        

    

    dout << "Case #" << (no+1) << ": ";
    dout <<  matches  << endl;
}


int main(int argc, char** argv)
{
    if(argc < 3)
        return 0;


    ifstream din(argv[1]);
    ofstream dout(argv[2]);

    int L,D,N;
    
    din >> L;    
    din >> D;    
    din >> N;    

    string newLine;
    getline(din,newLine);

    vector<string> dictionary(D);

    for(int i=0; i < D; i++)
    {
        string word;
        getline(din,word);
        dictionary[i] = word;
    }

    for(int i=0; i < N; i++)
    {
        solveAProblem(i,L,dictionary,din,dout);
    }

    din.close();
    dout.close();

    return 0;

}


    

