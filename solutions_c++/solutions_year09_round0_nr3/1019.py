#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;
int DP[600][600];
int solve(const string &s,int i,const string &p,int j){return(i|j)<=0?(i|j)+1:(DP[i][j]>=0)?DP[i][j]:DP[i][j]=(solve(s,i-1,p,j)+(s[i-1]==p[j-1])*solve(s,i-1,p,j-1))%10000;}
int main()
{
 int N;
 char c;
 cin>>N;
 string s;
 getline(cin,s);
 for(int C=0;C<N;C++){
  getline(cin,s);
  memset(DP,0xff,sizeof(DP));
  printf( "Case #%d: %04d\n",C+1,solve(s,s.size(),"welcome to code jam",strlen("welcome to code jam")));
 }
 return 0;
}
