#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

#define FOR(i,n) for(int i=0;i<n;i++)
#define FOX(i,x) for(int i=0;i<x.size();i++)
#define PB push_back

int memo[600][20];

string A="welcome to code jam";

string inp;

int ret(int a, int b)
{
  if(b<0)
    return 1;
  if(a<0)
    return 0;
  int &res=memo[a][b];
  if(res!=-1)
    return res;
  if(inp[a]==A[b])
    return res=(ret(a-1,b-1) + ret(a-1,b))%10000;
  else
    return res=ret(a-1,b);
}

int main()
{
  int n;
  cin>>n;
  getline(cin,inp);
  FOR(i,n)
    {
      memset(memo,-1,sizeof(memo));
      getline(cin,inp);
      printf("Case #%d: %04d\n",i+1, ret(inp.size()-1,A.size()-1));
    }
  return 0;
}
