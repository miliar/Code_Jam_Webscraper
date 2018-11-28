#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <utility>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int) n; ++i)
#define fore(i, a, b) for(int i = (int) a; i < (int) b; ++i)

#define ll long long
#define ld long double
#define PLL pair <ld, ld>

#define x first
#define y second

const ld EPS = 1e-9;
const int MAXN = 100000;

string a[MAXN];
char tmp[MAXN];
string s, s1;

vector <string> v;
int main()
{
    freopen("input.txt","rt", stdin);
    freopen("output.txt", "wt", stdout);    
       
    int l, d, n;
    cin >> l >> d >> n;
    
    forn(i, d){
        scanf("%s", &tmp);
        a[i] = tmp;
    }
    
    forn(iii, n){
        scanf("%s", &tmp);
        s = tmp;
        int j = 0;
        
        v.clear();
        v.reserve(15);
        
        while (j < s.size()){
            if (s[j] == '('){
                ++j;
                s1 = "";
                while (s[j] != ')'){
                    s1 += s[j];
                    ++j;
                }
                v.push_back(s1);
                ++j;
                continue;
            } 
            s1 = "";
            s1 += s[j];
            v.push_back(s1);
            ++j;
        }
        
        int cnt = 0;
        forn(i, d){
            bool f = 1;
            if (v.size() != l) continue;
            
            forn(j, v.size()){
                bool cur = 0;
                forn(k, v[j].size()){
                    if (v[j][k] == a[i][j]){
                        cur = 1;
                        break;
                    }
                }
                if (!cur){
                   f = 0;
                   break;
                }
            }
            if (f) ++cnt;
        }
        printf("Case #%d: %d\n", iii + 1, cnt);
    }
                            
    return 0;
}

