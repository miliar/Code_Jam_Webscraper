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
#include<math.h>
#include<stack>
using namespace std;

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define ABS(X) ((X) < 0 ? (-(X)) : (X))
#define S(X) ((X)*(X))

typedef pair<int,int> PII;
typedef __int64 LL;

//int dr[]={0,-1,-1,-1,0,1,1,1};
//int dc[]={-1,-1,0,1,1,1,0,-1};

struct R
{
	int x1,x2,y1,y2;
}r[102];

int w[2][200][200];

int main()
{
	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
//	freopen("D-small-attempt1.in","r",stdin);freopen("D-small-attempt1.out","w",stdout);
//	freopen("D-small-attempt2.in","r",stdin);freopen("D-small-attempt2.out","w",stdout);
//	freopen("D-large.in","r",stdin);freopen("D-large.out","w",stdout);

	int T,ks;
	int R,i,lx,ly,hx,hy;
	int x,y,k,cnt,d,flag,nd;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		scanf("%d",&R);

		for(i=1;i<=R;i++)
		{
			scanf("%d%d%d%d",&r[i].x1,&r[i].y1,&r[i].x2,&r[i].y2);
			if(i==1) lx=r[i].x1; else lx=MIN(lx,r[i].x1);
			if(i==1) hx=r[i].x2; else hx=MAX(hx,r[i].x2);
			if(i==1) ly=r[i].y1; else ly=MIN(ly,r[i].y1);
			if(i==1) hy=r[i].y2; else hy=MAX(hy,r[i].y2);
		}

		lx=1;
		ly=1;

		for(x=lx-1;x<=hx;x++)
			for(y=ly-1;y<=hy;y++)
				w[0][y][x]=0;

		for(k=1;k<=R;k++)
		{
			for(x=r[k].x1;x<=r[k].x2;x++)
				for(y=r[k].y1;y<=r[k].y2;y++)
					w[0][y][x]=1;
		}

		cnt=0;
		d=0;
		while(1)
		{
/*			for(y=ly;y<=hy;y++)
			{
				for(x=lx;x<=hx;x++)
					printf("%d",w[d][y][x]);
				printf("\n");
			}
			printf("\n\n\n");
*/
			flag=0;
			for(x=lx;x<=hx;x++)
				for(y=ly;y<=hy;y++)
				{
					if(w[d][y][x]) {flag=1; goto end;}
				}

end:

			if(!flag) break;

			cnt++;

			nd=d^1;
			for(x=lx;x<=hx;x++)
				for(y=ly;y<=hy;y++)
				{
					if(w[d][y][x])
					{
						if(w[d][y-1][x]==0 && w[d][y][x-1]==0) w[nd][y][x]=0;
						else w[nd][y][x]=1;
					}
					else
					{
						if(w[d][y-1][x]==1 && w[d][y][x-1]==1) w[nd][y][x]=1;
						else w[nd][y][x]=0;
					}
				}

			d^=1;
			

		}

		printf("Case #%d: %d\n",ks,cnt);
	}

	return 0;
}