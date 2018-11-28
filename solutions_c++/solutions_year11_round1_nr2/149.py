#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

#define FR(i, n) for (int i=0; i<(n); i++)
#define FOR(i, a, b) for (int i=(a); i<=(b); i++)
#define SZ(a) ((int) a.size())

using namespace std;

int ntest;
int n, m;
string a[11111];
set<string> se[11];
set<string> xet, newxet;
string list;

bool cochua(string st, char ch) {
     FR(i, SZ(st)) if (st[i]==ch) return true;
     return false;
}

void process() {
     cin >> n >> m;
     //cout << n << " " << m << endl;
     
     FOR(i,1,10) se[i].clear();
     FR(i, n) {
           cin >> a[i];
           int le = SZ(a[i]);
           se[le].insert(a[i]);
     }
     FR(u, m) {
           cin >> list;
           int best = -1;
           string bestst;
           FR(i, n) {
                 int cur = 0;
                 string st = a[i];
                 int len = SZ(a[i]);
                 int lsize = SZ(se[len]);
                 int j = 0;
                 xet = se[len];
                 while (SZ(xet)>1) {
                       //list[j]
                       vector<int> occ; occ.clear();
                       FR(k, SZ(st)) if (st[k]==list[j]) occ.push_back(k);
                       if (SZ(occ)==0) cur++;
                       
                       newxet.clear();
                       for (set<string>::iterator it=xet.begin(); it!=xet.end(); it++) {
                           string xau = *it;
                           int cnt = 0;
                           bool ok = true;
                           FR(k, SZ(occ)) if (xau[occ[k]]!=list[j]) {ok = false; break; }
                           if (!ok) continue;
                           FR(k, SZ(xau)) if (xau[k]==list[j]) cnt++;
                           if (cnt==SZ(occ)) newxet.insert(xau);
                       }
                       
                       xet = newxet;
                       if (SZ(xet)==1) break;
                       // how to find next j
                       while (1) {
                             j++; // list[j]
                             bool ok = false;
                             for (set<string>::iterator it=xet.begin(); it!=xet.end(); it++) {
                                 if (cochua(*it, list[j])) {
                                    ok = true;
                                    break;
                                 }
                             }
                             if (ok) break;
                       }
                 }
                 
                 if (cur>best) {
                    best = cur;
                    bestst = a[i];
                    //cout << cur << " " << a[i] << endl;
                 }
           }
           cout << " " << bestst;
     }     
     cout << endl;
}

int main() {
    
    freopen("B-small-attempt0.in", "rt", stdin);
    freopen("b.out", "wt", stdout);
    
    cin >> ntest;
    for (int i=1; i<=ntest; i++) {
        printf("Case #%ld:", i);
        process();           
    }    
    
    return 0;
}
