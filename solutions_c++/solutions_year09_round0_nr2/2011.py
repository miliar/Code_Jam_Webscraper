/*
Task: B
Lang: C++
*/

#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <stack>

#define SP system("pause")

using namespace std;

ifstream ff;
ofstream of;
char v;
int H,W;
int G[101][101];
char G1[101][101];
char dfs(int x, int y)
{
    // SP;
     int n=G[x][y],s=n,w=n,e=n;
     if(x>0 && G[x-1][y]<G[x][y])n=G[x-1][y];
     if(y>0 && G[x][y-1]<G[x][y])w=G[x][y-1];
     if(y<W-1 && G[x][y+1]<G[x][y])e=G[x][y+1];
     if(x<H-1 && G[x+1][y]<G[x][y])s=G[x+1][y];
     if(n<G[x][y] && n<=e && n<=w && n<=s){G1[x][y]=dfs(x-1,y);}
     else
     if(w<G[x][y] && w<n && w<=e && w<=s){G1[x][y]=dfs(x,y-1);}
     else
     if(e<G[x][y] && e<n && e<w && e<=s){G1[x][y]=dfs(x,y+1);}
     else
     if(s<G[x][y] && s<n && s<e && s<w){G1[x][y]=dfs(x+1,y);}
         if(G1[x][y]=='W'){G1[x][y]=v;v++;return v-1;}
         else return G1[x][y];
    
}

int main()
{
    ff.open("B-large.in");
    of.open("B-large.out");
    int N;
    ff>>N;
    for(int z=0; z<N; z++)
    {
            ff>>H>>W;
            for(int i=0; i<H;  i++)
            {
                    for(int j=0; j<W; j++)
                    {
                            ff>>G[i][j];
                            G1[i][j]='W';
                    }
                    
            }
            v='a';
            for(int i=0; i<H; i++)
            for(int j=0; j<W; j++)
            dfs(i,j);
            of<<"Case #"<<z+1<<":"<<endl;
            for(int i=0; i<H; i++)
            {
            for(int j=0; j<W; j++)
            {
                    of<<G1[i][j]<<" ";
            }
            of<<endl;
            }
    }
  //  SP;
    return 0;
}
