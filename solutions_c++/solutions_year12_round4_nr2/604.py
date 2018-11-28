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
#include <time.h>
using namespace std;
#pragma comment(linker, "/STACK:50000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "B-large(1)";

void init(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
}

int n,w,l;
pair <double,int> mas[1111];
double rx[1111],ry[1111];

int check(double x, double y, int cur)
{
	if (x<0 || y<0 || x>w || y>l) return 0;
	for (int i=0;i<cur;i++)
	{
		double dst = (rx[i]-x)*(rx[i]-x) + (ry[i]-y)*(ry[i]-y);
		if (dst>1e-9) dst= sqrt(dst);
		if (dst+1e-9<mas[i].first+mas[cur].first) return 0;
	}
	return 1;
}

double resx[1111],resy[1111];

int main() {

	init();

	int tst;

	scanf("%d",&tst);

	for (int cas=1;cas<=tst;cas++)
	{
	
		scanf("%d %d %d",&n,&w,&l);
		
		for (int i=0;i<n;i++)
		{
			mas[i].second=i;
			scanf("%lf",&mas[i].first);
		}
		sort(mas,mas+n);

		reverse(mas,mas+n);

		rx[0]=0;
		ry[0]=0;
		for (int i=1;i<n;i++)
		{
			int ok=0;
			while (!ok)
			{
				for (int j=i-1;j>=0;j--)
				{
					double x= rand()-16000;
					double y= rand()-16000;
					double len = sqrt(x*x+y*y);
					x/=len;
					y/=len;
					x+=1e-9;
					y+=1e-9;
					x = rx[j]+x*(mas[j].first+mas[i].first);
					y = ry[j]+y*(mas[j].first+mas[i].first);
					if (check(x,y,i))
					{
						ok=1;
						rx[i]=x;
						ry[i]=y;
					}
				}			
			}		
		}

		for (int i=0;i<n;i++)
		{
			resx[mas[i].second] = rx[i];
			resy[mas[i].second] = ry[i];
		}

	
	
		printf("Case #%d: ",cas);

		for (int i=0;i<n;i++)
			printf("%.9lf %.9lf ",resx[i],resy[i]);
		printf("\n");
	}


	
	

	return 0;
}