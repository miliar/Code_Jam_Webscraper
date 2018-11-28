#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int n,m,v,re;
int nin[10001][2],nro[10001];
int dp[10001][2];

int slv(int trn,int dsr)
{
    if (dp[trn][dsr]!=-1) return dp[trn][dsr];
    int tmp=100000;
    if (trn<=(m-1)/2)
    {
    if (nin[trn][1])
    {
       if (dsr)
       {
          if (nin[trn][0]==1) 
          {
              tmp=min(tmp,slv(2*trn,1)+slv(2*trn+1,1));
              tmp=min(tmp,slv(2*trn,0)+slv(2*trn+1,1)+1);
              tmp=min(tmp,slv(2*trn,1)+slv(2*trn+1,0)+1);
          }
          else
          {
              tmp=min(tmp,slv(2*trn,1)+slv(2*trn+1,1));
              tmp=min(tmp,slv(2*trn,0)+slv(2*trn+1,1));
              tmp=min(tmp,slv(2*trn,1)+slv(2*trn+1,0));
          }
       }
       else
       {
          if (nin[trn][0]==1) 
          {
              tmp=min(tmp,slv(2*trn,1)+slv(2*trn+1,0));
              tmp=min(tmp,slv(2*trn,0)+slv(2*trn+1,1));
              tmp=min(tmp,slv(2*trn,0)+slv(2*trn+1,0));
          }
          else
          {
              tmp=min(tmp,slv(2*trn,0)+slv(2*trn+1,0));
              tmp=min(tmp,slv(2*trn,0)+slv(2*trn+1,1)+1);
              tmp=min(tmp,slv(2*trn,1)+slv(2*trn+1,0)+1);
          }
       }
    }
    else
    {
        if (dsr)
        {
          if (nin[trn][0]==1) 
          {
              tmp=min(tmp,slv(2*trn,1)+slv(2*trn+1,1));
          }
          else
          {
              tmp=min(tmp,slv(2*trn,1)+slv(2*trn+1,1));
              tmp=min(tmp,slv(2*trn,0)+slv(2*trn+1,1));
              tmp=min(tmp,slv(2*trn,1)+slv(2*trn+1,0));
          }  
        }
        else
        {
          if (nin[trn][0]==1) 
          {
              tmp=min(tmp,slv(2*trn,1)+slv(2*trn+1,0));
              tmp=min(tmp,slv(2*trn,0)+slv(2*trn+1,1));
              tmp=min(tmp,slv(2*trn,0)+slv(2*trn+1,0));
          }
          else
          {
              tmp=min(tmp,slv(2*trn,0)+slv(2*trn+1,0));
          }
        }
    }
    }
    else
    {
        //cout << trn << " " << nro[trn-(m-1)/2] << " ";
        if (nro[trn-(m-1)/2]==dsr) return dp[trn][dsr]=0;
        else return dp[trn][dsr]=15000;
    }
    return dp[trn][dsr]=tmp;
}

int main()
{
    fstream fin("A-large.in",ifstream::in);
    fstream fout("A-large.out",ofstream::out);
    fin >> n;
    for(int j=1;j<=n;j++)
    {
        fin >> m >> v;
        rep(i,(m-1)/2) fin >> nin[i+1][0] >> nin[i+1][1];
        rep(i,(m+1)/2) fin >> nro[i+1];
        rep(i,m+1) dp[i][0]=dp[i][1]=-1;
        re=slv(1,v);
        if (re<=10000) fout << "Case #" << j << ": " << re << "\n";
        else fout << "Case #" << j << ": IMPOSSIBLE\n";
    }
    fin.close();
    fout.close();
    system("PAUSE");
    return 0;
}
