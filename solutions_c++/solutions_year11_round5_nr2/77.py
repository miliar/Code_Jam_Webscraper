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
int n, dn;
int a[11111],d[11111],c[11111];

int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		memset(a, 0, sizeof(a));
		memset(d, 0, sizeof(d));
		memset(c, 0, sizeof(c));

		cin >> n;

		for(int i=0;i<n;i++) cin >> a[i];
		sort(a, a + n);

		dn = 0;
		for(int i=0;i<n;i++){
			int mi = -1, mii = (int)1e9;
			for(int j=0;j<dn;j++) if(d[j] + 1 == a[i] && c[j] < mii){
				mii  = c[j];
				mi = j;
			}
			if(mi != -1){
				c[mi]++;
				d[mi] = a[i];
			}else{
				d[dn++] = a[i];
				c[dn-1] = 1;
			}
		}

		int mi = (int)1e9;
		if(n == 0) mi = 0;
		for(int i=0;i<dn;i++) if(c[i] < mi) mi = c[i];
				
		printf("Case #%d: ",_);
		cout << mi << endl;
	}
	return 0;
}
