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

int a[10005];
int endat[10005];
int b[10005];

int test(int M) {
	int i, j;
	for(i=1;i<=10001;i++){
		b[i] = a[i];
		endat[i] = 0;
	}
	for(i=1;i<=10000;i++){
		while(b[i]>0){
			if(endat[i]) {
				--b[i];
				--endat[i];
				++endat[i+1];
			} else {
				for(j=0;j<M;j++) {
					if(--b[i+j]<0)
						return 0;
				}
				endat[i+M]++;
			}
		}
	}
	return true;
}

int main(void) {
    int T, cs;
    scanf("%d", &T);
    for(cs=1;cs<=T;cs++) {
        int n, i, j;
		scanf("%d", &n);
		memset(a, 0, sizeof(a));
		memset(endat, 0, sizeof(endat));
		for(i=0;i<n;i++) {
			int x;
			scanf("%d", &x);
			a[x]++;
		}
		printf("Case #%d: ", cs);
		if(n==0) {printf("0\n"); fprintf(stderr, "Case #%d: %d\n", cs, 0); continue;}
		int L = 1, R = n, ans=0, M;
		while(L<=R) {
			M = (L+R)/2;
			if(test(M))
				ans=M, L=M+1;
			else
				R=M-1;
		}
		printf("%d\n", ans);
		fprintf(stderr, "Case #%d: %d\n", cs, ans);
    }
    return 0;
}

