#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <assert.h>
#include <cstring>

using namespace std;
#define pb push_back
#define mp make_pair
#define loop(i,n) for (int i=0;i<n;++i)
#define loop2(i,l,r) for (int i=l;i<r;++i)
#define all(v) (v).begin(),(v).end()
#define foreach(it,A) for(typeof A.begin() it=A.begin();it!=A.end();++it)
#define print(A) {foreach(it,A) cout<<*it<<" ";cout<<endl;}
#define two(x) (1ll<<(x))
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;


int main(){
    int nTest; cin>>nTest;
    loop(test,nTest) {
        int a,b;
        cin>>a>>b;
        int nDigit = 1, upper = 10;
        ll res = 0;
        loop2(x,a,b+1) {
            while (x>=upper) {
                nDigit++;upper*=10;
            }
            int y = x;
            set<int> used;
            loop(i,nDigit-1) {
                y = (y+(y%10)*upper)/10;
                if (y>x && y>=a && y<=b) {
                    if (used.count(y)) continue;
                    used.insert(y);
                    ++res;
                }
            }
        }
        cout<<"Case #"<<test+1<<": "<<res<<endl;
    }
}
