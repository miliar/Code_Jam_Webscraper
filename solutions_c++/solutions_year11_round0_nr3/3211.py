#include<cstdio>
#include<iostream>
using namespace std;
int n, t;
int Case = 0;
int main() {
	scanf("%d", &n);
	while(n--) {
        ++Case;
		scanf("%d", &t);
        int C[t], m = 1000000, Ssum = 0, Psum = 0;
        for(int i = 0; i < t; ++i) {
            scanf("%d", &C[i]);
            Ssum += C[i];
            Psum ^= C[i];
            m = min(m, C[i]);
        }
        if(Psum != 0) {
            printf("Case #%d: %s\n", Case, "NO");
        } else {
            printf("Case #%d: %d\n", Case, Ssum - m);
        }
	}
	return 0;
}
