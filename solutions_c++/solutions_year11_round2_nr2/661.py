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

string problem_name = "B-large(1)";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}

pair <int,int> mas[2111];


int main()
{
	init();

	int tst;
	scanf("%d",&tst);

	for (int cas=1;cas<=tst;cas++)
	{
		double res=0;
		int c,d;
		scanf("%d%d",&c,&d);
		for (int i=0;i<c;i++)
			scanf("%d%d",&mas[i].first,&mas[i].second);
		sort(mas,mas+c);
		double l=0,r=1e12;
		for (int step=1;step<=100;step++)
		{
			double t = (l+r)/2;
			double left=-(1e12);
			bool ok = 1;
			for (int i=0;i<c;i++)
			{
				//double dst = abs(mas[i].first-left)
				double canleft = (double)mas[i].first - t;
				double canright = (double)mas[i].first + t;
				double fir = max(canleft,left+d);
				double last = fir + (mas[i].second-1)*(double)d;
				if ( (abs(fir-(double)mas[i].first)-(1e-9))>t || (abs(last-(double)mas[i].first)-(1e-9))> t ) ok=0;
				left = last;
			}
			if (ok) r=t; else l=t;		
		}
		 

	
		printf("Case #%d: %.8lf\n",cas,r);
	}






	return 0;
}

