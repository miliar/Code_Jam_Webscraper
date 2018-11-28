#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <map>
using namespace std;

#define sz 2000001

bool use[sz];
int acc[sz];


int checknum(int n,int b)
{
  char wd[100];
  for(int i=0;i<100;i++)
    wd[i] = 0;
  int c = 0;
  sprintf(wd,"%d",n);
  int len = strlen(wd);
  map<int,bool> kk;
  for(int i=0;i<len-1;i++)
  {
    wd[ len+i ] = wd[i];
    wd[i] = 0;
    if( wd[i+1]!='0' && atoi(wd+i+1) <= b && atoi(wd+i+1)>n && kk[atoi(wd+i+1)]==NULL)
    {
      //cout << n << " " << atoi(wd+i+1) << endl;
      kk[atoi(wd+i+1)] = true;
      c++;
    }
  }
  return c;
}

int main()
{
  int acn = 0;
  int n;
  int a,b;
  cin >> n;
  for(int i=0;i<n;i++)
  {
    cout << "Case #" << i+1 << ": ";
    cin >> a >> b;
    acn = 0;
    for(int i=a;i<=b;i++)
    {
      acn += checknum(i,b);
    }
    cout << acn << endl;
  }
}
