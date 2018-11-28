#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <map>
using namespace std;

string s;
const string w = "welcome to code jam";

map<pair<int, int>, int> memo;

int solve(int p, int q)
{
    int r = 0, r2 = 0;
    if(q == w.size())
        return 1;
    if(p == s.size())
        return 0;
    map<pair<int, int>, int>::iterator it = memo.find(make_pair(p, q));
    if(it != memo.end())
        return it->second;
    if(s[p] == w[q]) {
        r = solve(p+1, q+1);
        memo.insert(make_pair(make_pair(p+1, q+1), r));
    }
    r2 = solve(p+1, q);
    memo.insert(make_pair(make_pair(p+1, q), r2));
    return r+r2;
}

int main()
{
    int n;
    cin >> n;
    string tmp;
    getline(cin, tmp);

    for(int cnt=1;cnt<=n;cnt++) {
        getline(cin, s);
//        cout << s << endl;

        memo.clear();

        printf("Case #%d: %04d\n", cnt, solve(0, 0));
    }
    
    return 0;
}
