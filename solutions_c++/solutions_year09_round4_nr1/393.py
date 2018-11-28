#include <algorithm>
#include <iterator>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;

typedef vector<int> vi;
typedef vector<string> vs;

#define f(i,a,b) for(int i=(a);i<(b);++i)
#define fd(i,a,b) for(int i=(a);i>=(b);--i)
#define pb(_v,_a) (_v).push_back(_a)
#define sz size()
#define range(_a) (_a).begin(),(_a).end()
#define foreach(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define init(m,v) memset((m), (v), sizeof((m)))
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 

ll ans;
int main() {
    int nn;
    cin>>nn;
    f(test,1,nn+1) {
        int n;
        ans = 0;
        cin>>n;
        vs mat;
        f(i,0,n) {
            string s;
            cin>>s;
            pb(mat,s);
        }
        vi ints(n);
        f(i,0,n) {
            ints[i] = -1;
            fd(j,n-1,0) {
                if (mat[i][j] == '1') {
                    ints[i] = j;
                    break;
                }
            }
        }
        f(i,0,n-1) {
            if (ints[i] > i) 
            f(j,i+1,n) {
                if (ints[j] <= i) {
                    int t = ints[j];
                    fd(k,j,i+1) { ans++; ints[k] = ints[k-1];}
                    ints[i] = t;
                    break;
                }
            }
        }
        cout<<"Case #"<<test<<": "<<ans<<endl;
    }
    return 0;
}
