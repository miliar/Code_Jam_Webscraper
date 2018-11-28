#include <vector>
#include <fstream>
#include <iostream>
#include <cmath>
#include <string>

using namespace std;
int calcMinTime(string s)
{
    int base;
    vector<char> letters;
    for(int i = 0; i < s.size(); i++)
    {
        char nextLetter = s.at(i);
        vector<char>::iterator itr;
        bool found = false;
        for(itr = letters.begin(); itr != letters.end(); itr++)
        {
            if(*itr == nextLetter)
            {
                found = true;
                break;
            }
        }
        if(!found)
        {
            letters.push_back(nextLetter);
        }
    }
    base = letters.size();
    if(base < 2)
        base = 2;

    int toReturn = 0;
    for(int i = 0; i < s.size(); i++)
    {
        char nextLetter = s.at(i);
        vector<char>::iterator itr;
        int count = 0;
        for(itr = letters.begin(); itr != letters.end(); itr++)
        {
            if(*itr == nextLetter)
            {
                int nextPlace = count;
                if(count == 0)
                    nextPlace = 1;
                if(count == 1)
                    nextPlace = 0;
                int x = s.length();
                toReturn += nextPlace * pow((double)base,(int)s.length()-i - 1);
                break;
            }
            count++;
        }
    }

    return toReturn;
}

int main()
{
    ifstream myFile("problem1.txt");
    ofstream myAnswer("answer1.txt");
    if (myFile.is_open())
    {
        int T;
        myFile >> T;
        string temp;
        getline(myFile, temp);
        
        for(int tc = 1; tc <= T; tc++)
        {
            string nextCase;
            getline(myFile, nextCase);
            myAnswer << "Case #" << tc << ": " << calcMinTime(nextCase) << endl;
        }
    }
}