#include "stdio.h"
#include "string.h"
#define bool int


int N;			// 100
int NA,NB;		// 20-100
int T;			// 5-60
int ans[2];

int trip[2][100][2];

void swap(int &a, int &b)
{
	int c;
	c=a;a=b;b=c;
}


void solve()
{
	ans[0]=ans[1]=0;
	int q[2][100];
	int qn[2];
	int i,j,k,l;
	int finished=0;
	int p[2];
	for (i=0;i<NA;i++)
	{
		for (j=i+1;j<NA;j++ )
		{
			if ((trip[0][i][0]>trip[0][j][0])
			||(trip[0][i][0]==trip[0][j][0]&&trip[0][i][1]>trip[0][j][1]))
			{
				swap(trip[0][i][0],trip[0][j][0]);
				swap(trip[0][i][1],trip[0][j][1]);
			}
		}
	}
	for (i=0;i<NB;i++)
	{
		for (j=i+1;j<NB;j++ )
		{
			if ((trip[1][i][0]>trip[1][j][0])
			||(trip[1][i][0]==trip[1][j][0]&&trip[1][i][1]>trip[1][j][1]))
			{
				swap(trip[1][i][0],trip[1][j][0]);
				swap(trip[1][i][1],trip[1][j][1]);
			}
		}
	}
	p[0]=p[1]=0;
	qn[0]=qn[1]=0;
	int go;		// go from A or B?
	int neednewtrain;
	while (finished<NA+NB)
	{
		if (p[0]==NA) go=1;
		else
		if (p[1]==NB) go=0;
		else
		if (trip[0][p[0]][0]<=trip[1][p[1]][0])
		{
			//A go
			go=0;
		}
		else
		{
			//B go
			go=1;
		}

		// this trip is from trip[go][p[go]][0] to trip[go][p[go]][1]

		neednewtrain=1;

		if (qn[go])
		{
			if (q[go][0]<=trip[go][p[go]][0])
			{
				neednewtrain=0;
				for (k=0;k<qn[go]-1;k++)
				{
					q[go][k]=q[go][k+1];
				}
				qn[go]--;

			}
			else
			{
				neednewtrain=1;
			}
		}
		else
		{
			//we need a new train
			neednewtrain=1;
		}
		if (neednewtrain)
		{
			ans[go]++;
		}

		//put this train at the other station
		q[1-go][qn[1-go]]=trip[go][p[go]][1]+T;
		qn[1-go]++;
		k=qn[1-go]-1;
		while (k>0 && q[1-go][k-1]>q[1-go][k])
		{
			swap(q[1-go][k-1],q[1-go][k]);
			k--;
		}

		p[go]++;
		finished++;
	}

}

int main()
{
//	freopen("B-small-attempt0.in","r",stdin);
//	freopen("B-small-attempt0.out","w",stdout);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&N);
	int i,j;
	int h1,m1,h2,m2;
	for (i=0;i<N;i++)
	{
		scanf("%d",&T);
		scanf("%d %d",&NA,&NB);
		for (j=0;j<NA;j++)
		{
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			//printf("%d:%d %d:%d\n",h1,m1,h2,m2);
			trip[0][j][0]=h1*60+m1;
			trip[0][j][1]=h2*60+m2;
		}
		for (j=0;j<NB;j++)
		{
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			//printf("%d:%d %d:%d\n",h1,m1,h2,m2);
			trip[1][j][0]=h1*60+m1;
			trip[1][j][1]=h2*60+m2;
		}
		solve();
		printf ("Case #%d: %d %d\n",i+1,ans[0],ans[1]);
	}
	return 0;
}
