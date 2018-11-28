#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <memory.h>
#include <queue>
#include <string>
#include <string.h>
#include <cmath>
#include <utility>
#include <time.h>


typedef long long LL;
typedef unsigned long long ULL;

#define PI 3.1415926535897932384626433832795
#define sqr(x) ((x)*(x))
#define OUT_RT cerr << (float(clock()) / CLOCKS_PER_SEC) << endl

using namespace std;

int T;
int a[11111],was[11111];
//long double v[1111][1111],f[1111],fact[1111];

int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);

	for(int _=1;_<=T;_++){
		
		int n, cnt = 0;
		cin >> n;
//		memset(was,0,sizeof(was));
		for(int i=1;i<=n;i++){
			cin >> a[i];
			cnt += a[i] != i;
		}
/*		for(int i=1;i<n;i++) if(!was[a[i]]){
			int x = a[i], c = 0;
			while(!was[x]){
				was[x] = 1;
				x = a[x];
				c++;
			}
			ans += f[c];
		}      */

		printf("Case #%d: ",_);
		cout << fixed << double(cnt) << endl;
	}
	return 0;
}
