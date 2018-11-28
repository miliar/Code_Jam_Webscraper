/*
 * Author: code6
 * Created Time:  2011/5/21 9:00:39
 * File Name: A.cpp
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

ll N, D, G;
ll gcd(ll a, ll b) {
    return b ? gcd(b, a % b) : a;
}

int main() {
    //freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    
    int t, cas = 0;
    cin>>t;
    while (t--) {
        cas ++;
        cin>>N>>D>>G;
        ll ba = 100 / gcd(100LL, D);
        
        bool flag = true;
        
        if (D == 0 && G == 0) {
            //nothing
        } else {
            if (D == 0) {
                flag = G < 100;
            } else {
                if (G == 0) {
                    flag = false;
                } else {
                    if (D == 100 && G == 100) {
                        //nothing
                    } else {
                        if (D == 100) {
                            //nothing
                        } else {
                            if (G == 100) {
                                flag = false;
                            } else {
                                flag = ba <= N;
                            }
                        }
                    }
                }
            }
        }
        
        printf("Case #%d: ", cas);
        if (flag) {
            puts("Possible");
        } else {
            puts("Broken");
        }
    }
    return 0;
}

