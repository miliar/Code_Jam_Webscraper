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

int m, v;
int gate[10001];
int canChange[10001];
int dp[10001][2];
int go(int pos, int expected) {
    if (pos >= (m-1)/2) {
        return (gate[pos] == expected)?0:-1;
    }
    int &ans = dp[pos][expected];
    if ( ans >= -1) {
        return ans;
    }
    // gate
    if (!canChange[pos]) {
        if (gate[pos]) { // and
            if (expected == 0) {
                int left = go(pos*2+1, 0);
                int right = go(pos*2+2, 0);
                if (left >=0 || right >=0) {
                    if (left == -1) return ans = right;
                    if (right == -1) return ans = left;
                    return ans = min(left, right);
                }
                return ans = -1;
            } else {
                int left = go(pos*2+1, 1);
                int right = go(pos*2+2, 1);
                if (left >=0 && right >=0) return ans = left + right;
                return ans = -1;                
            }
        }
        else {
            if (expected == 0) {
                int left = go(pos*2+1, 0);
                int right = go(pos*2+2, 0);
                if (left >=0 && right >=0) return ans = left + right;
                return ans = -1;                
            } else {
                int left = go(pos*2+1, 1);
                int right = go(pos*2+2, 1);
                if (left >=0 || right >=0) {
                    if (left == -1) return ans = right;
                    if (right == -1) return ans = left;
                    return ans = min(left, right);
                }
                return ans = -1;
            }
        }
    }
    else { 
        // and
        if (expected == 0) {
            int left = go(pos*2+1, 0);
            int right = go(pos*2+2, 0);
            if (left >=0 || right >=0) {
                if (left == -1) ans = right;
                else if (right == -1) ans = left;
                else ans = min(left, right);
            }
            else ans = -1;
        } else {
            int left = go(pos*2+1, 1);
            int right = go(pos*2+2, 1);
            if (left >=0 && right >=0) ans = left + right;
            else ans = -1;                
        }
        if (gate[pos] == 0 && ans >=0) {
            ans++;
        }
        int ans2 = -1;
        // or gate try
        if (expected == 0) {
            int left = go(pos*2+1, 0);
            int right = go(pos*2+2, 0);
            if (left >=0 && right >=0) ans2 = left + right;
            else ans2 = -1;                
        } else {
            int left = go(pos*2+1, 1);
            int right = go(pos*2+2, 1);
            if (left >=0 || right >=0) {
                if (left == -1) ans2 = right;
                else if (right == -1) ans2 = left;
                else ans2 = min(left, right);
            }
            else ans2 = -1;
        }
        if (ans2 >=0 && gate[pos] == 1) 
            ans2++;
        if (ans2 >=0 || ans >=0 ){
            if (ans2 == -1) return ans;
            if (ans == -1) return ans = ans2;
            return ans = min(ans, ans2);
        }
        return ans;
    }
}
int main() {
    int testCases;
    cin>>testCases;
    f(testCase, 1, testCases+1) {
        cin>>m>>v;
        init(gate, 0);
        init(canChange, 0);
        f(i, 0, 10001) {
            f(j,0,2) dp[i][j] = -2;
        }
        int i;
        for (i=0;i<(m-1)/2;i++) {
            cin>>gate[i]>>canChange[i];
        }
        f(j,0,(m+1)/2) {
            cin>>gate[i+j];
            canChange[i+j] = 0;
        }
        int ans = go(0, v);
        /*
        f(i,0,m) {
            cout<<i<<" "<<dp[i][0]<<" "<<dp[i][1]<<endl;
        }
        */
        cout<<"Case #"<<testCase<<": ";
        if (ans == -1) {
            cout<<"IMPOSSIBLE";
        }
        else cout<<ans;
        cout<<endl;
    }
    return 0;
}
