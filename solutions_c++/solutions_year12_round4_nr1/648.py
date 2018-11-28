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


int d[10500],l[10500];
int fir[10500];
int reach[10500];


void main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int t;
	scanf("%d",&t);
	for (int T=0;T<t;T++)
	{
		int n;
		scanf("%d",&n);

		for (int i=0;i<=n;i++)
			fir[i]=-1;
		for (int i=0;i<=n;i++)
			reach[i]=0;

		for (int i=0;i<n;i++)
			scanf("%d%d",&d[i],&l[i]);
		scanf("%d",&d[n]);
		l[n]=0;
		reach[0]=d[0];

		for (int i=0;i<=n;i++)
			for (int j=i+1;j<=n;j++)
				if (fir[j]==-1 && d[j]-d[i]<=l[j])
					fir[j]=i;

		for (int i=0;i<n;i++)
			if (reach[i])
				for (int j=i+1;j<=n;j++)
					if (!reach[j])
					{
						if (reach[i]<d[j]-d[i])
							break;
						if (j==n)
						{
							reach[j]=1;
							break;
						}
						{

							if (fir[j]==-1 || fir[j]>i)
								reach[j]=l[j];
							else
								reach[j]=d[j]-d[i];
						}
					}

		printf("Case #%d: ",T+1);
		if (reach[n])
			printf("YES");
		else
			printf("NO");
		printf("\n");

	}

}