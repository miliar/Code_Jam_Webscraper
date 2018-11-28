#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<algorithm>

using namespace std;

#define MAX 5002

int flag[MAX],ans[MAX],id[MAX];

int main()
{
	int tests,cs=0,i,j,k;

    int x=clock();
    freopen("C:\\C.in","r",stdin);
	freopen("C:\\Csmall2.txt","w",stdout);

	scanf("%d",&tests);

	while(tests--)
	{
		int K,n;

		scanf("%d %d",&K,&n);
		for(i=0;i<n;i++)
			scanf("%d",&id[i]);

		int pos=0;

		memset(flag,0,sizeof(flag));

		for(i=1;i<=K;i++)
		{
           // printf("%d\n",i);
			int tot=0;
			while(1)
			{
				if(!flag[pos]) tot++;
				if(tot>=i) break;
				pos++;
				if(pos==K) pos=0;
			//	pos=(pos+1)%K;
			}
			flag[pos]=1;
			ans[pos]=i;
		}

		printf("Case #%d:",++cs);
		for(i=0;i<n;i++)
			printf(" %d",ans[id[i]-1]);
		printf("\n");

	}

    int y=clock();
    printf("%d\n",y-x);
    
	return 0;
}
