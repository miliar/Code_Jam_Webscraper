#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <bitset>

using namespace std;

#define LL long long
#define pb push_back
#define r(_x,_a,_b,_c) for(_x _a = _b; _a <= _c; _a++)
#define rm(_x,_a,_b,_c,_m) for(_x _a = _b; _a <= _c; _a+=_m)
#define revr(_x,_a,_b,_c) for(_x _a = _b; _a >= _c; _a--)
#define revrm(_x,_a,_b,_c,_m) for(_x _a = _b; _a >= _c; _a-=_m)
#define eps 1e-3
#define mp make_pair
#define fi first
#define se second
#define INF 100000000

int t;
long a,b;
string as;

int main() {
		scanf("%d",&t);
		r(int,xa,1,t) {
				LL jml = 0;
				scanf("%ld %ld",&a,&b);
				long tmp = b;
				while(tmp > 0) {
						as+='0'+tmp%10;
						tmp/=10;
				}
				reverse(as.begin(),as.end());
				r(long,i,a,b) {
						long tmp = i;
						string s;
						while(tmp>0) {
								s+= '0' + (tmp%10);
								tmp/=10;
						}
						reverse(s.begin(),s.end());
						r(int,j,1,s.size()-1) {
								string sss;
								r(int,k,j,s.size()-1)
										sss += s[k];
								r(int,k,0,j-1)
										sss += s[k];
								if(sss > s && sss <= as && sss[0] != '0') {
										jml++;
								}
						}
				}
				printf("Case #%d: %lld\n",xa,jml);
		}
}
