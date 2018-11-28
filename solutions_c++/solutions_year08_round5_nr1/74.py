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

vector<int> rightWalls[6100];
vector<int> downWalls[6100];

ifstream in("happy.txt");;
ofstream out;

int NORTH = 0;
int EAST = 1;
int SOUTH = 2;
int WEST = 3;

void forward(int& row, int& col, int dir)
{
     if (dir == NORTH)
     {
             downWalls[row-1].push_back(col);
             row -= 1;
     }
     else if (dir == SOUTH)
     {
          downWalls[row].push_back(col);
          row += 1;
     }
     else if (dir == EAST)
     {
          rightWalls[col].push_back(row);
          col += 1;
     }
     else
     {
         rightWalls[col-1].push_back(row);
         col -= 1;
     }
}
          
void turn(int& dir, char t)
{
     if (t == 'R')
           dir = (dir + 1) % 4;
     else
         dir = (dir + 3) % 4;
}

void traverse()
{
     int row = 3050;
     int col = 3050;
     int dir = NORTH;
     
     int numTravs;
     in >> numTravs;
     for (int t = 0; t < numTravs; t++)
     {
         int reps;
         string str;
         in >> str >> reps;
         for (int rep = 0; rep < reps; rep++)
         {
             for (int i = 0; i < str.length(); i++)
             {
                 char ch = str[i];
                 if (ch == 'F') forward(row, col, dir);
                 else turn(dir, ch);
             }
         }
     }
     for (int i = 0; i < 6100; i++)
     {
         sort(downWalls[i].begin(), downWalls[i].end());
         sort(rightWalls[i].begin(), rightWalls[i].end());
     }
}
                 
bool hasEastWest(int row, int col)
{
     vector<int>& dw = downWalls[row];
     if (dw.size() < 2) return false;
     if (dw[0] <= col && dw[dw.size() - 1] >= col + 1) return true;
     return false;
}

bool hasNorthSouth(int row, int col)
{
     vector<int>& rw = rightWalls[col];
     if (rw.size() < 2) return false;
     if (rw[0] <= row && rw[rw.size() - 1] >= row + 1) return true;
     return false;
}

bool isInPoly(int row, int col)
{
     vector<int>& rw = rightWalls[col];
     if (rw.size() < 2) return false;
     int total = 0;
     for (int i = 0; i < rw.size(); i++)
     {
         if (rw[i] <= row) total++;
         else break;
     }
     if (total % 2 == 1) return true;
     return false;
}

int main()
{   
    ofstream out("sad.txt");
    int cases;
    in >> cases;
    for (int c = 0; c < cases; c++)
    {
        for (int i = 0; i < 6100; i++)
        {
            rightWalls[i] = vector<int>();
            downWalls[i]= vector<int>();
        }
        traverse();
        cout << "done traversing" << endl;
        
        int total = 0;
        for (int r = 5; r < 6095; r++)
        {
        if (downWalls[r].size() < 2) continue;
        for (int c = 5; c < 6095; c++)
        {
            if (rightWalls[c].size() < 2) continue;
            if ((hasNorthSouth(r, c) || hasEastWest(r,c)) && !isInPoly(r,c)) total++;
        }
        }
        out << "Case #" << (c+1) << ": " << total << endl;
    }
    return 0;
}


    

