#include<cstdio>
#include<string>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<map>
#include<queue>
#include<vector>
#include<iostream>
#include<sstream>

using namespace std;

#define pf printf
#define sf scanf
#define co continue
#define re return
#define pb push_back
#define fo(a,b) for(a=0;a<b;a++)

vector<int> v1, v2;

int main() {
    
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;
    int cases = 1;
    int i;
    for( sf("%d", &t); t--; ) {
         int n;
         sf("%d", &n);
         v1.clear();
         v2.clear();
         for(i=0;i<n;i++) {
           int a;
           cin >> a;
           v1.pb(a);
         }
         
         for(i=0;i<n;i++) {
           int a;
           cin >> a;
           v2.pb(a);
         }
         
         sort(v1.begin(), v1.end() );
         sort(v2.begin(), v2.end() );
         reverse(v2.begin(), v2.end() );
         
         long long res = 0;
         
         for(i=0;i<n;i++) {
           res += (long long) v1[i] * v2[i];
         }
         
         cout << "Case #" << cases++ << ": " <<  res << endl;
    }
    return 0;
}

