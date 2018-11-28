#include <stdio.h>
#include <sstream>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <memory.h>
#include <queue>
#include <string>
#include <string.h>
#include <cmath>
#include <utility>
#include <bitset>
#include <time.h>
#include <climits>

#define PI 3.1415926535897932384626433832795
#define sqr(x) ((x)*(x))
#define OUT_RT cerr << (float(clock()) / CLOCKS_PER_SEC) << endl

typedef long long LL;
typedef unsigned long long ULL;

using namespace std;


int a[11111];

int main(void){
    freopen("in","r",stdin);
    freopen("out","w",stdout);

    int T;
    scanf("%d\n",&T);
    cout.precision(15);
    cout << fixed;
    for(int _=1;_<=T;_++){
        int n;
        int s = 0;

        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            s += a[i];
        }

        double sss = 0;
        printf("Case #%d:",_);
        for (int i = 0; i < n; i++) {
            double left = a[i];
            double right = a[i] + s;
            for (int it = 0; it < 200; it++) {
                double center = (left + right) / 2;
                
                double sum = 0;
                for (int j = 0; j < n; j++) {
                    if (center > a[j])
                        sum += center - a[j];
                }
                if (sum > s) {
                    right = center;
                } else {
                    left = center;
                }
            }
            cout << " " << (100 * (left - a[i]) / s);
            sss += (100 * (left - a[i]) / s);
        }
//        cerr << _ << endl;
        cerr << sss << endl;
        cout << endl;        
    }

    return 0;
}
