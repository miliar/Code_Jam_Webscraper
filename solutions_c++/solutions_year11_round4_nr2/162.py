//Grzegorz Prusak
#include <cstdio>
#include <algorithm>
#include <cstdlib>

#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FOR(i,p,k)  for(int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(int i=(p); i>=(k); --i)

typedef long long LL;

char A[550][550];

typedef int TAB[550][550];

TAB M,MV[2],V[2];

int r,c,d;

void vert(TAB T)
{ REP(y,c) REP(x,r) T[x][y] += (y?T[x][y-1]:0); }

int sqr(TAB T, int x, int y, int w)
{ return T[x+w-1][y+w-1]-(x?T[x-1][y+w-1]:0)-(y?T[x+w-1][y-1]:0)+(x&&y?T[x-1][y-1]:0); }

int blade(TAB T, int x, int y, int w)
{ return sqr(T,x,y,w)-sqr(T,x,y,1)-sqr(T,x+w-1,y,1)-sqr(T,x+w-1,y+w-1,1)-sqr(T,x,y+w-1,1); }

void log(TAB T)
{
	REP(x,r){ REP(y,c) printf("%3d",T[x][y]); puts(""); }
}

int main()
{
	int Q; scanf("%d",&Q); FOR(q,1,Q)
	{
		scanf("%d%d%d",&r,&c,&d);
		REP(i,r) scanf(" %s",A[i]);
		//REP(i,r) REP(j,c) A[i][j] = rand()%10;
		REP(i,r) REP(j,c) A[i][j] -= '0';		
		REP(y,c) REP(x,r) V[0][x][y] = (x?V[0][x-1][y]:0) + x;
		REP(y,c) REP(x,r) V[1][x][y] = (x?V[1][x-1][y]:0) + y;
		REP(y,c) REP(x,r) M[x][y] = (x?M[x-1][y]:0) + A[x][y];
		REP(y,c) REP(x,r) MV[0][x][y] = (x?MV[0][x-1][y]:0) + A[x][y]*x;
		REP(y,c) REP(x,r) MV[1][x][y] = (x?MV[1][x-1][y]:0) + A[x][y]*y;
  		vert(V[0]);
		vert(V[1]);
		vert(M);
		vert(MV[0]);
		vert(MV[1]);
	
		//log(M);
		int best = 2;

		REP(x,r) REP(y,c)
		{
			int w0 = std::min(r-x,c-y);
			FOR(w,best+1,w0)
			{
				/*if(w==5 && x==1 && y==1)
				{
				printf("x=%d y=%d w=%d\n",x,y,w);
				printf("\n M = %d\n",blade(M,1,1,5));
				printf("\n V[0] = %d\n",blade(V[0],1,1,5));
				printf("\n V[1] = %d\n",blade(V[1],1,1,5));
				printf("\n MV[0] = %d\n",blade(MV[0],1,1,5));
				printf("\n MV[1] = %d\n",blade(MV[1],1,1,5));
				}*/

				LL m = blade(M,x,y,w);
				//printf("cond0 = %d*%lld==%d*%lld\n",blade(V[0],x,y,r),m,blade(MV[0],x,y,r),LL(w*w-4));
				//printf("cond1 = %d*%lld==%d*%lld\n",blade(V[1],x,y,r),m,blade(MV[1],x,y,r),LL(w*w-4));
				
				int s = w*w*(w-1)/2-2*(w-1);
				int a = w*w-4;
				if(
					LL(x*a+s)*m==blade(MV[0],x,y,w)*LL(a) &&
					LL(y*a+s)*m==blade(MV[1],x,y,w)*LL(a)
				) best = w;
			}
		}

		if(best>2) printf("Case #%d: %d\n",q,best); else printf("Case #%d: IMPOSSIBLE\n",q);
	}
	return 0;
}

