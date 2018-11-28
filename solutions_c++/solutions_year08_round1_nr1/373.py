#include<iostream>
using namespace std;
#define INF 1<<30
#define N 808

class km_n3
{
private:
	static bool km_n3::bfs(int *phalanx,int n, int *a, int *b, bool *flagA,bool *flagB, int *aMate,
		int *bMate,int *slack, int *pre, int &head, int &tail, int *q)
	{
		while(head<tail)
		{
			int v = q[head++], u = v>>1;
			if( v&1 ) // a
			{
				if(bMate[u] == -1)
				{
					agument(aMate,bMate,pre,u); return true;
				}
				else
				{
					flagA[ bMate[u] ] = true;
					q[tail++] = (bMate[u]<<1);
				}
			}
			else // b
			{
				for(int i = 0; i<n; i++)
				{
					if(flagB[i]) continue;
					if(a[u]+b[i] != phalanx[u*n+i])
					{
						int d = a[u]+b[i]-phalanx[u*n+i];
						if(slack[i] > d)
						{
							slack[i] = d; pre[i] = u;
						}
					}
					else
					{
						flagB[i] = true; pre[i] = u;
						q[tail++] = ((i<<1)|1);
					}
				}
			}
		}
		return false;
	}

	static void km_n3::agument(int *aMate, int *bMate, int *pre, int v)
	{
		while(v!=-1)
		{
			int u = aMate[pre[v]];
			bMate[v] = pre[v];
			aMate[pre[v]] = v;
			v = u;
		}
	}


public:
	static int km_n3::km(int *phalanx, int n)
	{
		int *a, *b, *aMate, *bMate ,*slack, *pre ;
		bool *flagA, *flagB;
		int head, tail, *q; //queue

		a = new int[n];
		b = new int[n];
		aMate = new int[n];
		bMate = new int[n];
		slack = new int[n];
		pre = new int[n];
		flagA = new bool[n];
		flagB = new bool[n];
		q = new int[n*n];

		int i,j;
		for(i=0; i<n; i++)
		{
			int maxVal = -INF;
			for(j=0; j<n; j++)
			{
				if(maxVal < phalanx[i*n+j]) maxVal = phalanx[i*n+j];
			}
			a[i] = maxVal;
			b[i] = 0;
		}

		for(i=0; i<n; i++)
		{
			aMate[i] = -1;
			bMate[i] = -1;
		}

		bool agu = true;
		for(int an = 0; an < n; an++)
		{
			if(agu)
			{
				for(i=0; i<n; i++) flagA[i] = false;
				for(i=0; i<n; i++) flagB[i] = false;
				for(i=0; i<n; i++) slack[i] = INF;
				head=tail=0;
				flagA[an] = true;
				q[tail++] = (an<<1);
			}
			if(bfs(phalanx,n,a,b,flagA,flagB,aMate,bMate,slack,pre,head,tail,q))
			{
				agu = true; continue;
			}

			int minD = INF; an--; agu = false;
			for(i=0; i<n; i++)
			{
				if(!flagB[i] && minD > slack[i]) minD = slack[i];
			}
			for(i=0; i<n; i++)
			{
				if(flagA[i]) a[i] -= minD;
				if(flagB[i]) b[i] += minD;
				slack[i] -= minD;
			}
			for(i=0; i<n; i++)
			{
				if(!flagB[i] && slack[i] ==0)
				{
					flagB[i] = true;
					q[tail++] = ((i<<1)|1);
				}
			}
		}

		int res = 0;
		for(i=0; i<n; i++) res += phalanx[i*n+aMate[i]];
		
		delete []a;
		delete []b;
		delete []aMate;
		delete []bMate;
		delete []flagA;
		delete []flagB;

		return res;
	}
};
km_n3 s;
int main()
{
  	int n, *phalanx = new int[N*N];;
	int t,i,j,k,r, a[N], b[N];
	freopen("C:\\Documents and Settings\\v-guozh\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Documents and Settings\\v-guozh\\Desktop\\a.out","w",stdout);

	scanf("%d",&t);
	for(r=0; r<t; r++)
	{
	    scanf("%d",&n);
		//phalanx = new int[n*n];
		for(j=0; j<n; j++) scanf("%d",&a[j]);
		for(j=0; j<n; j++) scanf("%d",&b[j]);
		for(i = 0; i<n; i++)
		{
			k=i*n;
			for(j = 0; j<n; j++)
			{
				phalanx[k+j] = 0-a[i]*b[j];
			}
		}
		printf("Case #%d: %d\n", r+1,-s.km(phalanx,n) );
		//delete []phalanx;
	}
	return 0;
}
