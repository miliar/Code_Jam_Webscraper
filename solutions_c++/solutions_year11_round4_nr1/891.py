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

string problem_name = "A-large(2)";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}


struct st
{
	int b,e,w;
};

int cmp(st &a,st &b)
{
	return (a.w) <b.w;
}

st mas[1111];

int main()
{
	init();

	int tst;
	scanf("%d",&tst);

	for (int cas=1;cas<=tst;cas++)
	{
		double res=0;
		int x,S,R,N;
		double t;
		scanf("%d%d%d%lf%d",&x,&S,&R,&t,&N);
		int tot=0;
		for (int i=0;i<N;i++) {
			scanf("%d%d%d",&mas[i].b,&mas[i].e,&mas[i].w);
			tot +=mas[i].e-mas[i].b;
		}
		N++;
		mas[N-1].b=0;
		mas[N-1].e=x-tot;
		mas[N-1].w=0;

		sort(mas,mas+N,cmp);

		for (int i=0;i<N;i++)
		{
			double len = mas[i].e-mas[i].b;
			if (t>0)
			{
				double can = t*(double)(R+mas[i].w);
				if (can>=len)
				{
					res+= len*1.0/(R+mas[i].w);
					t -= len*1.0/(R+mas[i].w);
					len=0;					
					
				} else
				{
					len -= t*(double)(R+mas[i].w);
					res+=t;
					t=0;
				}

			/*	int mn = min(len,t);
				t-=mn;
				len-=mn;
				res += mn*1.0/(R+mas[i].w);
				*/
			}
			res += len*1.0/(S+mas[i].w);
		}
	
	
		printf("Case #%d: %.9lf\n",cas,res);
	}




	return 0;
}

