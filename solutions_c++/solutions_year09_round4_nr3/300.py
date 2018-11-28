#include<stdio.h>
#include<vector>
#include<queue>

using namespace std;

int T, n, m;

int a[111][111];
int G[111][111];




#define MAXV 500
struct MF
{
  vector< vector<int> > AL;
  int V, S, T, TF;
  int F[MAXV][MAXV];

  MF(int VV, int SS, int TT) : V(VV), S(SS), T(TT)
  {
    int l1, l2;
    TF = 0; AL.clear(); AL.resize(V);
    for(l1=0;l1<V;l1++) for(l2=0;l2<V;l2++) F[l1][l2] = 0;
  }
  void Add(int t1, int t2, int w)
  {
    if(F[t1][t2] == 0){ AL[t1].push_back(t2); AL[t2].push_back(t1); }
    F[t1][t2] += w;
  }
  int FF()
  {
    int l1, l2, t1, t2;
    vector<int> Check(V);
    vector<int> Back(V, -1);
    queue<int> q;
    q.push(S);
    Check[S] = 0x7fffffff;
    while(!q.empty())
    {
      l1 = q.front();
      if(l1 == T) break;
      q.pop();
      for(l2=0;l2<AL[l1].size();l2++)
        if(F[l1][AL[l1][l2]] && Check[AL[l1][l2]] == 0)
        {
          Check[AL[l1][l2]] = min(F[l1][AL[l1][l2]], Check[l1]);
          Back[AL[l1][l2]] = l1;
          q.push(AL[l1][l2]);
        }
    }
    if(l1 != T) return 0;
    TF += Check[T];
    for(l1=T;l1!=S;l1=Back[l1])
    {
      F[Back[l1]][l1] -= Check[T];
      F[l1][Back[l1]] += Check[T];
    }
    return Check[T];
  }
};

int main(void)
{
	int l0, l1, l2, l3;
	int ret;

	freopen("C2.in","r",stdin);
	freopen("C2.out","w",stdout);


	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d %d",&n,&m);
		for(l1=0;l1<n;l1++) for(l2=0;l2<m;l2++) scanf("%d",&a[l1][l2]);
		ret = 0;

		for(l1=0;l1<n;l1++) for(l2=0;l2<n;l2++ )G[l1][l2] = 0;

		for(l1=0;l1<n;l1++)
		{
			for(l2=0;l2<n;l2++)
			{
				for(l3=0;l3<m;l3++)
				{
					if(a[l1][l3] >= a[l2][l3]) break;
				}
				if(l3 == m)
				{
					G[l1][l2] = 1;
				}
			}
		}


		MF mf(n+n+2, 0, 1);
		for(l1=0;l1<n;l1++)
		{
			mf.Add(0, 2+l1, 1);
			mf.Add(n+2+l1, 1, 1);
		}
		for(l1=0;l1<n;l1++)
		{
			for(l2=0;l2<n;l2++) if(G[l1][l2])
			{
				mf.Add(2+l1, n+2+l2, 1);
			}
		}

		while(mf.FF());

		printf("Case #%d: %d\n",l0,n-mf.TF);
	}
}




/*


#include<stdio.h>

int T, n, m;

int a[111][111];

int inter[111][111];
int solo[(1 << 16) + 1];
int D[(1 << 16) + 1];
int C[(1 << 16) + 1];

int Go(int flag)
{
	if(flag == 0)
	{
		return 0;
	}
	if(solo[flag]) return 1;

	if(C[flag] == 0)
	{
		C[flag] = 1;
		D[flag] = n;
		int subset;
		for(subset = (flag - 1)&flag;subset>0;subset=(subset-1)&flag)
		{
			if(solo[subset])
			{
				int target = 1 + Go(flag ^ subset);
				if(target < D[flag]) D[flag] = target;
			}
		}
	}
	return D[flag];
}

int main(void)
{
	int l0, l1, l2, l3;

	freopen("C1.in","r",stdin);
	freopen("C1.out","w",stdout);


	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d %d",&n,&m);
		for(l1=0;l1<n;l1++) for(l2=0;l2<m;l2++) scanf("%d",&a[l1][l2]);

		for(l1=0;l1<n;l1++) for(l2=0;l2<n;l2++) inter[l1][l2] = 0;
		for(l1=0;l1<(1<<n);l1++) solo[l1] = C[l1] = 0;

		for(l1=0;l1<n;l1++)
		{
			for(l2=l1+1;l2<n;l2++)
			{
				for(l3=0;l3<m;l3++)
				{
					if(a[l1][l3] == a[l2][l3])
					{
						inter[l1][l2] = 1;
						goto maki;
					}
				}

				for(l3=0;l3+1<m;l3++)
				{
					if(a[l1][l3] < a[l2][l3] && a[l1][l3+1] > a[l2][l3+1])
					{
						inter[l1][l2] = 1;
						goto maki;
					}
					if(a[l1][l3] > a[l2][l3] && a[l1][l3+1] < a[l2][l3+1])
					{
						inter[l1][l2] = 1;
						goto maki;
					}
				}


maki: ;
			}
		}



		for(l1=0;l1<(1<<n);l1++)
		{
			int nono = 0;
			for(l2=0;l2<n;l2++)
			{
				if(l1 & (1 << l2))
				{
					for(l3=l2+1;l3<n;l3++)
					{
						if(l1 & (1 << l3))
						{
							if(inter[l2][l3]) goto maki2;
						}
					}
				}
			}
			solo[l1] = 1;
maki2: ;
		}

		printf("Case #%d: %d\n",l0,Go((1<<n)-1));
	}
}

*/