#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <set>

#define VI vector <int>
#define VVI vector < vector<int> >
#define VS vector <string>
#define rep(i,n) for(int i=0;i<(n);++i)
#define repab(i,a,b) for(int i=(a);i<=(b);++i)
#define PB push_back
#define SORT(v) sort(v.begin(), v.end())

using namespace std;

int ca[1001000];

void licz(void)
{
	int k;
	scanf("%d",&k);
	repab(i,1,k)ca[i]=0;
	int id=1, z;
	repab(q,1,k)
	{
		z=q;
		while(z>0)
		{
			if (ca[id]==0)
				z--;
			if(z>0) id++;
			if (id>k)id=1;
		}
		ca[id]=q;
	}
	int n,di;
	scanf("%d",&n);
	rep(i,n)
	{
		scanf("%d",&di);
		printf("%d ",ca[di]);
	}
	printf("\n");
}

int main(void)
{
	int dd;
	scanf("%d",&dd);
	for(int yy=0;yy<dd;yy++)
	{
		printf("Case #%d: ", yy+1);
		licz();
	}
	return 0;
}
