#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> p[2];
vector<pair<int, int > > a;
int n;
int ntest, res;
int curpos[2], nextpid[2];

void process() {
     
     res = 0;
     cin >> n;
     p[0].clear();
     p[1].clear();
     a.clear();
     
     for (int i=0; i<n; i++) {
         string robot;
         int pos, id;
         cin >> robot >> pos;  
         if (robot[0]=='O') id = 0;
         else id = 1;         
         p[id].push_back(pos);
         a.push_back(make_pair(id, pos));
     }
     
     curpos[0] = curpos[1] = 1;
     nextpid[0] = nextpid[1] = 0;
     for (int i=0; i<n; i++) {
         int id = a[i].first, pos = a[i].second;
         
         int inc = abs(curpos[id] - pos) + 1;
         curpos[id] = pos;
         nextpid[id]++;
         res += inc;
         
         //cout << id << " " << inc << endl;
         
         if (curpos[1-id]<p[1-id][nextpid[1-id]]) {
           curpos[1-id] += min(inc, abs(p[1-id][nextpid[1-id]] - curpos[1-id]));
         } else {
           curpos[1-id] -= min(inc, abs(p[1-id][nextpid[1-id]] - curpos[1-id]));
         }
     }     
}

int main() {
    
    freopen("A-large.in", "rt", stdin);
    freopen("al.out", "wt", stdout);
    
    cin >> ntest;
    for (int i=1; i<=ntest; i++) {
        process();
        printf("Case #%ld: %ld\n", i, res);
    }    
    
    return 0;
}
