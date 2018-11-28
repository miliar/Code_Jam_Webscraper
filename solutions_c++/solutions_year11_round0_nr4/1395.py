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

string problem_name = "D-large";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}


int cnk[1122][1122];
int h[1122][1122];
double dp[1122];
int fact[1122];

double pr(int col, int onplace)
{
	return h[col][onplace]*1.0/fact[col];
}

double go(int col)
{
	if (col<=1) return 0;
	if (dp[col]>-0.1) return dp[col];
	double res= 0 ;

	for (int i=1;i<=col;i++)
		res+=go(col-i)*pr(col,i);
	
	for (int i=1;i<col;i++)
		res=min(res,(go(i)+go(col-i)) );


	return dp[col] = (1 + res)/(1-pr(col,0));
}

int main()
{
	init();

	fact[0]=1;
	for (int i=1;i<=10;i++)
		fact[i]=fact[i-1]*i;

	cnk[0][0]=1;
	for (int i=1;i<=10;i++) {
		cnk[i][0]=1;
		for (int j=1;j<=10;j++)
			cnk[i][j]=cnk[i-1][j]+cnk[i-1][j-1];
	}

	for (int i=0;i<=11;i++)
		dp[i]=-1;
	
	h[0][0]=1;
	for (int i=1;i<=10;i++)
	{
		if (i==1) h[i][0]=0; else
		h[i][0] = (h[i-1][0]+h[i-2][0])*(i-1);
		for (int j=1;j<=i;j++)
			h[i][j] = cnk[i][j]*h[i-j][0];	
	}


	int tst;
	scanf("%d",&tst);
	for (int cas=1;cas<=tst;cas++) {
	
		int n;
		scanf("%d",&n);
		int col=0;
		int a;
		for (int i=1;i<=n;i++) {
			scanf("%d",&a);
			if (a!=i) col++;
		}
	
		printf("Case #%d: %.8lf\n",cas,1.0*col);
	}





	

	return 0;
}

