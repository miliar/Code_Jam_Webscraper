#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <cmath>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

#define SIZE(X) ((int)X.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)

typedef long long LL;
typedef pair<int,int> PII;

template<class T> void out(T A[],int n) {cout<<"{"; for (int i=0;i<n;i++){ cout<<A[i];if (i==n-1) cout<<"}"; else cout<<",";} cout<<endl;}
template<class T> void out(T A[],int n, int m) {for(int i=0;i<n;++i) out(A[i],m);}\
template<class T> void out(vector<T> A,int n=-1) {if (n<0 || n>SIZE(A)) n=SIZE(A);cout<<"{";for (int i=0;i<n;i++) {cout<<A[i];if (i==n-1) cout<<"}"; else cout<<",";} cout<<endl;}

const int MAXN = 1024;
const int INF = 1000000000;

int mask[15], ans, len;
char s[15];

void go(int ind) {
	if (ind == len-1) {
		LL sum = 0, num = s[0]-'0';
		int flag = -1;
		for (int i = 0; i < len-1; ++i) {
			if (mask[i] == 0) {
				num = num * 10 + s[i+1] - '0';
			}
			else if (mask[i] == 1) {
				if (flag == 1) sum += num;
				if (flag == 2) sum -= num;
				if (flag == -1) sum = num;
				flag = 1;
				num = s[i+1] - '0';
			}
			else if (mask[i] == 2) {
				if (flag == 1) sum += num;
				if (flag == 2) sum -= num;
				if (flag == -1) sum = num;
				flag = 2;
				num = s[i+1] - '0';
			}
		}
		if (flag == -1) sum = num;
		if (flag == 1) sum += num;
		if (flag == 2) sum -= num;
		if ( sum%2==0 || sum%3==0 || sum%5==0 || sum%7==0 )
			ans++;
		return;
	}
	for (int i = 0; i < 3; ++i) {
		mask[ind] = i;
		go(ind+1);
	}
}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int N;

	scanf("%d", &N);
	for (int cas = 1; cas <= N; ++cas) {
		scanf("%s", s);
		len = strlen(s);
		ans = 0;
		go(0);
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}

