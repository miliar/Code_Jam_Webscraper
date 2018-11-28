#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;

typedef __int64 ll;

const int MAXN = 500;
char str[MAXN];
int num[MAXN];
int val[MAXN];

ll convert(){
	int cnt = 1, f = 1;
	memset(val, -1, sizeof(val));
	val[str[0]] = 1;
	int len = strlen(str);
	for(int i = 0; i < len; ++i){
		if(val[str[i]] != -1){
			num[i] = val[str[i]];
		}else if(f){
			val[str[i]] = 0;
			num[i] = 0;
			f = 0;
		}else {
			val[str[i]] = ++cnt;
			num[i] = cnt;
		}
	}
	ll b = cnt+1, c = 1;
	ll ret = 0;
	for(int i = len-1; i >= 0; --i){
		ret = ret+num[i]*c;
		c *= b;
	}
	return ret;
}

int main()
{
	int T;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t){
		scanf("%s", str);
		ll ret = convert();
		printf("Case #%d: %I64d\n", t, ret);
	}
	return 0;
}


