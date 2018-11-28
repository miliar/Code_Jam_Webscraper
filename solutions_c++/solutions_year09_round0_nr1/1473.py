#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <climits>
#include <string>
#include <cstring>
using namespace std;

#define forn(a, n) for(int (a) = 0; (a) < (n); ++(a))
#define forsn(a, s, n) for(int (a) = (s); (a) < (n); ++(a))
#define forall(a, b) for(typeof((b).begin()) (a) = (b).begin(); (a) != (b).end(); ++(a))
#define esta(a, b) (((a) & (1LL<<(b))) != 0)

typedef long long tint;
const int INF = INT_MAX-1000;

int l, d, n, ret, mapa[20][30];
char words[5005][20], buffer[512];

int main()
{
#ifdef TAVO92
	freopen("A-large.in" , "r" , stdin);
	freopen("A-large.out", "w" , stdout);
#endif

	scanf("%i%i%i", &l, &d, &n);
	
	forn(i, d) scanf("%s", words[i]);
	forn(t, n)
	{
		scanf("%s", buffer);
		memset(mapa, 0, sizeof(mapa));
		
		bool abre=false;
		int pos = 0;
		
		forn(j, INF)
		{
			if(buffer[j] == '\0') break;
			else if(buffer[j] == '(')
				abre = true;
			else if(buffer[j] == ')')
			{
				abre = false;
				++pos;
			}
			else
			{
				mapa[pos][buffer[j]-'a'] = 1;
				
				if(!abre)
					++pos;
			}
		}
		
		ret=0;
		
		forn(i, d)
		{
			bool p = true;
			forn(j, l)
				p &= mapa[j][words[i][j]-'a'];
			
			ret += p;
		}
		
		printf("Case #%i: %i\n", t+1, ret);
	}
	
	return 0;
}
