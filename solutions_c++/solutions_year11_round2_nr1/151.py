#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <cctype>
#include <cassert>

using namespace std;

#define pb push_back
#define mp make_pair
#define rep(i,n) for(int i = 0; i < (n); i++)
#define repr(i,b,e) for(int i = (b); i <= (e); i++)
#define INF (1001001001)
#define EPS (1e-15)

#define pr(x) do{cout << (#x) << " = " << (x) << endl;}while(0)
#define pri(x,i) do{cout << (#x) << "[" << i << "] = " << (x[i]) << endl;}while(0)
#define pra(x,n) rep(__i,n) pri(x,__i);
#define prar(x,b,e) repr(__i,b,e) pri(x,__i);

typedef long long llint;
typedef pair<int, int> pint;
typedef vector<int> vint;

int in() {
	int a;
	scanf("%d ", &a);
	return a;
}

struct Team {
	int winlose[256];
	double wp, owp, oowp;
	int win, lose;
};

int main() {
	int T = in();
	rep(tst, T) {
		printf("Case #%d:\n", tst + 1);
		
		Team teams[256];
		
		int N = in();
		rep(i, N) {
			char temp[256];
			gets(temp);
			
			rep(k, N) {
				teams[i].winlose[k] = (temp[k] == '0' ? 0 : temp[k] == '1' ? 1 : -1);
			}
		}
		
		// calc WP
		rep(i, N) {
			teams[i].win = teams[i].lose = 0;
			rep(k, N) {
				if(teams[i].winlose[k] != -1) {
					teams[i].winlose[k] == 0 ? teams[i].lose++ : teams[i].win++;
				}
			}
			teams[i].wp = 1. * teams[i].win / (teams[i].win + teams[i].lose);
		}
		
		// calc OWP
		rep(i, N) {
			double sum = 0;
			int n = 0;
			
			rep(k, N) {
				if(teams[i].winlose[k] == -1) continue;
				
				double afterwp;
				if(teams[k].winlose[i] == 0) {
					afterwp = 1. * teams[k].win / (teams[k].win + teams[k].lose - 1);
				}
				else if(teams[k].winlose[i] == 1) {
					afterwp = 1. * (teams[k].win - 1) / (teams[k].win + teams[k].lose - 1);
				}
				else {
					afterwp = teams[k].wp;
				}
				
				sum += afterwp;
				n++;
			}
			teams[i].owp = sum / n;
		}
		
		// calc OOWP
		rep(i, N) {
			double sum = 0;
			int n = 0;
			rep(k, N) {
				if(teams[i].winlose[k] != -1) {
					sum += teams[k].owp;
					n++;
				}
			}
			
			teams[i].oowp = sum / n;
		}
		
		// calc RPI
		rep(i, N) {
			printf("%.9f\n", 0.25 * teams[i].wp + 0.5 * teams[i].owp + 0.25 * teams[i].oowp);
		}
	}
	return 0;
}
