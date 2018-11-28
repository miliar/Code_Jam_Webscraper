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

int arr[10];
int compress(string s) {
    int ret = 1;
    f(i,1,s.sz) {
        if (s[i] != s[i-1]) ret++;
    }
    return ret;
}
string modify(string s, int *arr, int k) {
    int t = s.sz / k;
    string result = "";
    f(i,0,t) {
        f(j,0,k)
        result = result + s[i*k + arr[j]];
    }
    return result;
}
int main() {
    int testCases;
    cin>>testCases;
    f(testCase, 1, testCases+1) {
        int k;
        string s;
        cin>>k>>s;
        f(i,0,k)arr[i] = i;
        int ans = compress(s);
        do {
            string s1 = modify(s, arr, k);
            int l = compress(s1);
            ans <?= l;
        }while (next_permutation(arr, arr+k));
        cout<<"Case #"<<testCase<<": ";
        if (ans == -1) {
            cout<<"IMPOSSIBLE";
        }
        else cout<<ans;
        cout<<endl;
    }
    return 0;
}
