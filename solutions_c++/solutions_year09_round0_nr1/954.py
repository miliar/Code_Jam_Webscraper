#include <iostream>
#include <strstream>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <complex>
#include <string>
#include <stack>
#include <cctype>
#include <cassert>
#include <vector>
#include <cmath>
#include <ctime>
#include <cstring>
#include <functional>
#include <cstdlib>
#include <queue>
using namespace std;
#ifdef LOCAL
#define ll __int64
#define OUTLL "%I64d" 
#else
#define ll long long
#define OUTLL "%lld"
#endif
#define trav(it,cont) for(it=(cont).begin(); it!=(cont).end(); ++it)
#define forn(i,n) for(i=0;(i)<(n);++i)
#define MAX(a,b) ((a)<(b)?(b):(a))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define SWAP(a,b) a^=b;b^=a;a^=b
using namespace std;

int len, n, m;
const int LEN = 16;
const int N = 5000;
char text[N][LEN];

int main()
{
#ifdef LOCAL
	freopen("in2.txt", "r", stdin);
#endif
	int i, k, lv;
	
	char strtmp[N];
	char valid[LEN][256];
	scanf("%d%d%d", &len, &n, &m);
	forn(i,n){
		scanf("%s", text[i]);
	}

	freopen("out.txt", "w", stdout);
	forn(i,m){
		scanf("%s", strtmp);
		lv = 0;
		memset(valid,0,(sizeof valid));
		for(k=0; strtmp[k]; k++,lv++){
			if(strtmp[k] == '('){
				k++;
				while(strtmp[k]!=')' ){
					valid[lv][strtmp[k]] = 1;
					k++;
				}
			}else{
				valid[lv][strtmp[k]] = 1;
			}
		}

		int cnt = 0;
		forn(k,n){
			forn(lv,len){
				if ( !valid[lv][text[k][lv]])break;
			}
			if ( lv >= len)cnt++;
		}

		printf("Case #%d: %d\n", i+1, cnt);
	}
	return 0;
}
