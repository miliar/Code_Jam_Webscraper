#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <list>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cstdio>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef long long ll;
#define PB push_back
#define SZ(a) int((a).size())
#define ALL(c) (c).begin(), (c).end()
#define TR(c, i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(ALL(c),x) != (c).end())
#define debug(var) cout<<#var<<"="<<(var)<<endl


int calDis(double* p1, double *p2, int n, int *rd) {
    int sn = 0;
    for(int i = 0; i < n; i++) {
        for(int j = i + 1; j < n; j++) {

            if(sqrt((p1[i] - p1[j]) * (p1[i] - p1[j]) + 
                (p2[i] - p2[j]) * (p2[i] - p2[j])) >= (rd[i] + rd[j])) {

            }
            else {
                sn++;
            }
        }
    }
    return sn;
}

void func()
{
    int data[1001];
    double p1[1001], p2[1001], sp1[10][1001], sp2[10][1001];
    int n;
    int w, h;
    cin >> n;
    cin >> w >> h;
    for(int i = 0; i < n; i++) {
        
        cin >> data[i];
    }
    for(int i = 0; i < n; i++) {
        p1[i] = rand() % w;
        p2[i] = rand() % h;
    }
    
    for(int wn = 0; wn < 10000; wn++) {
        int sn = calDis(p1, p2, n, data);
        
        //debug(sn);
        if(sn == 0) break;
        
        vector<PII> hh;
        for(int i = 0; i < 10; i++) {
            
            for(int j = 0; j < n; j++) {
                if(rand() % 10 > 7) {
                    
                    sp1[i][j] = rand() % w;
                    sp2[i][j] = rand() % h;
                }
                else {
                    sp1[i][j] = p1[j];
                    sp2[i][j] = p2[j];
                }
            }
            hh.push_back(make_pair<int, int>(calDis(sp1[i], sp2[i], n, data), i));
        }
        
        sort(hh.begin(), hh.end());
        for(int i = 0; i < n; i++) {
            
            if(rand() % 2 > 0) {
                p1[i] = sp1[hh[0].second][i];
                p2[i] = sp2[hh[0].second][i];
            }
            else {
                p1[i] = sp1[hh[1].second][i];
                p2[i] = sp2[hh[1].second][i];
            }
        }
    }
    for(int i = 0; i < n; i++) {
        cout << " " << p1[i] << " " << p2[i];
    }
    cout << endl;
}

int main()
{
    int t;
    freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-large.in", "r", stdin);
    freopen("B-out.txt", "w", stdout);
    cin >> t;
    for(int ti = 1; ti <= t; ti++)
    {
        cout << "Case #" << ti << ":";
        func();
    }
}