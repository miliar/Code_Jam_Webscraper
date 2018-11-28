#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <set>

using namespace std;

int N,A,B;

int main() {
    set<string> s;
    string a,b;
    int T,i,j,cas=1,ans;

    scanf("%d", &T);
    while(T--) {
        scanf("%d%d", &A, &B);
        for(i=0; i<A; i++) {
            cin >> a;
            for(j=1; j<a.size(); j++) {
                if(a[j] == '/')
                    s.insert(a.substr(0, j));
            }
            s.insert(a.substr(0, a.size()));
        }
        ans = 0;
        for(i=0; i<B; i++) {
            cin >> b;
            for(j=1; j<b.size(); j++) {
                if(b[j] == '/') {
            //        cout << b.substr(0, j) << endl;
                    if((s.insert(b.substr(0, j))).second)
                        ans++;
                }
            }
            if((s.insert(b.substr(0,b.size()))).second)
                ans++;
        }
        printf("Case #%d: %d\n", cas++, ans);
        s.clear();
    }
    return 0;
}
            
