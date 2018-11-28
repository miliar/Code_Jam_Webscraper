#include<iostream>
#include<vector>
#include<stdio.h>
#include<sstream>
#include<istream>
#include<fstream>
#include<iterator>
using namespace std;

void bestResult (vector<int> input, int testcase)
{
    int number = input[0];
    int surprises = input [1];
    int score = input[2];
    if (number <= 0)
        return;
    int success = 0;
    for (int iterator = 3; iterator < input.size (); iterator++)
    {
        int value = input [iterator];
        int x = value/3;
        int remainder = value%3;
        switch (remainder)
        {
            case 0:
                if (score <= x)
                {
                    success++;
                    break;
                }
                if (score == x+1 && surprises > 0)
                {
                   if (x-1 < 0)
                     break;
                    surprises--;
                    success++;
                }
                break;
            case 1:
                if (score <= x+1)
                    success++;
                break;
            case 2:
                if (score <=x+1)
                {
                    success++;
                    break;
                }
                if (score == x+2 && surprises > 0)
                {
                    success++;
                    surprises--;
                }
                break;
        }
    }
    cout<<"Case #"<<testcase<<": "<<success<<endl; 
}

int main()
{
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );
    std::string line;
    int size = 0;
    int testcase = 0;
    int num = 0, value;
    getline( std::cin, line );
    std::istringstream a (line);
    a>>value;
    while ( num < value )
    {
        getline( std::cin, line ) ; 
        vector<int> temp;
        testcase++;
        std::istringstream is( line );
        std::copy(std::istream_iterator<int>(is), 
                std::istream_iterator<int>(), 
                std::back_inserter(temp));
        size=0;
        bestResult (temp, testcase);
        num++;
    }
}
