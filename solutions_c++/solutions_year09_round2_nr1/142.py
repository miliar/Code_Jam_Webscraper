#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <fstream>
#include <cassert>
#include <memory.h>

using namespace std;

int t,a,l;

char s[1000][1000];

char x[1000];
string res;
char tt[101];
int gn=1,n;
double wat[1000];
string name[1000];
int lft[1000];
int rght[1000];

int make(string ans)
{
	int b=0,e=ans.size()-1;
	for (;ans[b]!='(';b++);
	for (;ans[e]!=')';e--);
	int v=0,g=b+1;
	for (;(ans[g]<'0'||ans[g]>'9')&&ans[g]!='.';g++);
	for (;(ans[g]>='0'&&ans[g]<='9')||ans[g]=='.';g++)
		tt[v++]=ans[g];
	tt[v]=0;
	double pp=0;
	sscanf(tt,"%lf",&pp);
	int gon=gn++;
	wat[gon]=pp;
	lft[gon]=-1;
	rght[gon]=-1;
	name[gon]="";
	int tak=-1;
	for (int h=g;h<e;h++)
		if (ans[h]>='a'&&ans[h]<='z'&&tak==-1)
			tak=h;
	string vall="";
	int ot=tak;
	if (tak!=-1)
	{
		for (int h=tak;h<e&&ans[h]>='a'&&ans[h]<='z';h++)
			ot++;
		vall=ans.substr(tak,ot-tak);
		name[gon]=vall;
		int ded=ot;
		int pull=0;
		for (int ff=ot;ff<e;ff++)
		{
			if (ans[ff]=='(')
			{
				pull++;
				if (!pull)
				{
					lft[gon]=make(ans.substr(ot,ff+1-ot));
					rght[gon]=make(ans.substr(ff+1,e-ff-1));
					return gon;
				}
			}
			else if (ans[ff]==')')
			{
				pull--;
				if (!pull)
				{
					lft[gon]=make(ans.substr(ot,ff+1-ot));
					rght[gon]=make(ans.substr(ff+1,e-ff-1));
					return gon;
				}
			}
		}
	}
	return gon;
}


int main()
{
	freopen("out.txt","r",stdin);
	freopen("nut.txt","w",stdout);
	scanf("%d",&t);
	for (int cas=1;cas<=t;cas++)
	{
		gn=1;
		res="";
		scanf("%d",&l);
		gets(x);
		for (int i=0;i<l;i++)
		{
			gets(x);
			res=res+string(x);
		}
		make(res);
		scanf("%d",&a);
		printf("Case #%d:\n",cas);
		for (int i=0;i<a;i++)
		{
			set< string > ss;
			scanf("%s %d",x,&n);
			for (int j=0;j<n;j++)
			{
				scanf("%s",s[j]);
				ss.insert(string(s[j]));
			}
			double p=1;
			int pos=1;
			for (;1;)
			{
				p*=wat[pos];
				if (name[pos].size())
				{
					if (ss.find(name[pos])!=ss.end())
						pos=lft[pos];
					else
						pos=rght[pos];
				}
				else
					break;
			}
			printf("%.7lf\n",p);
		}
	}
	return 0;
}