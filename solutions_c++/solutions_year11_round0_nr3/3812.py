#include <cstdio>
#include <algorithm>
using namespace std;

int n, b[20], c[20], ma, t, s1, s2, p1, p2;

void chk(){
	bool f1 = false, f2 = false;
	p1 = p2 = s1 = s2 = 0;

	for(int i=0; i<n; i++){
		if(b[i]==0) {
			f1 = true;
			p1 ^= c[i];
			s1 += c[i];
		} else {
			f2 = true;
			p2 ^= c[i];
			s2 += c[i];
		}
	}
	if(p1 == p2 && f1 && f2)
		ma = max(max(s1, s2), ma);
}

int re(int i){
	if(i==n) chk();
	else {
		b[i]=0;
		re(i+1);
		b[i]=1;
		re(i+1);
	}
}

int main(void){
	scanf("%d", &t);
	for(int k=0; k<t; k++) {
		scanf("%d", &n);
		ma = -1;
		for(int i=0; i<n; i++) scanf("%d", &c[i]);
		re(0);
		printf("Case #%d: ", k+1);
		if(ma == -1) printf("NO\n");
		else printf("%d\n", ma);
	}
	return 0;
}
