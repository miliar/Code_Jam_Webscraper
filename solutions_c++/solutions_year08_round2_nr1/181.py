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

typedef __int64 LL;

LL x[100005],y[100005];

int cnt[4][4];

int main()
{
	int tests,cs=0,i,j,k;

	freopen("C:\\Alarge.txt","w",stdout);

	scanf("%d",&tests);

	while(tests--)
	{
		int n;
		LL A,B,C,D,x0,y0,M;

		scanf("%d %I64d %I64d %I64d %I64d %I64d %I64d %I64d",&n,&A,&B,&C,&D,&x0,&y0
			,&M);

		x[0]= x0, y[0]= y0;

		for(i=1;i<n;i++)
		{
			x[i]=((LL)A*x[i-1]+B)%M;
			y[i]=((LL)C*y[i-1]+D)%M;
			//printf("%I64d %I64d\n",x[i],y[i]);
		}

		memset(cnt,0,sizeof(cnt));

		LL ans=0;

		for(i=0;i<n;i++)
			cnt[x[i]%3][y[i]%3]++;

		int x1,x2,y1,y2,y3,x3;

		for(x1=0;x1<3;x1++)
			for(y1=0;y1<3;y1++) for(x2=0;x2<3;x2++)
			for(y2=0;y2<3;y2++) for(x3=0;x3<3;x3++)
			for(y3=0;y3<3;y3++)
			{
				if((x1+x2+x3)%3 || (y1+y2+y3)%3) continue;
				
				LL a=cnt[x1][y1],b=cnt[x2][y2],c=cnt[x3][y3];

				if(x1==x2 && y1==y2) --b;
				if(x1==x3 && y1==y3) --c;
				if(x2==x3 && y2==y3) --c;

				if(a<=0 || b<=0 || c<=0) continue;

				ans+=(LL)a*b*c;
			}


		printf("Case #%d: %I64d\n",++cs,ans/6);


	}

	return 0;
}