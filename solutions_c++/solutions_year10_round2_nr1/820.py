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

const ld EPS = 1e-9;
const int MAXN = 200000;
const int MAXS = 210;

struct st{
	string s;
	int cnt;
	int l[MAXS];

	st(){
		s = "";
		cnt = 0;
	}

	st(string q){
		s = q;
		cnt = 0;
	}
};

st a[MAXN];
char tmp[MAXN];
string s;
string v[MAXN];
int h;

void razbor(string &s){
	h = 0;
	if (s.size() < 2){
		return;
	}

	int i = 1;

	string p = "";
	while (i < int(s.size())){
		if (s[i] == '/'){
			v[h] = p;
			++h;
			p = "";
			++i;
			continue;
		}

		p += s[i];
		++i;
	}

	v[h] = p;
	++h;
}



int main()
{
    freopen("input.txt","rt", stdin);
    freopen("output.txt", "wt", stdout);    

	int tk;
	cin >> tk;

	forn(ii, tk){
		int n, m;
		cin >> n >> m;
		int H = 1;
		a[0] = st("");

		forn(i, n){
			scanf("%s", &tmp);
			s = tmp;
			razbor(s);

			int t1 = 0;

			forn(t2, h){
				int idx = -1;
				forn(j, a[t1].cnt){
					if (a[a[t1].l[j]].s == v[t2]){
						idx = a[t1].l[j];
						break;
					}
				}

				if (idx == -1){
					idx = H;
					a[t1].l[a[t1].cnt] = idx;
					++a[t1].cnt;					
					++H;

					a[idx] = st();
					a[idx].s = v[t2];
				}

				t1 = idx;
			}
		}
		int ans = 0;

		forn(i, m){
			scanf("%s", &tmp);
			s = tmp;
			razbor(s);

			int t1 = 0;

			forn(t2, h){
				int idx = -1;
				forn(j, a[t1].cnt){
					if (a[a[t1].l[j]].s == v[t2]){
						idx = a[t1].l[j];
						break;
					}
				}

				if (idx == -1){
					idx = H;
					a[t1].l[a[t1].cnt] = idx;
					++a[t1].cnt;					
					++H;
					++ans;

					a[idx] = st();
					a[idx].s = v[t2];
				}

				t1 = idx;
			}
		}

		printf("Case #%d: %d\n", ii + 1, ans);
		
	}

          
    return 0;
}

