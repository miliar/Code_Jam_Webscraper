
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

void solve(vector<int> points, int s, int p);

int main(void) {
    int t, n, s, p, sum, pt;
    int i, j;
    vector<int> points;
    
   // freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    
    cin >> t;
    
    for (i = 0; i < t; i++) {
        cin >> n >> s >> p;
        
        for (j = 0; j < n; j++) {
            cin >> pt;
            points.push_back(pt);
        }
        sort(points.begin(), points.end());
        cout << "Case #" << i + 1 << ": ";
        solve(points, s, p);
        cout << endl;
        points.clear();
    }
    
    return 0;
}

void solve(vector<int> points, int s, int p) {
    int aux, a, b, c, best_results = 0;
    int i;
    
    for (i = points.size() - 1; i >= 0; i--) {
        if (points[i]/3 + points[i]%3 < p && s <= 0) break;
        
        a = b = c = points[i]/3;
        
        if (points[i] % 3 == 0) {
            if (a >= p) {
                best_results++;
                continue;
            }
            
            if (s > 0 && a > 0 && a < 10) {
                a++;
                s--;
                if (a >= p) best_results++;
            }
        }
        else {
            a++;
            
            if (a >= p) {
                best_results++;
                continue;
            }
            
            if (a + b + c < points[i]) {
                if (s > 0 && a < 10) {
                    a++;
                    s--;
                    if (a >= p) best_results++;
                }
            }
        }
    }
    
    cout << best_results;
}
