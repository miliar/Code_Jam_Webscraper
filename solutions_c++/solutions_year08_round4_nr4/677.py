#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int) n; ++i)
#define fore(i, a, b) for(int i = (int) a; i < (int) b; ++i)

#define ll long long
#define ld long double

const ld EPS = 1e-9;
const int MAXN = 2000;

char tmp[MAXN];
string s, s1;
int k;
vector <int> v;

int count(string &s){
    char l = ' ';
    int res = 0;
    forn(i, s.size()){
        if (s[i] != l){
           ++res;
           l = s[i];
        }
    }
    return res;
}

int main()
{
    freopen("input.txt","rt", stdin);
    freopen("output.txt", "wt", stdout);    
    int tk;
    cin >> tk;
    
    forn(ii, tk){
        scanf("%d", &k);
        scanf("%s", &tmp);
        s = tmp; 
        s1 = s;
        int t = s.size() / k;
        
        v.clear();
        forn(i, k){
           v.push_back(i);
        }
        
        int ans = s.size() + 1;
        
        ans = min(ans, count(s1));
        
        while (next_permutation(v.begin(), v.end())){
           forn(j, t){
               forn(i, k){
                   s1[j * k + i] = s[j * k + v[i]];                   
               } 
           }
           ans = min(ans, count(s1));
        }  

       printf("Case #%d: ", ii + 1);
   
       printf("%d\n", ans);

        
    }          
    return 0;
}

