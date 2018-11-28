#pragma warning ( disable : 4786 )

#include <iostream>
#include <sstream>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>

#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
using namespace std;

//#define _rep( i, a, b, x ) for( __typeof(b) i = ( a ); i <= ( b ); i += x )
#define _rep( i, a, b, x ) for( i = ( a ); i <= ( b ); i += x )
#define rep( i, n ) _rep( i, 0, n - 1, 1 )

#define ff first
#define ss second

#define pii pair< int, int >
#define psi pair< string, int >

#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define set(p) memset(p, -1, sizeof(p))
#define clr(p) memset(p, 0, sizeof(p))

//typedef long long i64;
//typedef __int64 i64;
typedef long double ld;

//const double pi = (2.0*acos(0.0));
const double pi = acos(-1.0);
const double eps = 1e-9;
const int inf = (1<<28);
const int MAX = 1000005;

int a, b, len;
int flg[10];
int ans;
char str[10];
int pow10[10];
map< pii, bool > M;

void calPow10() {
	int i, j, k;
	pow10[0] = 1;
	for(i=1; i<10; i++) pow10[i] = pow10[i-1] * 10; 
}

void countPair(int num) {
	int tmp, i, j, k;
	char tmpS[10], ch;
	k = num;
	sprintf(tmpS, "%d", num);

	for(i=0; i<len; i++) {
		if(tmpS[0] == '0') {
			for(j=1; tmpS[j]; j++) {
				tmpS[j-1] = tmpS[j];
			}
			tmpS[j-1] = '0';
			tmpS[j] = '\0';
			continue;
		}
		sscanf(tmpS, "%d", &k);
		//tmp = k / (pow10[len-1]);
		//k = k % (pow10[len-1]);
		//k = (k*10) + tmp;

		//if(!tmp) continue;
		//printf("->%d\n", k);
		ch = tmpS[0];
		for(j=1; tmpS[j]; j++) {
			tmpS[j-1] = tmpS[j];
		}
		tmpS[j-1] = ch;
		tmpS[j] = '\0';

		if(k<a || k>b) continue;
		if((M[pii(num, k)]==true) || (M[pii(k, num)]==true)) continue;
		if(num == k) continue;
		//if(num != k) ans += 2;
		//else ans += 1;
		ans += 1;
		M[pii(num, k)] = true;
		M[pii(k, num)] = true;
		//printf("->%d : %d\n", num, k);
		//M[pii(k, num)] = true;
	}
}

void func(int num, int pos) {
	int i, j, k;
	if(pos == len) {
		if(num<a || num>b) return;
		countPair(num);
		return;
	}
	for(i=0; i<10; i++) {
		if(!pos && !i) continue;
		num = (num*10) + i;
		func(num, pos+1);
		num /= 10;
	}
}

int main() {
	freopen("C-small-attempt0.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int i, j, k;
	int test, t = 0, kase=0;

	calPow10();
	scanf("%d", &test);
	while(test--) {
		scanf("%d %d", &a, &b);
		ans = 0;
		sprintf(str, "%d", a);
		len = strlen(str);
		M.clear();
		func(0, 0);
		printf("Case #%d: %d\n", ++t, ans);
	}
	return 0;
}
