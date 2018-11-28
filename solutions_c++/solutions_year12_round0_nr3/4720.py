#include <map>
#include <stdio.h>
#include <string.h>

using namespace std;

int x,y;
char h[2000005];
char pr[4000][4000];
int ch = 1;

int count = 0;

inline int cas(int x) {
	if ( x < 10)
		return 10;
	if ( x < 100)
		return 100;
	if ( x < 1000)
		return 1000;
	if ( x < 10000)
		return 10000;
	if ( x < 100000)
		return 100000;
}

inline int isOk(int x) {
	
	int a = 10;
	int ret = 0;
	while (a < x) {
		if ( x % a >= (a / 10)) {
			int newNr = x / a + (x % a) * (cas(x) / a);
			if (h[newNr] == ch) {
				if (pr[newNr][x] != ch && pr[x][newNr] != ch) {
					ret++;
					pr[newNr][x] = ch;
					pr[x][newNr] = ch;
				}
				//printf("(%d %d)\n",newNr,x);
			}
		}
		a *= 10;
	}
	h[x] = ch;
	return ret;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.out","w",stdout);

	int t;
	scanf("%d",&t);

	while (t--) {
		scanf("%d %d",&x,&y);
		
		for (int i = x ; i <= y ; ++i) {
			count += isOk(i);
		}
		printf("Case #%d: %d\n",ch,count);
		ch++;		
		count = 0;
	}

	return 0;
}
