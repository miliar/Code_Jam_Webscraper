//Grzegorz Prusak: problem "Alien language" (Google code jam 2009)
#include <iostream>

//debug mode
#define DEBUG_MODE 0
#define DEBUG(i) if((1<<i)&DEBUG_MODE)

//loops
#define REP(i,n)    for(int i=0 ; i<(n); ++i)
#define FOR(i,p,k)  for(int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(int i=(p); i>=(k); --i)

const int E_max = 27	+2;
const int l_max = 15	+2;
const int d_max = 5000	+100;
const int n_max = 500	+10;

typedef int Word[l_max];

int l,d,n;

bool cmp(Word &a, Word &b){ REP(i,l) if(!(a[i]&b[i])) return 0; return 1; }

int main()
{
	//input
	std::cin >> l >> d >> n;
	
	Word A[d_max]; REP(i,d)
	{
		char str[l_max]; std::cin >> str; DEBUG(0) std::cout << "[" << str << "]\n";
		REP(j,l) A[i][j] = 1<<(str[j]-'a');
	}
	DEBUG(0) REP(i,d){ REP(j,l) std::cout << A[i][j] << " "; std::cout << "\n"; }
	
	Word P[n_max]={}; REP(i,n)
	{
		char str[l_max*E_max]; std::cin >> str; DEBUG(0) std::cout << "[" << str << "]\n";
		int pos = 0; REP(j,l)
			if(str[pos++]!='(') P[i][j] = 1<<(str[pos-1]-'a');
			else while(str[pos++]!=')') P[i][j] |= 1<<(str[pos-1]-'a');
	}
	DEBUG(0) REP(i,d){ REP(j,l) std::cout << P[i][j] << " "; std::cout << "\n"; }
	
	//process
	int res[n_max]={};
	REP(i,n) REP(j,d) if(cmp(P[i],A[j])) res[i]++;
	
	//output
	REP(i,n) std::cout << "Case #" << i+1 << ": " << res[i] << "\n";
	
	return 0;
}

