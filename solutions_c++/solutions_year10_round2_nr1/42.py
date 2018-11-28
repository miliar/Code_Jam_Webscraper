#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <ctime>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define SIZE(c) ((int)((c).size()))
#define FOREACH(i,c) for(__typeof((c).begin()) i =(c).begin();i!=(c).end();++i)
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef long long LL;
typedef long double LD;

#define st first
#define nd second
#define mp make_pair
#define pb push_back

const int NIL = (-1);

vector<string> split(string s) {
    vector<string> v;
    for(int i=1;i<s.length();i++)
        if (s[i]=='/')
            v.push_back(s.substr(0,i));
    v.push_back(s);
    return v;
}

void scase() {
    set<string> s;
    int n,m;
    cin >> n >> m;
    while(n--) {
        string buf;
        cin >> buf;
        s.insert(buf);
    }
    int count = 0;
    while(m--) {
        string buf;
        cin >> buf;
        vector<string> v = split(buf);
        for(int i=0;i<v.size();i++)
            if (s.find(v[i])==s.end()) {
                s.insert(v[i]);
                count ++;
            }
    }
    cout << count << endl;
}

int main() {
    int j;
    cin >> j; 
    for(int i=1;i<=j;i++) {
        cout << "Case #"<<i<<": ";
        scase();
    }
    return 0;
}

