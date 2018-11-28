#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
using namespace std;
typedef unsigned long long LLU;
typedef long long LL;
typedef pair<int,int> pii;
#define MP make_pair
const int INF=99999999;
const double PI=3.1415926535897932384626;
const double EPS=1E-11;
bool comp(pii a,pii b)
{
	return a.second<b.second;
}
int main()
{
	freopen("test.in","r",stdin); freopen("test.out","w",stdout);
	int testn;
	scanf("%d",&testn);
	for(int tn=1;tn<=testn;tn++)
	{
		int len,walk,run,time,num;
		scanf("%d%d%d%d%d",&len,&walk,&run,&time,&num);
		vector<pair<pii,int> > segs;
		vector<pii> segs2;
		for(int i=0;i<num;i++)
		{
			int a,b,c;
			scanf("%d%d%d",&a,&b,&c);
			segs.push_back(MP(MP(a,b),c));
		}
		sort(segs.begin(),segs.end());
		int p=0;
		for(int i=0;i<num;i++)
		{
			if(segs[i].first.first>p)
				segs2.push_back(MP(segs[i].first.first-p,0));
			segs2.push_back(MP(segs[i].first.second-segs[i].first.first,segs[i].second));
			p=segs[i].first.second;
		}
		if(len>p)
			segs2.push_back(MP(len-p,0));
		sort(segs2.begin(),segs2.end(),comp);
		
//		for(int i=0;i<segs2.size();i++)
//			printf("%d %d\n",segs2[i].first,segs2[i].second);
		
		double tot=time,s=0;
		for(int i=0;i<segs2.size();i++)
		{
			double t=(double)segs2[i].first/(segs2[i].second+run);
			if(tot>=t)
			{
				s+=t;
				tot-=t;
			}
			else
			{
				t=((double)segs2[i].first-tot*(segs2[i].second+run))/(segs2[i].second+walk);
				s+=t+tot;
				tot=0;
			}
//			printf("%f\n",s);
		}
		printf("Case #%d: %.9f\n",tn,s);
	}
}
