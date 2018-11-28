#include <stdio.h>
#include <string.h>
#include <string>
#include <queue>
#include <algorithm>
#include <math.h>
#include <vector>
#include <utility>
#include <map>
#include <stack>

#define fi first
#define se second
#define mp make_pair
#define ll long long
#define pii pair <int, int>
#define vi vector <int>
#define REP(a,b) for(int a = 0; a < b; ++a)
#define FORU(a,b,c) for(int a = b; a <= c; ++a)
#define FORD(a,b,c) for(int a = b; a >= c; --a)
#define MOD 1000000000
#define MODLL 1000000000LL
#define INF 2123123123
#define pb push_back
using namespace std;

int main()
{
	int n, s, p, temp, T;
	
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	
	scanf("%d", &T);
	
	FORU(tc, 1, T) {
		int surprise = 0, passed = 0, surpas = 0;
		
		scanf("%d %d %d", &n, &s, &p);
		
		REP(i, n) {
			scanf("%d", &temp);
			
			if (temp >= (3*p-4)) {
				if (temp == (3*p-4))
					++surprise;
				else if (temp == (3*p-3)) {
					if (p >= 2)
						++surpas;
				}
				else
					++passed;
			}
		}
		
		printf("Case #%d: %d\n", tc, passed+min(surprise+surpas, s));
	}
	
	return 0;
}
