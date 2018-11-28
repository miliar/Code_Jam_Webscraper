#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;
typedef long long LL;
#define oo 55
#define inf 1000000000
int a[oo][oo];
int N;
int Ans;

inline void Readin()
{
	scanf("%d",&N);
	for (int i=2;i<=2*N;++i)
		for (int j=1;j<=N;++j)
			if (i-j<=N && i-j>=1)
				scanf("%d",&a[i-j][j]);
}

inline void Work(int x,int y)
{
	x+=N,y+=N;
	for (int K=max(x,y)+N;K<=6*N;++K)
	{
		int minx=inf,miny=inf,maxx=-inf,maxy=-inf;
		for (int i=1;i<=N;++i)
			for (int j=1;j<=N;++j)
			{
				int I=i+x,J=j+y;
				int I1=J,J1=I;
				int I2=K+1-J,J2=K+1-I;
				int I3=J2,J3=I2;
				
				minx<?=I;
				miny<?=J;
				maxx>?=I;
				maxy>?=J;
				
				if (1<=I1-x && I1-x<=N && 1<=J1-y && J1-y<=N)
				{
					if (a[I1-x][J1-y]!=a[i][j]) goto End;
				}
				else{
					minx<?=I1;
					miny<?=J1;
					maxx>?=I1;
					maxy>?=J1;
				}
				
				I1=I2,J1=J2;
				if (1<=I1-x && I1-x<=N && 1<=J1-y && J1-y<=N)
				{
					if (a[I1-x][J1-y]!=a[i][j]) goto End;
				}
				else{
					minx<?=I1;
					miny<?=J1;
					maxx>?=I1;
					maxy>?=J1;
				}
				
				I1=I3,J1=J3;
				if (1<=I1-x && I1-x<=N && 1<=J1-y && J1-y<=N)
				{
					if (a[I1-x][J1-y]!=a[i][j]) goto End;
				}
				else{
					minx<?=I1;
					miny<?=J1;
					maxx>?=I1;
					maxy>?=J1;
				}
			}
		
		
		if (minx<=maxx && miny<=maxy)
		{
			int T=min(K-maxx,minx-1),F=min(K-maxy,miny-1);
			Ans<?=(K-2*min(T,F))*(K-2*min(T,F));
		}
		
		End:;
	}
}

inline void Solve()
{
	/*puts("");
	for (int i=1;i<=N;++i,puts(""))
		for (int j=1;j<=N;++j)
			printf("%d ",a[i][j]);*/
	Ans=inf;
	for (int i=0;i<=N;++i)
	{
		Work(0,i);
		Work(i,0);
		Work(N,i);
		Work(i,N);
	}
	
	printf("%d\n",Ans-N*N);
}

int main()
{
	//freopen("i.txt","r",stdin);
	
	int Test,Case=0;
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	
	return 0;
}
