#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <queue>
#define MAX 10009
using namespace std;

int f[MAX][4],n,cas,i,j,k,t1,t2,m,v;


void find(int nd)
{
	if (f[nd][0]!=-1 && f[nd][1]!=-1)
	{
		return ;
	}

	int ls = nd+nd, rs = nd+nd+1;

	find(ls);find(rs);

	if (f[nd][2]==1)  //and gate
	{
		// 1
		if (f[ls][1]<MAX && f[rs][1]<MAX)
			t1 = f[ls][1] + f[rs][1]; else t1 = MAX;
	
		if (f[nd][3] == 1)
		{
			t2 = f[ls][1];
			if (f[rs][1]<t2) t2 = f[rs][1];
			if (t2+1<t1) t1 = t2+1;
		}

		f[nd][1] = t1;

		//0
		t1 = f[ls][0];
		if (f[rs][0]<t1) t1 = f[rs][0];
		f[nd][0] = t1;
	}

	if (f[nd][2]==0)  //or gate
	{
		// 0
		if (f[ls][0]<MAX && f[rs][0]<MAX)
			t1 = f[ls][0] + f[rs][0]; else t1 = MAX;
	
		if (f[nd][3] == 1)
		{
			t2 = f[ls][0];
			if (f[rs][0]<t2) t2 = f[rs][0];
			if (t2+1<t1) t1 = t2+1;
		}

		f[nd][0] = t1;

		//1
		t1 = f[ls][1];
		if (f[rs][1]<t1) t1 = f[rs][1];
		f[nd][1] = t1;
	}
	return ;

}

int main()
{
	scanf("%d",&n);

	for (cas = 1; cas<=n ;cas++ )
	{
		scanf("%d%d",&m,&v);
		memset(f,-1,sizeof(f));
		k=(m-1)/2;
		for (i=1;i<=k ;i++ )
		{
			scanf("%d%d",&f[i][2],&f[i][3]);
		}
		for (i=k+1;i<=m ;i++ )
		{
			scanf("%d",&t1);
			f[i][t1]=0;
			f[i][1-t1]=MAX;
		}
		find(1);
		
		//for (i=1;i<=m ;i++ )printf("f[%d]  0=%d  1=%d\n",i,f[i][0],f[i][1]);
		printf("Case #%d: ",cas);
		if (f[1][v] == MAX)
		{
			printf("IMPOSSIBLE\n");
		}
		else printf("%d\n",f[1][v]);
	}
	return 0;
}
