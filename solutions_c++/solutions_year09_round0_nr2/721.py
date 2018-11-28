// Marcin Wrochna
// g++ -O2
// IDE: geany
#include <cstdio>
#include <cstring>
#include <deque>

using namespace std;

typedef pair<int,int> PI;
#define MP make_pair
#define REP(x,n) for(int x=0; x<(int)(n); ++x)
#define PB push_back
#define HH first
#define WW second

int  alt[100][100];
char lab[100][100];
const int dh[4] = {-1,0,0,1};
const int dw[4] = {0,-1,1,0};

int H,W;

PI target(PI from)
{
	if(from.HH<0 || from.HH>=H || from.WW<0 || from.WW>=W) return from;
	PI result=from;
	REP(r,4)
	{
		PI cand = MP(from.HH+dh[r],from.WW+dw[r]);
		if(cand.HH<0 || cand.HH>=H || cand.WW<0 || cand.WW>=W) continue;
		if(alt[cand.HH][cand.WW]<alt[result.HH][result.WW])	result = cand;
	}
	return result;
}

void doit() {	
	scanf("%d %d",&H,&W);
	REP(h,H) REP(w,W) scanf("%d", &alt[h][w]);
	 
	memset(lab, (char)0, sizeof(lab));
	char current = 'a';
	REP(h,H) REP(w,W) if(!lab[h][w])
	{
		deque<PI> Q;
		Q.push_back(MP(h,w));
		lab[h][w]=current;
		while(!Q.empty())
		{
			PI cur = Q.front();
			Q.pop_front();
			PI t = target(cur);
			if(!lab[t.HH][t.WW])
			{
				lab[t.HH][t.WW]=current;
				Q.push_back(t);
			}

			REP(r,4)
			{
				PI cand = MP(cur.HH+dh[r],cur.WW+dw[r]);
				if(target(cand)==cur && !lab[cand.HH][cand.WW])
				{
					lab[cand.HH][cand.WW]=current;
					Q.push_back(cand);
				}
			}
		}
		current++;
	}

	REP(h,H) { REP(w,W) printf("%c ", lab[h][w]); printf("\n"); }
}

int main()
{
	int NCase;
	scanf("%d",&NCase);
	REP(ncase,NCase) {
		printf("Case #%d:\n", ncase+1);
		doit();
	}

	return 0;
}
