#include <vector>
#include <cmath>
#include <queue>
#include <string>
#include <sstream>
#include <fstream>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <cctype>
#include <stack>

using namespace std;

#define fe(i,a,n) for(int i = a, __n = n; i < __n; i++)
#define fi(i,a,n) for(int i = a, __n = n; i <= __n; i++)
#define LL long long
#define ULL unsigned long long
#define VI vector<int>
#define VS vector<string>
#define VD vector<double>
#define SI stack<int>
#define SS stack<string>
#define SD stack<double>
#define ERRO 1e-10
#define INF 1e+99
#define tr(i,s) for(typeof(s.begin()) i = s.begin(); i != s.end(); i++)
#define all(v) v.begin(), v.end()

ULL getSeanSum(VI x) {
    ULL ret = 0;
    fe(i,0,x.size()) {
        ret += x[i];
    }
    return ret;
}

ULL getPatrickSum(VI x) {
    ULL ret = 0;
    fe(i,0,x.size()) {
        ret ^= x[i];
    }
    return ret;
}

int getMin(VI x) {
    int size = x.size();
    if (size > 0) {
        int ret = x[0];
        fe(i,0,size) {
            if (ret > x[i]) {
                ret = x[i];
            }
        }
        return ret;
    } else {
        return -1;
    }
}

int main() {
    int a;
    cin >> a;

    fe(i,0,a) {
        ULL ret;

        int b, c;
        VI x;
        VI patrickArray;
        VI seanArray;

        cin >> b;
        fe(j,0,b) {
            cin >> c;
            x.push_back(c);
        }
        sort(all(x));

        if (getPatrickSum(x) != 0) {
            ret = -1;
        } else {
            ret = getSeanSum(x) - getMin(x);
        }

        if (i != a - 1 && ret != -1)
            cout << "Case #" << i + 1 << ": " << ret << endl;
        else if (i != a - 1 && ret == -1)
            cout << "Case #" << i + 1 << ": " << "NO" << endl;
        else if (ret != -1)
            cout << "Case #" << i + 1 << ": " << ret;
        else
            cout << "Case #" << i + 1 << ": " << "NO";

    }
    return 0;
}
