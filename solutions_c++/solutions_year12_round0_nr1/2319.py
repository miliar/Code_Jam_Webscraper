#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#define PI 3.141592653589793238

using namespace std;

const char mapping[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int mp[30];

int ntest;

int main() {
    freopen("01.inp", "r", stdin);
    freopen("01.out", "w", stdout);
    
    /*for (int i = 0; i < 3; i++) {
        string s1, s2;
        char tmp[1010];
        gets(tmp);
        s1 = tmp;
        gets(tmp);
        s2 = tmp;
        for (int j = 0; j < s1.length(); j++)
            if (s1[j] >= 'a' && s1[j] <= 'z') 
               mp[s1[j] - 'a'] = s2[j] - 'a';
    }
    for (int i = 0; i < 26; i++)
        cout << (char)(i + 'a') << ',';
    cout << endl;
    for (int i = 0; i < 26; i++)
        cout << "'" << (char)(mp[i] + 'a') << "'" << ',';
    cout << endl;*/
    
    scanf("%d\n", &ntest);
    for (int test = 1; test <= ntest; test++) {
        char tmp[1010];
        gets(tmp);
        string s = tmp;
        string ans = "";
        for (int i = 0; i < s.length(); i++)
            if (s[i] >= 'a' && s[i] <= 'z')
               ans += mapping[s[i] - 'a'];
            else
                ans += s[i];
        cout << "Case #"  << test << ": " << ans << endl;
    }
}       
