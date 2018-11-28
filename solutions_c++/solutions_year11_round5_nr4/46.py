#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
using namespace std;
 
typedef long long LL;
typedef vector<int> vi;
typedef vector< pair<int, int> > vii;
#define MP(x,y) make_pair(x, y)
 
char a[1005];

bool issquare(LL x) {
	LL L = 0, R = (1LL<<30), M, ans;
	while(L<=R) {
		M = (L+R)/2;
		ans = M*M;
		if(ans == x) return true;
		else if(ans<x) L=M+1;
		else R = M-1;
	}
	return false;
}

void printans(LL x) {
	char w[1005];
	int nw=0;
	while(x>0) {
		w[nw++] = x%2+'0';
		x/=2;
	}
	w[nw]=0;
	reverse(w, w+nw);
	printf("%s\n", w);
	fprintf(stderr, "%s\n", w);
}

int main(void) {
    int T, cs;
    scanf("%d", &T);
    for(cs=1;cs<=T;cs++) {
        printf("Case #%d: ", cs);
		fprintf(stderr,"Case #%d: ", cs);
		scanf("%s", a);
		int n = 0;
		int i, j;
		for(i=0;a[i];i++)
			if(a[i]=='?') ++n;
		for(i=0;i<(1<<n);i++) {
			int t = i;
			LL w = 0;
			for(j=0;a[j];j++) {
				if(a[j]=='?') {
					w=w*2+t%2;
					t/=2;
				} else {
					w=w*2+a[j]-'0';
				}
			}
			if(issquare(w)) {
				printans(w);
				break;
			}
		}
    }
    return 0;
}

