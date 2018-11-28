#include <vector>
#include <iostream>
#include <map>
#include <functional>
#include <algorithm>
#include <list>
#include <string>
#include <sstream>
#include <bitset>
#include <cmath>
#include <iomanip>
#include <queue>
#include <set>
#include <stack>
#include <cassert>
using namespace std;

#define rep(i, size) \
    for (int i = 0; i < size; ++ i)

#define LL long long

void solve()
{

    int N;
    cin >> N;
    for (int k = 0; k < N; ++ k){
        int vector_n;
        cin >> vector_n;
        vector<int> a;
        vector<int> b;
        int t;
        rep(i, vector_n)
        {
            cin >> t;
            a.push_back(t);
        }
        rep(i, vector_n){
            cin >> t;
            b.push_back(t);
        }

        sort(a.begin(), a.end(), greater<int>());
        sort(b.begin(), b.end(), less<int>());
        
        LL ret = 0;

        rep(i, vector_n){
            ret += a[i] * b[i];
        }
       
        cout << "Case #" << (k+1) << ": " << ret << '\n';
    }
}