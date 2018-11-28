#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

//#define NDEBUG

#if defined(NDEBUG)
#define DBG_CODE(cb...)
#else
#define DBG_CODE(cb...) cb
#endif

#define WRITE(x) DBG_CODE(cout << x << endl)
#define WATCH(x) DBG_CODE(cout << #x << "=" << x << endl)

//[a, b) incrementando
#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); i++)
//(a, b] decrementando
#define FORR(i, a, b) for(typeof(a) i = (a) - 1; i >= (b) && i < (a) ; i--)

#define ALL(x) x.begin(), x.end()
#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define FOREACHR(i, c) for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)

const int MAX_ELEMENTS = 'Z' - 'A' + 1;

int get_id(char c)
{
	return c - 'A';
}

bool present[MAX_ELEMENTS];
bool combines[MAX_ELEMENTS][MAX_ELEMENTS];
int combination[MAX_ELEMENTS][MAX_ELEMENTS];
bool opposed[MAX_ELEMENTS][MAX_ELEMENTS];

int main()
{
	int NTC;
	scanf("%d", &NTC);
	FORN(TC, 0, NTC){
		memset(present, 0, sizeof(present));
		memset(combines, 0, sizeof(combines));
		memset(opposed, 0, sizeof(opposed));

		int C;
		scanf("%d", &C);
		FORN(i, 0, C){
			char ce1, ce2, ce3; 
			scanf("%*[ \t]%c%c%c", &ce1, &ce2, &ce3);
			int e1 = get_id(ce1);
			int e2 = get_id(ce2);
			int e3 = get_id(ce3);

			combines[e1][e2] = true;
			combines[e2][e1] = true;

			combination[e1][e2] = e3;
			combination[e2][e1] = e3;
		}

		int D;
		scanf("%d", &D);
		FORN(i, 0, D){
			char ce1, ce2;
			scanf("%*[ \t]%c%c", &ce1, &ce2);
			int e1 = get_id(ce1);
			int e2 = get_id(ce2);
			opposed[e1][e2] = true;
			opposed[e2][e1] = true;
		}

		list< int > r;
		int n;
		scanf("%d%*[ \t]", &n);
		FORN(i, 0, n){
			int e = get_id(getchar());

			if(!r.empty() && combines[r.back()][e]){
				int tmp = r.back();
				r.pop_back();
				r.push_back(combination[tmp][e]);
			}else{
				bool cleared = false;
				FOREACH(x, r){
					if(opposed[*x][e]){
						r.clear();
						cleared = true;
						break;
					}
				}

				if(!cleared) r.push_back(e);
			}
		}

		printf("Case #%d: [", TC + 1);
		FOREACH(e, r){
			if(e == r.begin())
				printf("%c", 'A' + *e);
			else
				printf(", %c", 'A' + *e);
		}
		printf("]\n");

	}
}
