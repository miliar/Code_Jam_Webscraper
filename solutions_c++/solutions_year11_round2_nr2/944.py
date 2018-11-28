#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

const double eps = 1e-7;

vector<pair<double,int>> v;

int c;
double d;

bool equal(double a,double b)
{
	return fabs(a-b) < eps;
}

bool judge(double sec)
{
	double prev=v[0].first-sec-d;
	int i,j;

	for(i=0;i<c;i++)
	{
		pair<double,int> &x=v[i];
		for(j=0;j<x.second;j++)
		{
			if(prev<=x.first)
			{
				if(x.first-prev>d)
				{
					prev = max(prev+d,x.first-sec);
				}
				else
				{
					if(x.first+sec-prev + eps<d) return false;
					prev += d;
				}
			}
			else
			{
				if(x.first+sec>prev)
				{
					if(x.first+sec-prev + eps < d) return false;
					prev+=d;
				}
				else return false;
			}
		}
	}
	return true;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	int ca=1;
	scanf("%d",&t);
	while(t--)
	{
		v.clear();
		scanf("%d%lf",&c,&d);
		int sum=0;
		for(int i=0;i<c;i++)
		{
			int a,b;
			scanf("%d%d",&a,&b);
			if(b<=0) continue;
			v.push_back(make_pair((double)a,b));
			sum+=b;
		}
		double left=0,right=d*sum+100,mid=(left+right)/2.0;
		while(right-left>1e-9)
		{
			if(judge(mid)) right=mid;
			else left=mid;
			mid=(left+right)/2.0;
		}
		printf("Case #%d: %.8lf\n",ca++,left);
	}
	return 0;
}