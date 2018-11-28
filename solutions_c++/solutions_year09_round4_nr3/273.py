#include <fstream>
#include <cstring>
#include <sstream>
#include <map>
#include <iostream>
#include <algorithm>

using namespace std;

int square[100];

#define M 128
#define N 128

bool graph[M][N];
bool seen[N];
int matchL[M], matchR[N];
int n, m;

bool bpm( int u )
{
    for( int v = 0; v < n; v++ ) if( graph[u][v] )
    {
        if( seen[v] ) continue;
        seen[v] = true;

        if( matchR[v] < 0 || bpm( matchR[v] ) )
        {
            matchL[u] = v;
            matchR[v] = u;
            return true;
        }
    }
    return false;
}

int matchaa()
{
    // Read input and populate graph[][]
    // Set m, n

    memset( matchL, -1, sizeof( matchL ) );
    memset( matchR, -1, sizeof( matchR ) );
    int cnt = 0;
    for( int i = 0; i < m; i++ )
    {
        memset( seen, 0, sizeof( seen ) );
        if( bpm( i ) ) cnt++;
    }

    // cnt contains the number of happy pigeons
    // matchL[i] contains the hole of pigeon i or -1 if pigeon i is unhappy
    // matchR[j] contains the pigeon in hole j or -1 if hole j is empty

    return cnt;
}


int stocks[110][30];
int nn, kk;

bool below(int i, int j)
{
    for(int x = 0; x < kk; x++)
    {
        if(stocks[i][x] >= stocks[j][x])
            return false;
    }
    return true;
}

int solve(ifstream &filein)
{


    memset(graph,0,sizeof(graph));


    filein>>nn>>kk;

    m = n = nn;
    for(int i = 0; i < nn; i++)
    {
        for(int j = 0; j < kk; j++)
        filein>>stocks[i][j];
    }

    for(int i = 0; i < nn; i++)
    for(int j = 0; j < nn; j++)
    {
        if(below(i,j))
            graph[i][j] = true;
    }
    return(nn-matchaa());
}


int main()
{
  ifstream filein("input1.txt");
  ofstream fileout("output1.txt");


  int t;
  filein>>t;

  for(int i = 0; i < t; i++)
  {
    int res = solve(filein);

    fileout<<"Case #"<<i+1<<": "<<res<<endl;
    cout<<"Case #"<<i+1<<": "<<res<<endl;
  }



  filein.close();
  fileout.close();

  return 0;
}
