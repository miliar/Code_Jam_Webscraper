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

int main() {
    int testCases;
    cin>>testCases;
    string s;
    f(testCase, 1, testCases+1) {
        cin>>s;
        char *c = (char *)s.c_str();
        int l = strlen(c);
        cout<<"Case #"<<testCase<<": ";
        if (next_permutation(c, c+l)) 
        {
            f(i,0,l) cout<<c[i];
            cout<<endl;
        } else {
            sort(c, c+l);
            int i=0;
            while (c[i] == '0') i++;
            cout<<c[i];
            f(j,0,i) cout<<"0";
            cout<<"0";
            f(j,i+1,l) cout<<c[j];
            cout<<endl;
        }
    }
    return 0;
}
