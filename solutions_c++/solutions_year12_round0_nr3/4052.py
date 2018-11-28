#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<cassert>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<sstream>

#define DEBUGLEVEL
#ifdef DEBUGLEVEL
#define printf_debug(fmt, args...) fprintf(stderr, fmt, ##args)
#else
#define printf_debug(fmt, args...)
#endif

typedef long long llong;

using namespace std;

bool is_recycled_pair(int n, int m) {
    stringstream s;
    s << n;
    string str_n = s.str();
    s.str("");
    s << m;
    string str_m = s.str();
    if(str_n.size() == str_m.size()) {
        for(int i = 0; i < str_n.size(); i++) {
            rotate(str_n.begin(), str_n.end() - 1, str_n.end());
            if(str_n == str_m) return true;
        }
    }
    return false;
}

int main() {
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
        int A, B, answer = 0;
        cin >> A >> B;
        for(int n = A; n <= B; n++) {
            for(int m = n + 1; m <= B; m++) {
                answer += is_recycled_pair(n, m);
            }
        }
        cout << "Case #" << t + 1 << ": " << answer << endl;
    }
    is_recycled_pair(124, 451);
    return 0;
}
