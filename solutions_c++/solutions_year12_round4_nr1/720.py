#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
#include <queue>
#include <algorithm>
using namespace std;

const int MAX_VINES=10005;
int n;
int pos[MAX_VINES+1];
int length[MAX_VINES+1];
int swing[MAX_VINES];

bool solve() {
    for (int i = 0 ; i < n+1 ; ++i) {
        swing[i] = -1;
    }
    swing[0] = pos[0];
    for (int i = 0 ; i < n ; ++i) {
        //printf("\n%d:%d+%d ",i,pos[i],swing[i]);
        if (swing[i] < 0) break;
        for (int j = i+1 ; j < n+1 && pos[i]+swing[i] >= pos[j] ; ++j) {
            int s = min(length[j],pos[j]-pos[i]);
            //printf("->%d:%d ",j,s);
            swing[j] = max(swing[j],s);
        }
    }
    return swing[n] >= 0;
}

void read() {
	scanf("%d",&n);
    for (int i = 0 ; i < n ; ++i) {
    	scanf("%d %d",&pos[i],&length[i]);
    	//printf("%d: %d %d\n",i,pos[i],length[i]);
    }
	scanf("%d",&pos[n]);
}

int main() {
	int n;
	scanf("%d",&n);
	for (int i = 0 ; i < n ; ++i) {
		read();
		bool s = solve();
		printf("Case #%d: %s\n",i+1,s ? "YES" : "NO");
	}
}

