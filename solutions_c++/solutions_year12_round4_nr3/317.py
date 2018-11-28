#include<stdio.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<utility>
#include<iostream>
#include<algorithm>
#include<queue>
#include<string>
#include<map>
#include<ctype.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef vector<int> vi;
int H[20000],G[20000],n,E;
int check() {
    int i,j;
    for (i=1; i<n; i++) {
        for (j=i+1; j<=n; j++) {
            if ((H[G[i]]-H[i]) * (j-i) < (H[j]-H[i]) * (G[i]-i))
                return G[i];
            if ((H[G[i]]-H[i]) * (j-i) == (H[j]-H[i]) * (G[i]-i)) {
                //printf("%d %d\n", j, G[i]);
                if (j < G[i]) return G[i];
            }
        }
    }
    return -1;
}
int main () {
    int i, j, m, TC=1,ans,tem,k,N;
    scanf("%d", &N);
    while (N--) {
        scanf("%d", &n);
        for (i=1; i<n; i++) scanf("%d", &G[i]);
        memset(H, 0, sizeof(H));
        for (i=0; i<100000; i++) {
            int x = check();
            if (x==-1) break;
            //printf("%d\n", x);
            //getchar();
            H[x] += 10;
        }
        printf("Case #%d:", TC++);
        if (i == 100000) printf(" Impossible\n");
        else {for (i=1; i<=n; i++) printf(" %d", H[i]);
        puts("");}
    }
    return 0;
}
