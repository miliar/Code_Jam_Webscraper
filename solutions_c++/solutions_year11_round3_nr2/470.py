#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#include <queue>
#include <map>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
using namespace std;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef vector<double> vd;
typedef queue<int> qi;

#define fori(i, n) for(i=0;i<n;i++)
#define fordi(i, n) for(int i=0;i<n;i++)
#define INF 0x7fffffff

char sc() {char r; if (scanf("%c", &r) != 1) {printf("-1"); exit(0);} return r;}
int si() {int r; if (scanf("%d", &r) != 1) {printf("-1"); exit(0);} return r;}
long long sli() {long long r; if (scanf("%lld", &r) != 1) {printf("-1"); exit(0);} return r;}
double sf() {double r; if (scanf("%lf", &r) != 1) {printf("-1"); exit(0);} return r;}


int calc(int t, int N, int C, vi &d, vi &boost) {
    double time=0;
    fordi(i,N) {
        int dist = d[i%C];
        if (boost[i]) {
            int bt = max((int)time,t);
            if (t<time)
                time += dist;
            else if(t > time + dist*2)
                time += dist*2;
            else {
                double td = t-time;
                time += td + (dist - td/2);
            }
        } else {
            time += dist*2;
        }
    }
    return (int) time;
}


main() {
    int T=si();
    fordi(ii,T) {
        printf("Case #%d: ",ii+1);
        int L=si(),t=si(),N=si(),C=si();
        vi d;
        d.resize(C);
        fordi(j,C) d[j]=si();
        vi booster;
        booster.resize(N);
        if (L==0)
            printf("%d\n",calc(t,N,C,d,booster));
        else if(L==1) {
            booster[0] = 1;
            int min=calc(t,N,C,d,booster);
            for(int i=1;i<N;i++) {
                int m;
                booster[i-1]=0;
                booster[i]=1;
                m  = calc(t,N,C,d,booster);
                if (m<min) min = m;
            }
            printf("%d\n",min);
        }
        else if(L==2) {
            booster[0] = 1;
            booster[1] = 1;
            int min=calc(t,N,C,d,booster);
            for(int i=2;i<N;i++) {
                for(int j=0;j<i;j++) {
                    fordi(k,N) booster[k]=0;
                booster[i]=1;
                booster[j]=1;
                int m  = calc(t,N,C,d,booster);
                if (m<min) min = m;
                }
            }
            printf("%d\n",min);
        }
    }
}
