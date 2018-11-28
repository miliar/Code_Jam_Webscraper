#include<iostream>
#include<string>
#include<algorithm>
#include<map>
#include<memory>
#include<vector>
#include<set>

using namespace std;

int main() {
    int t, n, m, k, x, y;
    cin >> t;
    for(int c=1; c<=t; c++) {
        cin >> n >> m;
        set<int> v[3001];
        int a[3001]={0};
        bool solved[3001] = {0};
        int sel[3001]={0};
        for(int i=0; i<m; i++) {
            cin >> k;
            for(int j=0; j<k; j++) {
                cin >> x >> y;
                if(y == 0) v[i].insert(x);
                else a[i] = x;
            }
        }
        
        
        bool b=false;
        while(true) {
            for(int i=0; i<m; i++) {
                
                if(not solved[i]) {
                    if(v[i].empty()) {
                        if(a[i] == 0) {
                            goto XXX;
                        }
                        else {
                            sel[a[i]] = 1;
                            for(int j=0; j<m; j++) v[j].erase(a[i]);
                        }
                        solved[i] = true;
                        goto NEXT;
                    }
                }
            }
            
            b = true;
            break;
            NEXT:;
        }
        XXX:;
        
        cout << "Case #" << c << ":";
        if(b) {
            for(int i=1; i<=n; i++) cout << ' ' << sel[i];
            cout << endl;
        }
        else {
            cout << " IMPOSSIBLE\n";
        }
        
    }
}
