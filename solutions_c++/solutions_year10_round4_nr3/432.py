/*
 * File:   main.cpp
 * Author: tanaeem
 *
 * Created on June 5, 2010, 8:47 PM
 */
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <string.h>
#include <map>
#include <vector>
using namespace std;

int inp[1100][1100];
int tk[1100][1100];
vector<int> psi,psj;
int main()
{
  freopen("C.in", "r", stdin);
  freopen("C1.op", "w", stdout);
  int t;
  scanf("%d", &t);
  for (int cs=1; cs <= t; cs++)
  {
    int sln=0,r, on=0, st=0;
    scanf("%d",&r);
    memset(inp,0,sizeof(inp));
    memset(tk,0,sizeof(tk));
    for (int i=0; i < r; i++)
    {
      int x1,x2,y1,y2;
      scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
      for (int i=x1; i <=x2; i++)
      {
        for(int j=y1;j<=y2;j++)
        {
          if(!inp[i][j])on++;
          inp[i][j]=1;
          
        }
      }
    }
    psi.clear();psj.clear();
    for (int i=1; i < 105; i++)
    {
      for (int j=1; j < 105; j++)
      {
        if(inp[i][j] && !inp[i-1][j] && !inp[i][j-1])
        {
          tk[i][j]=st;
          psi.push_back(i);
          psj.push_back(j);
        }

        if(!inp[i][j] && inp[i-1][j] && inp[i][j-1])
        {
          tk[i][j]=st;
          psi.push_back(i);
          psj.push_back(j);
        }
      }
    }
    while (on)
    {
      st++;
      for (int k=0; k < psi.size(); k++)
      {
        if(inp[psi[k]][psj[k]])on--;
        else on++;
        inp[psi[k]][psj[k]]^=1;
      }
      vector<int> ti=psi;
      vector<int> tj=psj;
      psi.clear();psj.clear();

      for (int k=0; k < ti.size(); k++)
      {
        int i,j;

        i=ti[k];j=tj[k]+1;

        if(tk[i][j]!=st && inp[i][j] && !inp[i-1][j] && !inp[i][j-1])
        {
          tk[i][j]=st;
          psi.push_back(i);
          psj.push_back(j);
        }

        if(tk[i][j]!=st && !inp[i][j] && inp[i-1][j] && inp[i][j-1])
        {
          tk[i][j]=st;
          psi.push_back(i);
          psj.push_back(j);
        }


        i=ti[k]+1;j=tj[k];

        if(tk[i][j]!=st && inp[i][j] && !inp[i-1][j] && !inp[i][j-1])
        {
          tk[i][j]=st;
          psi.push_back(i);
          psj.push_back(j);
        }

        if(tk[i][j]!=st && !inp[i][j] && inp[i-1][j] && inp[i][j-1])
        {
          tk[i][j]=st;
          psi.push_back(i);
          psj.push_back(j);
        }

      }
    }
    sln=st;
    printf("Case #%d: %d\n", cs, sln);
  }

  return (0);
}

