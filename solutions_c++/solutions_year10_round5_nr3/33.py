#include <iostream>
#include <set>
#include <stack>
using namespace std;
int ct[4000000];
stack<int> s;
int main() {
    int T; scanf("%d",&T); for (int t=1; t<=T; t++) {
        memset(ct,0,sizeof(ct));
        while (!s.empty()) s.pop();
        printf("Case #%d: ",t);
        int C; scanf("%d",&C);
        int ans = 0;
        for (int i=0; i<C; i++) {
            int P,V; scanf("%d %d",&P,&V);
            P+=2000000;
            /*ans += (V/2)*(V/2+1)*(2*(V/2)+1)/6;
            for (int i=P-V/2; i<=P+V/2; i++) {
                if (i==P && V%2==0) continue;
                ct[i]++;
                if (ct[i]==2) {s.push(i);}
            }*/
            ct[P]+=V;
            if (V>1) s.push(P);
        }
        while (!s.empty()) {
            int next = s.top();
            s.pop();
            int here = ct[next];
            ans += here/2;
            bool was = ct[next-1]>=2;
            ct[next-1] += here/2;            
            if (ct[next-1]>=2 && !was) {s.push(next-1);}

            was = ct[next+1]>=2;
            ct[next+1] += here/2;            
            if (ct[next+1]>=2 && !was) {s.push(next+1);}
            ct[next]=here%2;
        }
        printf("%d\n",ans);
    }
}
