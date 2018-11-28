#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <list>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

typedef long long LL;
typedef vector <int> VI;
typedef vector <double> VD;
typedef vector <vector<int > > VVI;
typedef pair <int,int> PII;
typedef vector <LL> VL;
typedef vector <string> VS;

#define INF 1000000000

VS split(string s, string t=" ") {
    VS ret;
    int a,b=0;
    while ((a=s.find_first_not_of(t,b))!=-1) {
        b=s.find_first_of(t,a);
        ret.push_back(s.substr(a,b-a));
    }
    return ret;
}

vector<string> a;
vector<string> b;

map<pair<int,string>, int> memo;

int go(int n, string str)
{
    if (memo.count(make_pair(n,str))) return memo[make_pair(n,str)];
    int &ret = memo[make_pair(n,str)];
    if (n == 0) return ret=0;
    if (b[n-1] == str) {
        return ret=INF;
    }
    ret = INF;
    for (int i=0; i<a.size(); i++) {
        if (a[i] == str) {
            ret <?= go(n-1,a[i]);
        } else {
            ret <?= 1+go(n-1,a[i]);
        }
    }
    return ret;
}

int main()
{
    int n;
    scanf("%d\n", &n);

    for (int tr=0; tr<n; tr++) {
        a.clear();
        b.clear();
        memo.clear();
        int s;
        scanf("%d\n", &s);
        for (int i=0; i<s; i++) {
            string buf;
            getline(cin,buf);
            a.push_back(buf);
        }
        int q;
        scanf("%d\n", &q);
        for (int qr=0; qr<q; qr++) {
            string buf;
            getline(cin,buf);
            b.push_back(buf);
        }
        int ret = INF;

        for (int i=0; i<a.size(); i++) {
            ret <?= go(q,a[i]);
        }
        printf("Case #%d: %d\n", tr+1, ret);
    }
}
