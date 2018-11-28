// google codejam.cpp : Defines the entry point for the console application.
//

// BEGIN CUT HERE
#include <stdafx.h>
// END CUT HERE
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i=0;i<n;++i)
#define VI vector<int>
#define VII vector<VI>
#define ALL(n) n.begin(),n.end()
#define LL long long
#define SIZE(o) o.size()

int dx4[]={0,0,-1,1};
int dy4[]={-1,1,0,0};

int main(int argc, _TCHAR* argv[])
{
	freopen("in","r",stdin);freopen("out","w",stdout);
	
	
	int testcase;
	scanf("%d",&testcase);
	
	int i,j,k;
	int caseID;
	

	REP(caseID,testcase)
	{
		int N,M;
		scanf("%d%d",&N,&M);
		
		int need=(1<<N)-1;
		M%=1<<N;
		if(M==need)
			printf("Case #%d: %s\n",caseID+1,"ON");
		else 
			printf("Case #%d: %s\n",caseID+1,"OFF");
	}
	
	
	return 0;
}

