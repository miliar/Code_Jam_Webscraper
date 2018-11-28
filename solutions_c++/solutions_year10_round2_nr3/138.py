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

long long m = 100003;
long long dp[555][555];
long long cnk[555][555];
long long go(int n, int pos)
{
	//if (pos<0) return 0;
	if (n==1) return pos==0;
	if (dp[n][pos]!=-1) return dp[n][pos];
	long long res=0;
	for (int i=0;i<n-pos;i++)
	{
		if (pos-i-1<0) break;
		res+=go(pos,pos-i-1)*cnk[n-pos-1][i];
		res%=m;
	}
	return dp[n][pos] = res;
}

int main()
{

	init();

	int tst;
	scanf("%d\n",&tst);
	memset(dp,-1,sizeof(dp));
	cnk[0][0]=1;
	for (int i=1;i<=500;i++)
	{
		cnk[i][0]=1;
		for (int j=1;j<=500;j++) {
			cnk[i][j]=cnk[i-1][j]+cnk[i-1][j-1];
			cnk[i][j]%=m;
		}
	}
	for (int cas=1;cas<=tst;cas++)
	{
		int res=0;
		int n;
		scanf("%d",&n);
		for (int i=1;i<n;i++) {
			res+=go(n,i);
			res%=m;
		}
		
		printf("Case #%d: %d\n",cas,res);
	}
	
	
	

  return 0;
}
