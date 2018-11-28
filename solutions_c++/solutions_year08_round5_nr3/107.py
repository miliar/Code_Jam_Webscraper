#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <algorithm>
using namespace std;

int memo[20][1024];
bool broken[20][20];
int rows, cols;

int calcMemo(vector<bool> vec)
{
    int total = 0;
    int mult = 512;
    for (int i = 0; i < vec.size(); i++)
    {
        if (vec[i]) total += mult;
        mult = mult / 2;
    }
    return total;
}

vector<bool> fromMemo(int i)
{
    vector<bool> vec(10);
    int mult = 512;
    int ind = 0;
    while (mult > 0)
    {
          if (i >= mult)
          {
                vec[ind] = 1;
                i -= mult;
          }
          ind++;
          mult /= 2;
    }
    return vec;
}

int calcTotal(vector<bool> vec)
{
    int total = 0;
    for (int i = 0; i < 10; i++)
    {
        if (vec[i]) total++;
    }
    return total;
}

bool isCorrect(vector<bool> back, vector<bool> front, int backRow)
{
     for (int i = 0; i < 10; i++)
     {
         if (i >= cols && back[i]) return false;   
         
         if (i < 9 && back[i] && back[i+1]) return false;
         if (broken[backRow][i] && back[i]) return false;
         
         if (i > 0 && back[i] && front[i-1]) return false;
         if (i < 9 && back[i] && front[i+1]) return false;
     }
     return true;
}

int recurse(int backRow, vector<bool> frontSet)
{
    if (backRow == rows) return 0;
    
    int frontMemo = calcMemo(frontSet);
    
    if (memo[backRow][frontMemo] >= 0) return memo[backRow][frontMemo];
    
    int themax = 0;
    for (int i = 0; i < 1024; i++)
    {
        vector<bool> backSet = fromMemo(i);
        if (!isCorrect(backSet,frontSet, backRow)) continue;
        int now = calcTotal(backSet);
        now += recurse(backRow + 1, backSet);
        if (now > themax) themax = now;
    }
    
    memo[backRow][frontMemo] = themax;
    return themax;
}

int main()
{
    ifstream in("happy.txt");
    ofstream out("sad.txt");
    int cases;
    in >> cases;
    
    for (int c = 0; c < cases; c++)
    {
        for (int i = 0; i < 20; i++)
        for (int j = 0; j < 1024; j++)
            memo[i][j] = -1;
        
        in >> rows >> cols;
        string str;
        for (int i = 0; i < rows; i++)
        {
            in >> str;
            for (int j = 0; j < cols; j++)
            {
                if (str[j] == 'x') broken[i][j] = true; else broken[i][j] = false;
            }
        }
        vector<bool> def(10);
        int rec = recurse(0, def);
        out << "Case #" << (c+1) << ": " << rec << endl;
    }
    return 0;
}
    

