/*
 * Author: code6
 * Created Time:  2011/5/7 22:54:44
 * File Name: B.cpp
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

string toStr(char c1 ,char c2)
{
    if (c1 > c2) swap(c1, c2);
    string ret = "";
    ret += c1;
    ret += c2;
    return ret;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int t, cas = 0;
    cin >> t;
    while ( t-- ) {
        cas ++;
        map<string, char> MP, MR;
        int c, d, n;
        int i, j;
        char c1, c2, c3;
        cin >> c;
        for (i = 0; i < c; i++) {
            cin>>c1>>c2>>c3;
            MP[toStr(c1, c2)] = c3;
        }
        
        cin >> d;
        for (i = 0; i < d; i++) {
            cin>>c1>>c2;
            MR[toStr(c1, c2)] = c1;
        }
        
        cin >> n;
        
        string str, ans;
        cin >> str;
        
        
        ans = "";
        for (i = 0; i < str.size(); i++) {
            ans += str[i];
            
            int l = ans.size();
            if (ans.size() <= 1) {
                continue;
            }
            
            c1 = ans[l - 1];
            c2 = ans[l - 2];
            
            if (MP.find(toStr(c1, c2)) != MP.end()) {
                c3 = MP[toStr(c1, c2)];
                ans[l - 2] = c3;
                ans = ans.substr(0, l - 1);
            } else {
                for (j = 0; j < l - 1; j ++) {
                    c2 = ans[j];
                    if (MR.find(toStr(c1, c2)) != MR.end()) {
                        ans = "";
                        break;
                    }
                }
            }
        }
        
       printf("Case #%d: [", cas); 
       bool first = true;
       for (i = 0; i < ans.size(); i++) {
           if (first) first = false; else printf(", ");
           putchar(ans[i]);
       } 
       printf("]\n");
    }
    return 0;
}

