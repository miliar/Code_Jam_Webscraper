#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;

const double eps=1e-7;
int T;
int w,l,u,g,x,y;
vector< pair<double,double> > L,U;

double gety(double x)
{
	if(x==U.back().first)
		return U.back().second-L.back().second;
	int p,q;
	for(int i=0;i<U.size();i++)
		if(U[i].first>x)
		{
			p=i;
			break;
		}
	for(int i=0;i<L.size();i++)
		if(L[i].first>x)
		{
			q=i;
			break;
		}
	double tmp1=L[q].second-(L[q].first-x)*(L[q].second-L[q-1].second)/(L[q].first-L[q-1].first);
	double tmp2=U[p].second-(U[p].first-x)*(U[p].second-U[p-1].second)/(U[p].first-U[p-1].first);
	return tmp2-tmp1;

}

double calc(double l,double r)
{
	double area=0;
	vector<double> V;
	V.push_back(l);
	V.push_back(r);
	for(int i=0;i<U.size();i++)
		if(l<U[i].first&&U[i].first<r)
			V.push_back(U[i].first);
	for(int i=0;i<L.size();i++)
		if(l<L[i].first&&L[i].first<r)
			V.push_back(L[i].first);
	sort(V.begin(),V.end());
	for(int i=1;i<V.size();i++)
		area+=(V[i]-V[i-1])*(gety(V[i])+gety(V[i-1]))/2;
	return area;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		double area=0;
		L.clear();
		U.clear();
		scanf("%d%d%d%d",&w,&l,&u,&g);
		for(int i=0;i<l;i++)
		{
			scanf("%d%d",&x,&y);
			L.push_back(make_pair(x,y));
		}
		for(int i=0;i<u;i++)
		{
			scanf("%d%d",&x,&y);
			U.push_back(make_pair(x,y));
		}
		printf("Case #%d:\n",test);
/*		int nowl=1;
		int nowu=1;
		double len=U[0].first-L[0].first;
		int last=0;
		vector<pair<int,double> > V;
		V.push_back(make_pair(0,len));
		while(nowl!=l&&nowu!=u)
		{
			if(L[nowl]>U[nowu])
			{
				double tmp=L[nowl].second-(L[nowl].first-U[nowu].first)*(L[nowl].second-L[nowl-1].second)/(L[nowl].first-L[nowl-1].first);
				double y=U[nowu].second-tmp;
				area+=(y+len)*(U[nowu].first-last)/2;
				len=y;
				V.push_back(make_pair(U[nowu].first,y));
				last=U[nowu++].first;
			}
			else
			{
				double tmp=U[nowu].second-(U[nowu].first-L[nowl].first)*(U[nowu].second-U[nowu-1].second)/(U[nowu].first-U[nowu-1].first);
				double y=tmp-L[nowl].second;
				area+=(y+len)*(L[nowl].first-last)/2;
				len=y;
				V.push_back(make_pair(L[nowl].first,y));
				last=L[nowl++].first;
			}
		}*/
		double l=0,r=U[u-1].first;
		area=calc(l,r);
		area/=g;
		for(int i=0;i<g-1;i++)
		{
			double nowl=l;
			while(l+eps<r)
			{
				double mid=(l+r)/2;
				if(calc(nowl,mid)>area)
					r=mid;
				else
					l=mid;
			}
			printf("%f\n",l);
			r=U[u-1].first;
		}
	}
	return 0;
}

