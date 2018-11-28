#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<cstdlib>
#include<ctime>
#include<map>
#include<vector>
#include<queue>
#include<sstream>
#include<stack>
using namespace std;

#define INF 0x7fffffff
#define EPS 1e-8

typedef long long LL;

void init(int mode,string problem)
{
	string infile="C:\\Users\\LaiLi\\Desktop\\GCJ\\";
	string outfile="C:\\Users\\LaiLi\\Desktop\\GCJ\\";
	if(mode==0)
		return;
	if(mode==1)
	{
		infile+=problem+"-small.in";
		outfile+=problem+"-small.out";
	}
	if(mode==2)
	{
		infile+=problem+"-large.in";
		outfile+=problem+"-large.out";
	}
	freopen(infile.c_str(),"r",stdin);
	freopen(outfile.c_str(),"w",stdout);
}

int a[1000005];
int d[1000005];

string solve()
{
	string ans;

	int i,j;
	int L,N,C;
	LL t,st;

	scanf("%d%I64d%d%d",&L,&t,&N,&C);
	for(i=0;i<C;i++)
		scanf("%d",&a[i]);
	for(i=0;i<N;i++)
		d[i]=a[i%C];
	st=0;
	vector<int> v;
	v.reserve(N);
	for(i=0;i<N;i++)
	{
		if(d[i]*2>t-st)
		{
			d[i]=((d[i]*2)-(t-st))/2;
			st+=t-st;
			for(j=i;j<N;j++)
				v.push_back(d[j]);
			break;
		}
		else
		{
			st+=d[i]*2;
		}
	}
	sort(v.begin(),v.end(),greater<int>());
	for(i=0;i<v.size();i++)
	{
		if(L>0)
		{
			st+=v[i];
			L--;
		}
		else
			st+=v[i]*2;
	}
	char res[1005];
	sprintf(res,"%I64d",st);
	ans=res;

	return ans;
}

int main()
{
	init(2,"B");

	int T,cs;
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++)
	{
		printf("Case #%d: %s\n",cs,solve().data());
		fflush(stdout);
	}
}