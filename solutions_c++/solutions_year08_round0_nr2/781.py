#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

#define pb push_back
#define sz size()
#define mp make_pair
#define ff first
#define ss second
#define INF 0x3f3f3f3f

vector< pair<int,int> > S,P;


void solve(int Cs)
{
	int crA,crB,tA,tB;
	int nA,nB,T;
	int x,y,p,s;

	S.clear();P.clear();

	scanf("%d\n%d %d",&T,&nA,&nB);

	for (int i=1;i<=nA;i++)
	{
		scanf("%d:%d",&x,&y);
		p=x*60+y;
		
		scanf("%d:%d",&x,&y);
		s=x*60+y+T;
		
		P.pb( mp(p,0) );
		S.pb( mp(s,1) );
	}
	
	for (int i=1;i<=nB;i++)
	{
		scanf("%d:%d",&x,&y);
		p=x*60+y;
		
		scanf("%d:%d",&x,&y);
		s=x*60+y+T;
		
		P.pb( mp(p,1) );
		S.pb( mp(s,0) );
	}
	
	tA=tB=crA=crB=0;

	sort(P.begin(),P.end() );
	sort(S.begin(),S.end() );
        P.pb( mp(INF,0) );

	for (x=0,y=0;(x<P.sz-1) || (y<S.sz) ;)
		if (S[y].ff<=P[x].ff)
			{
				if (S[y].ss==0)	crA++;
					else crB++;
				y++;
			}
				else
				{
					if (P[x].ss==0) 
							if (crA==0) tA++;
								else crA--;
						else 
							if (crB==0) tB++;
								else crB--;
				 	x++;
				}
	printf("Case #%d: %d %d\n",Cs,tA,tB);
}

int main()
{
	freopen("train.in","r",stdin);
	freopen("train.out","w",stdout);

	int n;
	scanf("%d",&n);

	for (int i=1;i<=n;i++) solve(i);
	return 0;
}
