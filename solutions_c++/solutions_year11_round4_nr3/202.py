/*
 * Author: code6
 * Created Time:  2011/6/4 22:56:58
 * File Name: C.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <ctime>
#include <string>

using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
typedef long long ll;
const double PI=acos(-1.0);
const double eps=1e-11;

const int N = 1000000 + 5000;

vector<int> prime;
bool vis[N];

void getPrime()
{
    int i, j;
    prime.clear();
    for (i = 2; i < N; i++) {
        if (!vis[i]) {
            prime.push_back(i);
        }
        for (j = 0; j < prime.size() && prime[j] * i < N; j++) {
            vis[i * prime[j]] = true;
        }
    }
}

int main() {
    
    freopen("C-large.in", "r", stdin);
    freopen("C.out", "w", stdout);
    
    getPrime();
    
    int t, cas = 0;
    cin >> t;
    while (t--) {
        cas ++;
        
        ll n;
        int i, j;
        cin>>n;
        
        ll ans;
        
        if (n == 1) {
            ans = 0;
        } else {
            ans = 1;
        }
        
        for (i = 0; i < prime.size() && prime[i] <= n; i++) {
            ll tmp = n;
            int ct = 0;
            while (tmp >= prime[i]) {
                ct ++;
                tmp /= prime[i];
            }
            ans +=  ct - 1;
        }
        
        cout<<"Case #"<<cas<<": "<<ans<<endl;
    }
    return 0;
}
