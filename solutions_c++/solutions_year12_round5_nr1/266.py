#include<iostream>
#include<cstdio>
#include<vector>
#include<utility>
#include<cmath>
#include<algorithm>

using namespace std;

const double eps = 1e-6;

struct node
{
	double v;
	int idx;
	bool operator <(const node& n2) const
	{
		return fabs(v-n2.v)<eps?idx<n2.idx:v>n2.v;
	}
};

int n;
int L[1000];
double P[1000];

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>L[i];
		for(int i=0;i<n;i++)
			cin>>P[i];

		vector<int> g;
		vector<node> d;
		for(int i=0;i<n;i++)
		{
			if (P[i]==0)
				g.push_back(i);
			else
			{
				node nn;
				nn.idx = i;
				nn.v = L[i]/((100-P[i])/100);
				d.push_back(nn);
			}
		}
		sort(d.begin(),d.end());
		printf("Case #%d:",tt);
		for(int i=0;i<d.size();i++)
			printf(" %d",d[i].idx);
		for(int i=0;i<g.size();i++)
			printf(" %d",g[i]);
		printf("\n");
	}
	return 0;
}
