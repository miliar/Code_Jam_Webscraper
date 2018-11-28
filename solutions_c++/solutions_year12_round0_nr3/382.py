#include <cstdio>
#include <cstring>
#include <set>
using namespace std;
const int MAXN = 2000010;
int f[MAXN],maxb,a,b;
int x[60],y[60];
bool hash[MAXN];
int check(int num) {
	set <int> s;
	int len = 0, tmp = num,move = 1;
	while(tmp) tmp/=10, len ++,move *= 10;
	int dex = 10;
	move/=10;
	int base = move;
	for(int i = 1;i < len;i ++) {
		int f = num % dex;
		int b = num / dex;
		int now = f*move + b;
		if(now < num && now >= base && now >= a) {
			s.insert(now);
		}
		dex *= 10;move /= 10;
	}
	return (int)s.size();
}
void work() {
	scanf("%d %d",&a,&b);
	f[0] = 0;
	for(int i = 1;i <= b;i ++) 
		f[i] = f[i - 1] + check(i);
	printf("%d\n",f[b] - f[a - 1]);
}
int main() {
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i = 1;i <= T;i ++) { 
		printf("Case #%d: ",i);
		work();
	}
}
