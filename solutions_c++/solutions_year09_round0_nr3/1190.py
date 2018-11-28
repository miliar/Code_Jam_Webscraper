#include <stdio.h>
#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cassert>
#include <string.h>
using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "C-large";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}
string w = "welcome to code jam";
string s;
int dp[510][100];

int go(int ps,int pw)
{
	if (ps>=sz(s)) 
		return pw==sz(w);
	if (dp[ps][pw]!=-1) return dp[ps][pw];
	int res=0;
	if (pw<sz(w))
	{
		if (s[ps]==w[pw]) res+=go(ps+1,pw+1);
		res%=10000;
	}
	res+=go(ps+1,pw);
	res%=10000;

	return dp[ps][pw] = res;
}

char st[555];

int main()
{
   init();



   int cas;
   scanf("%d\n",&cas);
   for (int t=1;t<=cas;t++)
   {
		gets(st);
		s=st;
		memset(dp,-1,sizeof(dp));
		int res=go(0,0);
		printf("Case #%d: %04d\n",t,res);   
   }




   return 0; 
}
