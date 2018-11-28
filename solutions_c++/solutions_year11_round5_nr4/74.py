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

string s,ans;
int l;

int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		
		int n = 0;
		cin >> s;
		l = s.length();		
		for(int i=0;i<l;i++) if(s[i] == '?') n++;
		ans = s;

		printf("Case #%d: ",_);
		for(int i=0;i<(1<<n);i++){
			LL ss = 0;
			int m = i, c;
			for(int j=0;j<l;j++){
				if(s[j] == '1')
					c = 1;else
				if(s[j] == '0')
					c = 0;else{
						c = m & 1;
						ans[j] = c + 48;
						m >>= 1;
					}
				ss = ss + ss + c;
			}
			LL t = (LL)(sqrt(ss) + 0.1);
			if(  t * t == ss){
				cout << ans << endl;
				break;
			}
		}
		
	}
	return 0;
}
