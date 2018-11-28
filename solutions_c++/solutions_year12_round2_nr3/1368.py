#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
using namespace std;

const int N=500;	

int i,j,k,m,n,l;       
long long a[N+10];
int f[10000000];

void dfs(int i)
{
	if (f[i]==0) return;
	cout<<' '<<f[i];
	dfs(i-f[i]);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		scanf("%d", &n);
		a[0]=0;
		for (i=1; i<=n; i++)
		{
			cin>>a[i];
			a[0]+=a[i];
		}
		memset(f,0xff,sizeof(f));
		f[0]=0;
		printf("Case #%d:\n", t);
		for (i=1; i<=n; i++)
			for (j=a[0]; j>=a[i]; j--)
				if (f[j-a[i]]!=-1)
				{
					if (f[j]==-1)
						f[j]=a[i];
					else
					{
						cout<<f[j];
						dfs(j-f[j]);
						cout<<endl;
						
						cout<<a[i];
						dfs(j-a[i]);
						cout<<endl;
						goto label;
					}
				}
label:		
		printf("\n");
	}
	return 0;
}
