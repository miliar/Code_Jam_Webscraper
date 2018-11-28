#include <iostream>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <queue>

using namespace std;


int k[2500];
int hi[2500];
int h[2500];
int d[2500];
vector <int> q[2500];

void main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);


	int t;
	scanf ("%d",&t);
	for (int T=0;T<t;T++)
	{
		int n;
		scanf("%d",&n);
		for (int i=0;i<n;i++)
			q[i].clear();
		for (int i=0;i<n-1;i++)
		{
			scanf("%d",&hi[i]);
			hi[i]--;
			q[hi[i]].push_back(i);
		}
		

		h[n-1]=100000000;
		d[n-1]=1;
		for (int i=n-1;i>-1;i--)
		{
			int D;
			if (q[i].size())
				D=(i-q[i][0])*d[i];
			for (int j=0;j<q[i].size();j++)
			{
				h[q[i][j]]=h[i]-D;
				d[q[i][j]]=D+1;
			}
		}

		printf("Case #%d: ",T+1);
		
		bool bo=true;
		for (int i=0;i<n-1;i++)
		{
			int maxi=i+1;
			int maxh=h[i+1];
			for (int j=i+2;j<n;j++)
				if ((maxh-h[i])*(j-i) < (h[j]-h[i])*(maxi-i))
				{
					maxi=j;
					maxh=h[j];
				}
			if (maxi!=hi[i])
			{
				bo=false;
				printf("Impossible");
				break;
			}
		}
		if (bo)
			for (int i=0;i<n;i++)
				printf("%d ",h[i]);
		printf("\n");


	}

}