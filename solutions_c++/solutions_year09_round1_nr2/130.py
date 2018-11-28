#include <stdio.h>
#include <algorithm>
#include <set>

using namespace std;

#define MAX 100
#define mp make_pair

typedef pair<int,int> pii;

int d[MAX][MAX]; //distancia 
int ts[MAX][MAX];
int tw[MAX][MAX];
int t0[MAX][MAX];

int di[]={0,1,0,-1},dj[]={1,0,-1,0};

void dijkstraelgv(pii o, int n, int m)
{
	int i,j;
	int ni,nj;
	int t,tc;
	int k;
	int p;
	set<pair<int,pii> > pq;
	for(i=0;i<2*n;++i)
		for(j=0;j<2*m;++j)
			d[i][j]=-1;
	d[o.first][o.second]=0;
	pq.insert(mp(0,o));
	while(!pq.empty())
	{
		i=(*pq.begin()).second.first;
		j=(*pq.begin()).second.second;
		pq.erase(pq.begin());
		for(k=0;k<4;++k)
		{
			ni=i+di[k];
			nj=j+dj[k];
			if(ni>=0 && nj>=0 && ni<2*n && nj<2*m)
			{
				if(i/2==ni/2 && j/2==nj/2)
				{
					if(i!=ni)
						t=d[i][j]-t0[i/2][j/2];
					else
						t=d[i][j]-(t0[i/2][j/2]+ts[i/2][j/2]);
					tc=ts[i/2][j/2]+tw[i/2][j/2];
					t=(t%tc + tc)%tc;
					if(i!=ni)
					{
						if(ts[i/2][j/2]<1)
							continue;
						if(t<ts[i/2][j/2])
							p=1;
						else
							p=tc-t+1;
					}
					else
					{
						if(tw[i/2][j/2]<1)
							continue;
						if(t<tw[i/2][j/2])
							p=1;
						else
							p=tc-t+1;
					}
				}
				else
					p=2;
				if( d[ni][nj]<0 || d[ni][nj]>d[i][j]+p )
				{
					if(d[ni][nj]>0)
						pq.erase(mp(d[ni][nj],mp(ni,nj)));
					d[ni][nj]=d[i][j]+p;
					pq.insert(mp(d[ni][nj],mp(ni,nj)));
				}
			}
		}
	}
}

int main()
{
	int n,m;
	int ncases,ccnt;
	int i,j;
	scanf("%d",&ncases);
	for(ccnt=1;ccnt<=ncases;++ccnt)
	{
		scanf("%d %d",&n,&m);
		for(i=0;i<n;++i)
			for(j=0;j<m;++j)
				scanf("%d %d %d\n",&ts[i][j],&tw[i][j],&t0[i][j]);
		dijkstraelgv(mp(2*n-1,0),n,m);
		printf("Case #%d: %d\n",ccnt,d[0][2*m-1]);
	}
	return 0;
}

