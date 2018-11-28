#include <cstdio>
#include <cstdlib>

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define MIN(a,b) ((a)<(b) ? (a):(b))

#define MAX 110

using namespace std;

int orange[MAX][2], blue[MAX][2], T, N;

int solve(int mb, int mo) {
	int b, o, pb, po, t, n;
	bool adv_n, adv_o, adv_b;
	
	b = o = 0; pb = 1, po = 1, t = 0, n = 0;
	while (b < mb || o < mo) {
		adv_n = adv_o = adv_b = false;
		if (orange[o][0] == po && orange[o][1] == n && o < mo)
			adv_n = true, adv_o = true;
		else if (blue[b][0] == pb && blue[b][1] == n && b < mb)
			adv_n = true, adv_b = true;
		if (po < orange[o][0] && o < mo) po++;
		else if (po > orange[o][0] && o < mo) po--;
		if (pb < blue[b][0] && b < mb) pb++;
		else if (pb > blue[b][0] && b < mb) pb--;
		
		if (adv_n) n++;
		if (adv_o) o++;
		if (adv_b) b++;
		t++;
		
	//	printf("@ end of time=%d, po=%d, pb=%d, n=%d\n",t,po,pb,n);
	//	printf("orange: btn=%d on=%d\n", orange[o][0], orange[o][1]);
	//	printf("blue: btn=%d bn=%d\n", blue[b][0], blue[b][1]);
	}
	return t;
}

int main() {
	int v, o, b; char c;
	
	scanf("%d", &T);
	FOR(i,0,T) {
		b = o = 0;
		scanf("%d\n", &N);
		FOR(j,0,N) {
			scanf("%c %d ", &c, &v);
			if (c == 'O')
				orange[o][0] = v, orange[o++][1] = j;
			else blue[b][0] = v, blue[b++][1] = j;
		}
		printf("Case #%d: %d\n", i+1, solve(b, o));
		fflush(stdout);
	}
	return 0;
}