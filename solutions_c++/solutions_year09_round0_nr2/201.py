//jhurwitz

#include <fstream>
#include <iostream>
#include <stdio.h>

using namespace std;
ifstream fin("b-large.in");
ofstream fout("b-large.out");

int H, W;
int map[101][101];
int basins[101][101];
int next[101][101][2];
int lastbasin=-1;

void fill(int component)
{
    int changed;
    do
    {
        changed = 0;
        for (int i=0; i<H; i++)
            for (int j=0; j<W; j++)
                if (basins[i][j]==-2)
                {
                    changed++;
                    if (i+1<H && basins[i+1][j]==-1 && next[i+1][j][0]==i && next[i+1][j][1]==j) //south
                        basins[i+1][j] = -2;
                    if (j+1<W && basins[i][j+1]==-1 && next[i][j+1][0]==i && next[i][j+1][1]==j) //east
                        basins[i][j+1] = -2;
                    if (j-1>=0 && basins[i][j-1]==-1 && next[i][j-1][0]==i && next[i][j-1][1]==j) //west
                        basins[i][j-1] = -2;
                    if (i-1>=0 && basins[i-1][j]==-1 && next[i-1][j][0]==i && next[i-1][j][1]==j) //north
                        basins[i-1][j] = -2;
                    
                    int ni=next[i][j][0]; int nj=next[i][j][1];
                    if (basins[ni][nj]==-1)
                        basins[ni][nj] = -2;
                    
                    basins[i][j] = component;
                }
    }
    while (changed>0);
}

void problem(int casenum)
{
    memset(map, 0, sizeof(map));
    
    fin >> H >> W;
    for (int i=0; i<H; i++)
        for (int j=0; j<W; j++)
            fin >> map[i][j];
    
    memset(basins, -1, sizeof(basins));
        
    for (int i=0; i<H; i++)
        for (int j=0; j<W; j++)
        {
            next[i][j][0]=i; next[i][j][1]=j;
            if (i-1>=0 && map[i-1][j]<map[next[i][j][0]][next[i][j][1]]) //north
            { next[i][j][0]=i-1; next[i][j][1]=j; }
            if (j-1>=0 && map[i][j-1]<map[next[i][j][0]][next[i][j][1]]) //west
            { next[i][j][0]=i; next[i][j][1]=j-1; }
            if (j+1<W && map[i][j+1]<map[next[i][j][0]][next[i][j][1]]) //east
            { next[i][j][0]=i; next[i][j][1]=j+1; }
            if (i+1<H && map[i+1][j]<map[next[i][j][0]][next[i][j][1]]) //south
            { next[i][j][0]=i+1; next[i][j][1]=j; }
        }
    
    int nextcomp = 0;
    for (int i=0; i<H; i++)
        for (int j=0; j<W; j++)
            if (basins[i][j]==-1)
            {
                basins[i][j]=-2;
                fill(nextcomp);
                nextcomp++;
            }
    
    fout << "Case #" << casenum << ":" << endl;
    for (int i=0; i<H; i++)
    {
        for (int j=0; j<W; j++)
            fout << (char)(basins[i][j]+'a') << ' ';
        fout << endl;
    }
}

int main()
{
    int N;
    fin >> N;
    
    for (int i=1; i<=N; i++)
        problem(i);
    
    return 0;
}
