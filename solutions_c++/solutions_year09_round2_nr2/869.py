#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

#define forn(i,n) for(int i=0;i<n;i++)
#define forab(i,a,b) for(int i=a;i<b;i++)
#define foreach(it,A) for(__typeof(A.begin()) it=A.begin();it!=A.end();it++)
#define forinc(i,a,b,inc) for(int i=a;i<b;i+=inc)
#define every(A) A.begin(),A.end()

#define DEBUG 0

#define dbg(x) if(DEBUG) cout<<x;
#define dbge(x) if(DEBUG) cout<<x<<endl;

int main() {
    int T;
    scanf("%d",&T);
    forn(i,T) {
        string s,t;
        cin>>s;
        t=s;
        next_permutation(s.begin(),s.end());
        dbge(s);
        if(s<=t) {
            if(s!=t) {
                sort(s.begin(), s.end());
            }
            int j=0;
            while(s[j]=='0')  {
                j++;
            }
            swap(s[0], s[j]);
            cout<<"Case #"<<(i+1)<<": "<<s[0]<<'0';
            if(s.length()>1) cout<<s.substr(1)<<endl;
            else cout<<endl;
        } else cout<<"Case #"<<(i+1)<<": "<<s<<endl;
    }
}
