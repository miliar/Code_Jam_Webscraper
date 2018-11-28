#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<map>
#include<iostream>
using namespace std;

int t,n,m;
set<string> dir[105];

int main() {
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&t);
    for (int i=0; i<t; i++) {
        scanf("%d%d",&n,&m);
        for (int j=0; j<105; j++) dir[j].clear();
        string ts,nds;
        for (int j=0; j<n; j++) {
            cin >> ts;
            int cnt=0;
            for (int k=0; k<ts.length(); k++)
                if (ts[k]=='/') cnt++;
            dir[cnt].insert(ts);
            }
        int ret=0;
        for (int j=0; j<m; j++) {
            cin >> ts;
            int ind=0,sla=0;
            nds="";
            while (ind<ts.length()) {
               do {
                  nds+=ts[ind];
                  ind++;
                  } while (ind<ts.length() && ts[ind]!='/');
               sla++;
               if (dir[sla].find(nds)==dir[sla].end()) {
                  dir[sla].insert(nds);
                  ret++;
                  }
               }
            }
        printf("Case #%d: %d\n",i+1,ret);
        }
    
}
