#include <iostream>
#include <strstream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <iterator>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define MAXINT 99999

using namespace std;

void doit(int** matrix, char** resmatrix, const int H, const int W)
{
    char clab = 'a';
    for(int j = 0; j < H; j++)
    {
        for(int k = 0; k < W; k++)
        {
            if(resmatrix[j][k] >= 'a' && resmatrix[j][k] <= 'z')
                continue;
            int cj = j, ck = k;
            while(true)
            {
                resmatrix[cj][ck] = clab;
                //find next point
                int n = MAXINT, w = MAXINT, e = MAXINT, s = MAXINT;
                n = cj-1 >= 0 ? matrix[cj-1][ck]:MAXINT;
                w = ck-1 >= 0 ? matrix[cj][ck-1]:MAXINT;
                e = ck+1 < W ? matrix[cj][ck+1]:MAXINT;
                s = cj+1 < H ? matrix[cj+1][ck]:MAXINT;
                if ( n == w == e == s == MAXINT)
                    return;//TODO
                if ( n <= w && n <= e && n <= s && n < matrix[cj][ck])
                        cj--;
                else if ( w <= n && w <= e && w <= s && w < matrix[cj][ck])
                        ck--;
                else if ( e <= n && e <= w && e <= s && e < matrix[cj][ck])
                        ck++;
                else if ( s <= n && s <= w && s <= e && s < matrix[cj][ck])
                        cj++;
                else
                {//sink
                    clab++;
                    break;
                }
                if(resmatrix[cj][ck]>='a'&&resmatrix[cj][ck]<='z')
                {
                    for(int ii = 0; ii < H; ii++)
                        for(int jj = 0; jj < W; jj++)
                            if(resmatrix[ii][jj] == clab)
                                resmatrix[ii][jj] = resmatrix[cj][ck];
                    break;
                }
            }
        }
    }
}

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int casenum = 0;
    int H = 0, W = 0;
    int** matrix = NULL;
    char** resmatrix = NULL;
    fin>>casenum;
    for(int i = 0; i < casenum; i++)
    {
        fin>>H>>W;
        matrix = new int*[H];
        resmatrix = new char*[H];
        for(int j = 0; j < H; j++)
        {
            matrix[j] = new int[W];
            resmatrix[j] = new char[W];
            for(int k = 0; k < W; k++)
            {
                fin>>matrix[j][k];
                //cout<<matrix[j][k]<<" ";
                resmatrix[j][k] = '\0';
            }
            //cout<<endl;
        }
        //do it
        doit(matrix, resmatrix, H, W);
        fout<<"Case #"<<i+1<<":"<<endl;
        for(int j = 0; j < H; j++)
        {
            for(int k = 0; k < W; k++)
            {
                fout<<resmatrix[j][k]<<" ";
            }
            fout<<endl;
        }
        //clean
        for(int j = 0; j < H; j++)
        {
            delete[] matrix[j];
            delete[] resmatrix[j];
        }
        delete[] matrix;
        delete[] resmatrix;
        matrix = NULL;
        resmatrix = NULL;
    }
    return 0;
}
