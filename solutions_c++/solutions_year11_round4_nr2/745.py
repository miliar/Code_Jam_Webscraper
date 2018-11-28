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

string problem_name = "B-small-attempt0(4)";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}


char mas[555][555];
int val[555][555];
int r,c;
int calc(int x, int y, int k)
{
	long long sum=0;
	long long sx=0,sy=0;
	for (int i=x;i<x+k;i++)
	for (int j=y;j<y+k;j++)
	{
		if (i==x && j==y) continue;
		if (i==x && j==y+k-1) continue;
		if (i==x+k-1 && j==y) continue;
		if (i==x+k-1 && j==y+k-1) continue;
		sum+=val[i][j];
		sx+=i*val[i][j];
		sy+=j*val[i][j];
	}
	double mx = sx*1.0/sum;
	double my = sy*1.0/sum;
	double needx = x+ (k-1)/2.;
	double needy = y+ (k-1)/2.;
	if (abs(mx-needx)<=1e-9 && abs(my-needy)<=1e-9) return 1;
	return 0;
}


int main()
{
	init();

	int tst;
	scanf("%d",&tst);

	for (int cas=1;cas<=tst;cas++)
	{
		int res=0;


		int d;
		scanf("%d%d%d\n",&r,&c,&d);
		for (int i=0;i<r;i++)
		{
			gets(mas[i]);
			for (int j=0;j<c;j++)
				val[i][j]=d+mas[i][j]-'0';
		}

		for (int cur=10;cur>=3;cur--) {
			int ok=0;
			for (int i=0;i+cur<=r;i++)
			for (int j=0;j+cur<=c;j++)
				if (calc(i,j,cur)) ok=1;
			if (ok)
			{
				res=cur;
				break;
			}
		
		}
		
	
		if (res==0)
		printf("Case #%d: IMPOSSIBLE\n",cas); else
		printf("Case #%d: %d\n",cas,res);
	}




	return 0;
}

