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
using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "b-large";

void init(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
 	freopen((problem_name+".out").c_str(),"wt",stdout);
}


int i,j,k;

int a[1600],b[1600];
pair <pair <int, int> , int > mas[500];


int main()
{
	init();

	int n,na,nb;
	scanf("%d\n",&n);
	int T;
	for (int tt=1;tt<=n;tt++)
	{		
		scanf("%d\n",&T);
		scanf("%d%d\n",&na,&nb);
		
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		int cur=0,h1,m1,h2,m2;
		for (i=0;i<na;i++)
		{
			scanf("%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
			h1=h1*60+m1;
			h2=h2*60+m2;
			mas[cur++] = make_pair(make_pair(h1,h2),1);			
		}
		for (i=0;i<nb;i++)
		{
			scanf("%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
			h1=h1*60+m1;
			h2=h2*60+m2;
			mas[cur++] = make_pair(make_pair(h1,h2),2);			
		}
		int aa=0,bb=0;
		int ra=0,rb=0;
		sort(mas,mas+cur);
		int t=0;
		for (i=0;i<cur;i++)
		{
			while  (mas[i].first.first>t)
			{
				t++;
				aa+=a[t];
				bb+=b[t];
			}
			if (mas[i].second==1)
			{
				if (aa==0)	ra++; else aa--;			
				b[mas[i].first.second+T]++;			
			} else
			{
				if (bb==0)	rb++; else bb--;			
				a[mas[i].first.second+T]++;		
			}		
		}
		printf("Case #%d: %d %d\n",tt,ra,rb);	
	}



		

	return 0;
}
