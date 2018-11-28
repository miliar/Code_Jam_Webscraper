#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <utility>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int) (n); ++i)
#define fore(i, a, b) for(int i = (int) (a); i < (int) (b); ++i)

#define ll long long
#define ld long double
#define PLL pair <ld, ld>
#define PII pair <int, int>
#define pb push_back

const ld EPS = 1e-9;
const int MAXN = 60;
const int INF = (int)(1e9 + 1e-9);

int t[2];
char tmp[MAXN * 20];
string s;
int a[MAXN][MAXN];
bool b[MAXN][MAXN];
int q[MAXN * 20];
int h = 0;
int last[MAXN];

void up(int &a, int b){
	a = min(a, b);
}

int M(char c){
	return c - 'A' + 1;
}

int main()
{
    freopen("input.txt","rt", stdin);
    freopen("b.out", "wt", stdout);    
	
	int tk;
	cin >> tk;

	forn(ii, tk){
		int t1;
		cin >> t1;

		memset(a, 0, sizeof a);
		memset(b, 0, sizeof b);
		memset(last, 255, sizeof last);

		forn(i, t1){
			scanf("%s", &tmp);
			a[M(tmp[0])][M(tmp[1])] = M(tmp[2]);
			a[M(tmp[1])][M(tmp[0])] = M(tmp[2]);
		}

		cin >> t1;

		forn(i, t1){
			scanf("%s", &tmp);
			b[M(tmp[0])][M(tmp[1])] = 1;
			b[M(tmp[1])][M(tmp[0])] = 1;
		}

		cin >> t1;
		scanf("%s", &tmp);
		s = tmp;

		h = 0;
		forn(i, s.size()){
			int x = M(s[i]);

			if (h == 0){
				q[h] = x;
				++h;				
				continue;
			}

			if (a[q[h - 1]][x]){
				q[h - 1] = a[q[h - 1]][x];
				continue;
			}

			bool f = 0;
			forn(j, h){
				if (b[q[j]][x]){
					h = 0;
					f = 1;
					break;
				}
			}

			if (!f){
				q[h] = x;
				++h;
			}
		}
		printf("Case #%d: ", ii + 1);

		printf("[");
		forn(i, h){
			if (i == 0){
				printf("%c", q[i] + 'A' - 1);
				continue;
			}
			printf(", %c", q[i] + 'A' - 1);
		}
		printf("]\n");
	}

	return 0;
}

