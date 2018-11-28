#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

long long s2i(const string& s)
{
    long long ret = 0;
    for(int i=0;i<s.size();i++) {
        ret = ret*10 + (s[i]-'0');
    }
    return ret;
}

bool isugly(long long n)
{
    return n%2 == 0 || n%3 == 0 || n%5 == 0 || n%7 == 0;
}

long long solve(const string& s, long long n, bool sign, int idx)
{
    if(idx == s.size()-1) {
        return isugly(n+(sign?1:-1)*s2i(s)) ? 1 : 0;
    }
    long long cnt = 0;
    cnt += solve(s, n, sign, idx+1);
    cnt += solve(s.substr(idx+1), n+(sign?1:-1)*s2i(s.substr(0, idx+1)), true, 0);
    cnt += solve(s.substr(idx+1), n+(sign?1:-1)*s2i(s.substr(0, idx+1)), false, 0);
    return cnt;
}

int main()
{
    string s;
    int t;
    cin >> s;
    t = s2i(s);
    for(int ii=0;ii<t;ii++) {
        string s;
        cin >> s;
        cout << "Case #" << ii+1 << ": " << solve(s, 0, true, 0) << endl;
    }

    return 0;
}
