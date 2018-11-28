#pragma comment(linker,"/STACK:256000000")
#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <math.h>
#include <set>
#include <map>
using namespace std;



int main()
{
	//freopen("1.txt","rt",stdin);
	//freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-large.in","rt",stdin);
	//freopen("OutSmallB.txt","wt",stdout);
	freopen("OutLargeB.txt","wt",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		long long c,d;
		cin>>c>>d;
		vector<pair<long double,long long>> p(c);
		for(int j=0;j<c;j++)
			cin>>p[j].first>>p[j].second;
		long double lt=0,rt=1e16;
		long double md=(lt+rt)/2;
		sort(p.begin(),p.end());
		
		for(int k=1;k<500;k++)
		{
			md=(lt+rt)/2;
			vector<pair<long double,long double>> h(c);
			for(int j=0;j<c;j++)
				h[j]=make_pair(p[j].first-md,p[j].first+md);
			long double u=h[0].first;
			int li=0;
			for(int j=0;j<c;j++)
			{
				if(u<h[j].first)
					u=h[j].first;
				u+=long double(d*(p[j].second-1));
				if(u>h[j].second)
				{
					li=1;
					break;
				}
				u+=long double(d);
			}
			if(li==1)
				lt=md;
			else
				rt=md;
		}
		printf("Case #%d: %.12llf\n",i,md);	
	}




	





			



fclose(stdout);
}