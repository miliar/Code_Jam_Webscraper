#include<iostream>
#include<cstdio>
#include<vector>
#include<set>
#include<utility>
using namespace std;

struct ex
{
	vector<int> V;
	int c;
	ex(vector<int> _V,int _c)
	{
		V=_V;
		c=_c;
	}
	bool operator<(const ex &a)const
	{
		return V>a.V;
	}
};
vector<int> deal(vector<int> &V,int n,int k,int &sum)
{
	vector<int> tmp,tmp2;
	int i;
	for(i=0;i<V.size();i++)
	{
		if(sum+V[i]>k)
			break;
		sum+=V[i];
		tmp.push_back(V[i]);		
	}
	for(int j=i;j<V.size();j++)
		tmp2.push_back(V[j]);
	for(int i=0;i<tmp.size();i++)
		tmp2.push_back(tmp[i]);
	return tmp2;
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	long long res;
	int t,r,k,n,a,sum,d=0;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d %d %d",&r,&k,&n);
		res=0;
		vector<int> V,TV;
		vector<long long> all;
		set<ex> S;
		set<ex>::iterator it;
		for(int i=0;i<n;i++)
		{
			scanf("%d",&a);
			V.push_back(a);
		}
		all.push_back(0);
		for(int i=1;i<=r;i++)
		{
			ex tmp(V,i);
			it=S.find(tmp);
			if(it!=S.end())
			{
				int b=(*it).c;
				int e=i-1;
				long long tmp;
				int num,x;
				tmp=all[e]-all[b-1];
				num=r-(i-1);
				x=i-b;
				int e2=num%x;
				long long tmp2=all[b+e2-1]-all[b-1];
				res=res+(long long)(num/x)*tmp+tmp2;
				break;
			}
			sum=0;
			TV=deal(V,n,k,sum);
			S.insert(tmp);
			V=TV;
			res+=sum;
			all.push_back(res);
		}
		printf("Case #%d: %lld\n",++d,res);
	}
	return 0;
}
