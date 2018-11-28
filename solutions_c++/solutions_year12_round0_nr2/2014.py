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
#pragma comment(linker, "/STACK:50000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "B-large";

void init(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
}

int p;
int mas[111];
int calc(int n)
{
	int res=0;
	for (int i=0;i<=10;i++)
	for (int j=0;j<=10;j++) if (abs(i-j)<=2)
	for (int k=0;k<=10;k++) if (abs(i-k)<=2 && abs(j-k)<=2) if (i+j+k==n)
	{
		if (i>=p || j>=p && k>=p)
		{
			if (abs(i-j)==2 || abs(i-k)==2 || abs(j-k)==2) 
				res=max(res,1); else
				res=max(res,2);		
		}
	}
	return res;
}


int main() {

	init();

	

	int tst;
	scanf("%d\n",&tst);

	for (int cas=1;cas<=tst;cas++)
	{
		int n,s;
		scanf("%d %d %d",&n,&s,&p);
		int res=0,res2=0;
		for (int i=0;i<n;i++) {
			scanf("%d",&mas[i]);
			int cur = calc(mas[i]);
			if (cur==2) res++; else
			if (cur==1) res2++;
		}
		res+=min(s,res2);

		printf("Case #%d: %d\n",cas,res);	
	}


	

	

	return 0;
}