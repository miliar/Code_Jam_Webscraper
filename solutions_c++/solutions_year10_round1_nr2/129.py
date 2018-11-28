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

const int maxn = 256;
int a[maxn];
int b[maxn][256];

int main(){
	int T; cin >> T;
	for (int  _ = 0; _ < T; _++){
		int d,i,m,n; cin >> d >> i >> m >> n;
		for (int i = 0; i < n; i++){
			cin >> a[i];
		}
		memset(b,0x3f,sizeof(b));
		for (int k = 0; k < n; k++){
			for (int j= 0; j < 256; j++){
				assert(b[k][j] >= 0);
				for (int  l = j+1; l < 256; l++){
					int y = m ? (i*(((l-j-1+m)/m)))+b[k][j] : inf;
					int rr = min(y,l-j+b[k][j]);
					if (rr < b[k][l])
						b[k][l] = rr;
				}
				for (int l = j-1; l >= 0; l--){
					int y = m ? (i*((j-l-1+m)/m))+b[k][j] : inf;
					int rr = min(y,j-l+b[k][j]);
					if (rr < b[k][l])
						b[k][l] = rr;
				}
				assert(b[k][j] >= 0);
			}
			b[k+1][a[k]] = min(b[k][a[k]],b[k+1][a[k]]);
			b[k+1][a[k]] = min(d*k,b[k+1][a[k]]);
			for (int j = 0; j < 256; j++) if (j != a[k]){
				int& t = b[k+1][j];
				t = min(t,k*d+min(d+i,abs(a[k]-j)));
				assert(t >= 0);
			}
			for (int j = 0; j < 256; j++){
				int& t = b[k+1][j];
				t = min(t,b[k][j]+d);
				assert(t >= 0);
			}
			for (int j = 0; j < 256; j++){
				int& t = b[k+1][j];
				int ztre = min(abs(a[k]-j),d+i);
				for (int l = 0; l < 256; l++) if (abs(l-j) <= m){
					t = min(t,b[k][l]+ztre);
				}
				assert(t >= 0);
			}
		}
		int res = d*n;
		for (int j = 0; j < 256; j++){
			res = min(res,b[n][j]);
		}
//		for (int  j = 0; j <= n; j++){ for (int k = 0 ;  k < 60; k++){ printf("%d ",b[j][k]); } puts(""); }
		printf("Case #%d: %d\n",_+1,res);
	}
	return 0;
}

