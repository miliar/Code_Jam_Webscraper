#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional> 
#include <numeric>
using namespace std;
#define foreach(i,v) for(__typeof((v).end()) i=(v).begin();i!=(v).end();++i)
#define rforeach(i,v) for(__typeof((v).rend()) i=(v).rbegin();i!=(v).rend();++i)
#define FOR(i,b,e) for (int i=(b);i<(e);++i)
#define FORE(i,b,e) for (int i=(b);i<=(e);++i)
#define sq(x) ((x)*(x))
typedef long long LL;
 
int main(){
	int c;
	cin >> c;
	FORE(z,1,c){
		int n;
		cin >> n;
		int x[n], y[n], r[n];
		FOR(i,0,n)
			cin >> x[i] >> y[i] >> r[i];
		printf("Case #%d: ", z);
		if (n==1) printf("%d\n",r[0]);
		if (n==2) printf("%d\n",max(r[0],r[1]));
		if (n==3){
		double mini = 1e60;
			FOR(i,0,n){
				FOR(j,0,n){
					if (j==i) continue;
					FOR(k,0,n)
						if (k!=i && k!=j){
							double ans = r[j] + r[k] + sqrt(sq(x[j]-x[k]) + sq(y[j]-y[k]));
							if (ans < mini) mini = ans;
						}
				}
			}
			printf("%.9f\n",mini/2);
		}
	}
	return 0;
}
