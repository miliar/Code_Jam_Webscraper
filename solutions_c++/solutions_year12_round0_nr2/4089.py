#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <stack>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#define INF 1000000
typedef long long ll;
typedef unsigned long long llu;
using namespace std;

int main(void) {
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        int num, sup, border;
        cin >> num >> sup >> border;

        int cnt = 0;
        for(int j = 0; j < num; ++j) {
            int score;
            cin >> score;

            if(score < border) continue;
            else if(score >= (border * 3) - 2) ++cnt;
            else if(score >= (border * 3) - 4 && sup > 0) {
                ++cnt;
                --sup;
            }
        }

        cout << "Case #" << i << ": " << cnt << endl;
    }
    return 0;
}
