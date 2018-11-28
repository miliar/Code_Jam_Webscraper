#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

#define SIZE(a) ((int)((a).size()))
#define ALL(a) (a).begin(),(a).end()
#define FILL(a) memset(&a,0,sizeof(a))
#define PB push_back
#define MP make_pair
#define FOR(i,a,b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i,a) for (int i = 0; i < (int)(a); ++i)
typedef long long LL;

using namespace std;

int n;
string s[50];
int a[50];

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc;
	scanf("%d",&tc);
	REP(it,tc){
		printf("Case #%d: ", it+1);
		scanf("%d", &n);
		getline(cin, s[0]);
		REP(i,n)
			getline(cin, s[i]);
		FILL(a);
		REP(i,n){
			REP(j,n)
				if (s[i][j] == '1')
					a[i] = j;
		}
		int cnt = 0;
		bool fl = true;
		while (fl){
			fl = false;
			REP(i,n-1){
				if (a[i] > i){
					fl = true;
					int j = i+1;
					while (a[j] > i){
						++j;
					}
					for (int q = j-1; q >= i; --q){
						swap(a[q], a[q+1]);
						++cnt;
					}
				}
			}
		}
		cout << cnt << "\n";
	}
}
