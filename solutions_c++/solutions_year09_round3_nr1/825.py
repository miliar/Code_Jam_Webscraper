#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

string s;


void solve()
{
    long long x = 0;
    map<char, long long> m;
    vector<long long> v;
    
    m[s[0]] = 1;
    v.push_back(1);
    
    for (long long i = 1; i < s.length(); i++)
    {
        if (m.find(s[i]) == m.end()) {
            if (x == 1) x++;
            v.push_back(x);
            m[s[i]] = x;
            x++;
        } else {
            v.push_back(m[s[i]]);
        }       
    } 
    
    
    if (x == 1 || x == 0) x = 2;
    
    long long ans = 0;
    for (long long i = 0; i < v.size(); i++)
    {
        ans = ans * x + v[i];
    }     
    
    
    cout << ans << endl;     
}    

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    long long t; cin >> t;
    for (long long i = 1; i <= t; i++)
    {
        cout << "Case #" << i << ": ";
        cin >> s;
        solve();
    }    
}    

