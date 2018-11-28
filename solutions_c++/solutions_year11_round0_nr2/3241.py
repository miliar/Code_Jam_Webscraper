/*
 * =====================================================================================
 *
 *       Filename:  main.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Moritz Schaefer (), mollitz@gmail.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <map>

using namespace std;



void preCalculation()
{}

string calculate()
{
    vector<string> combiners;
    vector<string> opposers;
    string input;
    vector<char> output;
    int count; 
    cin >> count;
    for(int i=0; i< count; i++) //Read in combiners
    {
        string in;
        cin >> in;
        combiners.push_back(in);
    }
    cin >> count;
    for(int i=0; i<count; i++) //Read in opposers
    {
        string in;
        cin >> in;
        opposers.push_back(in);
    }
    cin >> count; //integer verwerfen
    cin >> input;

    for(int i=0; i< input.size(); i++)
    {
        output.push_back(input.at(i));
        char last = output[output.size()-1];
        char preLast = output[output.size()-2];
        for(int x=0;x<combiners.size(); x++)
        {
            if((last == combiners[x][0] && preLast == combiners[x][1]) || (last == combiners[x][1] && preLast ==
                combiners[x][0]))
            {
                output.pop_back();
                output[output.size()-1] = combiners[x][2];
            }
        }
        for(int x=0;x<opposers.size(); x++)
        {
            if(output[output.size()-1] == opposers[x][0])
            {
                //output nach opposers[x][1] durchsuchen. wenn da, dann löschen und break
                for(int y=0; y<output.size()-1; y++)
                {
                    if(output[y] == opposers[x][1])
                    {
                        output.clear();
                        break;
                    }
                }
            }
            if(output[output.size()-1] == opposers[x][1])
            {
                //output nach opposers[x][0] durchsuchen. wenn da, dann löschen und break
                for(int y=0; y<output.size()-1; y++)
                {
                    if(output[y] == opposers[x][0])
                    {
                        output.clear();
                        break;
                    }

                }
            }
        }
    }
    string outputString;
    outputString.push_back('[');
    for(int i=0; i<output.size(); i++)
    {
        if(i)
        {
            outputString += ", ";
        }
        outputString.push_back(output[i]);
    }
    outputString.push_back(']');

    return outputString;


}


int main(int argc, char *argv[])
{
    int cases;
    cin >> cases;
    preCalculation();
    for(int i = 0; i < cases; i++)
    {
        cout << "Case #" << i+1 << ": " << calculate() << endl;
    }
    return 0;
}
