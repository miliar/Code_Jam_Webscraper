#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

#define nmax 10

map<string,int> num;

struct painter
{
	int c,s,e;
} x[nmax];

bool u[nmax];


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,T,i,j,n,c,k,l,ans;
	string s;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		c=0;
		num.clear();
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			cin>>s>>x[i].s>>x[i].e;
			if (num.find(s)==num.end()) num[s]=c++;
			x[i].c=num[s];
		}
		ans=11;

		for(i=0;i<(1<<n);i++)
		{
			for(j=0;j<c;j++) u[j]=false;
			k=l=0;
			for(j=0;j<n;j++)
				if (i&(1<<j))
				{
					if(!u[x[j].c])
					{
						++k;
						u[x[j].c]=true;
					}
					++l;
				}
			if (l>=ans) continue;
			if (k>3) continue;
			for(j=1;j<=10000;j++)
			{
				for(k=0;k<n;k++)
					if (i&(1<<k))
						if (x[k].s<=j&&x[k].e>=j) break;
				if (k==n) break;
			}
			if (j>10000) ans=l;
		}

		printf("Case #%d: ",t);
		if (ans==11) printf("IMPOSSIBLE\n"); else printf("%d\n",ans);

	}


	return 0;
}
