#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
using namespace std;

bool changeable[11000];
bool value[11000];
int memo[11000][3];
int numNodes;

int BAD = 1000000;

int minChanges(int nodeNum, int val)
{
    if (val == 2) return 0;
    if (memo[nodeNum][val] >= 0) return memo[nodeNum][val];
    if (nodeNum * 2 > numNodes) //this is a leaf node
    {
       if (value[nodeNum] == val) return 0;
       return BAD;
    }
    //so now we know it's not a leaf node
    if (!value[nodeNum] && val == 1) //it's OR
    {
       int result1 = minChanges(nodeNum*2, 1) + minChanges(nodeNum*2+1, 2);
       int result2 = minChanges(nodeNum*2, 2) + minChanges(nodeNum*2+1, 1);
       int minRes = min(result1, result2);
       if (minRes >= BAD) 
          minRes = BAD;
       memo[nodeNum][val] = minRes;
    }
    else if (!value[nodeNum] && val == 0) //it's OR
    {
       int result1 = minChanges(nodeNum*2, 0) + minChanges(nodeNum*2+1, 0);
       int result2 = BAD, result3 = BAD;
       if (changeable[nodeNum])
       {
          result2 = 1+ minChanges(nodeNum*2, 0) + minChanges(nodeNum*2+1, 2);
          result3 = 1+ minChanges(nodeNum*2, 2) + minChanges(nodeNum*2+1, 0);
       }
       int minRes = min(result3, min(result1, result2));
       if (minRes >= BAD) minRes = BAD;
       memo[nodeNum][val] = minRes;
    }
    else if (value[nodeNum] && val == 1) //it's AND
    {
       int result1 = minChanges(nodeNum*2, 1) + minChanges(nodeNum*2+1, 1);
       int result2 = BAD, result3 = BAD;
       if (changeable[nodeNum])
       {
          result2 = 1+ minChanges(nodeNum*2, 1) + minChanges(nodeNum*2+1, 2);
          result3 = 1+ minChanges(nodeNum*2, 2) + minChanges(nodeNum*2+1, 1);
       }
       int minRes = min(result3, min(result1, result2));
       if (minRes >= BAD) minRes = BAD;
       memo[nodeNum][val] = minRes;
    }
    else if (value[nodeNum] && val == 0) //it's OR
    {
       int result1 = minChanges(nodeNum*2, 0) + minChanges(nodeNum*2+1, 2);
       int result2 = minChanges(nodeNum*2, 2) + minChanges(nodeNum*2+1, 0);
       int minRes = min(result1, result2);
       if (minRes >= BAD) minRes = BAD;
       memo[nodeNum][val] = minRes;
    }
    return memo[nodeNum][val];
}

int main()
{
    ifstream infile("happy.txt");
    ofstream outfile("sad.txt");
    
    int cases;
    infile >> cases;
    for (int c = 0; c < cases; c++)
    {
        for (int i = 0; i < 11000; i++)
        {
            memo[i][0] = -1;
            memo[i][1] = -1;
            memo[i][2] = -1;
        }
        
        int theval;
        infile >> numNodes >> theval;
        for (int i = 0; i < (numNodes - 1) / 2; i++)
        {
            infile >> value[i+1] >> changeable[i+1];
        }
        for (int i = (numNodes - 1) / 2; i < numNodes; i++)
        {
            int val;
            infile >> val;
            value[i+1] = val;
        }
        
        int result = minChanges(1, theval);
        if (result == BAD)
           outfile << "Case #" << (c+1) << ": IMPOSSIBLE" << endl;
        else
            outfile << "Case #" << (c+1) << ": " << result << endl;
     //     system("PAUSE");
    }
    return 0;       
    
}
