#include <algorithm>
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

string expr;
vs data;
int ch[21][256];
int n;
int k;
int arr[21];
int idx;
int dp[10];
int fact(int t) {
    if (t == 1) return 1;
    if (dp[t]) return dp[t];
    return dp[t] = t * fact(t-1);
}
void getVal(int cur, int remaining, ll &val){ 
    if (remaining == 0) {
        ll currentAns = 0;
        ll currentExpr = 1;
        f(i,0,expr.sz) {
            if (expr[i] == '+') {
                currentAns += currentExpr;
                currentExpr = 1;
                continue;
            }
            int cnt = 0;
            f(j,0,idx) {
                cnt += ch[arr[j]][expr[i]];
            }
            currentExpr = (currentExpr*cnt)%10009;
        }
        val = (currentExpr + currentAns + val)%10009;
        return;
    }
    f(i,0,n) {
        arr[idx] = i;
        idx++;
        getVal(i+1, remaining-1, val);
        idx--;
    }
}
int main() {
    int N;
    cin>>N;
    f(test,1,N+1) {
        init(ch, 0);
        cin>>expr>>k;
        cin>>n;
        f(i,0,n) {
            string str;
            cin>>str;
            f(j,0,str.sz) {
                ch[i][str[j]]++;
            }
        }
        cout<<"Case #"<<test<<":";
        f(i,1,k+1) {
            ll an = 0;
            getVal(0, i, an);
            cout<<" "<<an;
        }
        cout<<endl;
    }
    return 0;
}
