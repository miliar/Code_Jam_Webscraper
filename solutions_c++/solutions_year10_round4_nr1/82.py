#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cctype>

using namespace std;
typedef long long int64;
const int inf = 0x3f3f3f3f;
typedef double real;
const real eps = 1e-6;
typedef pair<int,int> pip;
#define Eo(x) { cerr << #x << " = " << (x) << endl; }

char buf[1 << 20];
char a[128][128];
int n,m;

bool check(char x, int i, int j){
	return (i < 0 || i >= m || j < 0 || j >= m || a[i][j] == ' ' || a[i][j] == x) ;
}

int main(){
	int T; cin >> T;
	for (int  _ = 0; _ < T; _++){
		printf("Case #%d: ",_+1);
		n; cin >> n;
		gets(buf);
		memset(a,' ',sizeof(a));
		for (int i = 0; i < 2*n-1; i++){
			gets(a[i]);
			a[i][strlen(a[i])] = ' ';
		}
		m = 2*n-1;
		int best = inf;
		for (int i = -2; i < m+2; i++){
			for (int j = -2; j < m+2; j++){
				bool ok = true;
				int mx = 0;

				for (int k = 0; k < m && ok; k++){
					int zk = i-(k-i);
					for (int l = 0; l < m; l++) if (a[k][l] != ' '){
						mx = max(mx,abs(k-i)+abs(l-j));

						int zl = j-(l-j);
						if (!check(a[k][l],zk,l) || !check(a[k][l],k,zl)){
							ok = false;
							break;
						}
					}
				}
				if (!ok) continue;
				best = min(best,(mx+1)*(mx+1));
			}
		}
		printf("%d\n",best-n*n);
	}
	return 0;
}

