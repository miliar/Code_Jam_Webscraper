//Grzegorz Prusak: problem "Welcome to code jam" (Google code jam 2009)
#include <iostream>
#include <iomanip>
#include <cstring>

//debug mode
#define DEBUG_MODE 1
#define DEBUG(i) if((1<<i)&DEBUG_MODE)

//loops
#define REP(i,n)    for(int i=0 ; i<(n); ++i)
#define FOR(i,p,k)  for(int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(int i=(p); i>=(k); --i)

const int n_max = 100	+10;
const int l_max = 500	+10;

const char *p = "\0welcome to code jam";
const int pl = 20;

int main()
{
	int n; std::cin >> n; REP(i,n)
	{
		//input
		char str[l_max]; std::cin >> std::ws; std::cin.getline(str,l_max);
		
		//automata
		int res[pl]={1}; for(char *ptr = str; *ptr; ptr++)
			FORD(j,pl-1,0) if(*ptr==p[j]) res[j] = (res[j]+res[j-1])%10000;
		
		//output
		std::cout.fill('0');
		std::cout << "Case #" << i+1 << ": ";
		std::cout.width(4);
		std::cout << res[pl-1] << "\n";
	}

	return 0;
}

