//Grzegorz Prusak: problem "train timetable"
#include <cstdio>
#include <algorithm>

//debug mode
#define DEBUG_MODE 0
#define DEBUG if(DEBUG_MODE)

//loops
#define REP(i,n)   for(register int i=0; i<(n); ++i)
#define FOR(i,p,k) for(register int i=(p); i<=(k); ++i)

//*****************************************************

const int na_max = 110;
const int nb_max = 110;

//*****************************************************

int read_hour()
{
	int res = 0;
	char c; scanf("\n");
	scanf("%c",&c); res = c-'0';
	scanf("%c",&c); res = res*10 + c-'0';
	scanf("%c",&c);
	scanf("%c",&c); res = res* 6 + c-'0';
	scanf("%c",&c); res = res*10 + c-'0';
	return res;
}

class TEvent
{
	public:
		TEvent(){}
		TEvent(bool ns, bool nd, int nh) : s(ns), d(nd), h(nh) {}
		
		bool s,d;
		int h;
};

bool cmp_event(TEvent a, TEvent b){ return a.h==b.h ?  a.d<b.d : a.h<b.h; }

//*****************************************************

int main()
{
	int n; scanf("%d",&n);
	FOR(i,1,n)
	{
		int t; scanf("%d",&t);
		
		//sorting events
		int na,nb; scanf("%d%d",&na,&nb);
		TEvent S[2*na_max + 2*nb_max]; int ss=0;
		REP(j,na)
		{
			S[ss++] = TEvent(0,1,read_hour());	
			S[ss++] = TEvent(1,0,read_hour()+t);
		}
		REP(j,nb)
		{
			S[ss++] = TEvent(1,1,read_hour());	
			S[ss++] = TEvent(0,0,read_hour()+t);
		}
		std::sort(S,S+ss,cmp_event);
		DEBUG REP(j,ss) printf("%c %c %d\n", S[j].s ? 'B' : 'A', S[j].d ? 'D' : 'A', S[j].h);
		
		//simulation
		int an=0,ar=0,bn=0,br=0;
		REP(j,ss)
		{
			if(S[j].s==0)
			{
				if(S[j].d==0) ar++;
				else ar>0 ? ar-- : an++;
			}
			else
			{
				if(S[j].d==0) br++;
				else br>0 ? br-- : bn++;			
			}
		}
		
		//returning result
		printf("Case #%d: %d %d\n",i,an,bn);
	}

	return 0;
}

