#include <vector>        
#include <map>        
#include <set>        
#include <deque>        
#include <algorithm>        
#include <utility>        
#include <sstream>        
#include <iostream>        
#include <cstdio>        
#include <cmath>        
#include <cstdlib> 
#include <string>
#include <time.h>

using namespace std;   

#define SZ(a) ((int)(a).size())   
#define pii pair<int, int>  
#define mp make_pair  
template<class A, class B> A convert(B x) {stringstream s; s << x; A r; s >> r; return r;}

vector<string> pattern;
vector<string> a;


int main()
{

    int l, d, n;
    cin >> l >> d >> n;
    for (int i = 0; i < d; ++i)
    {
        string s;
        cin >> s;
        a.push_back(s);
    }
    sort(a.begin(), a.end());

    for (int i = 0; i < n; ++i)
    {
        string s;
        cin >> s;
        pattern.clear();
        pattern.push_back("");
        bool fl = false;
        for (int j = 0; j < SZ(s); ++j)
        {
            if (s[j] == '(') 
            {
                fl = true;
                continue;
            }
            if (s[j] == ')')
            {
                fl = false;
                pattern.push_back("");
                continue;
            }
            if (fl)
                pattern[SZ(pattern)-1] += s[j];
            else
            {
                pattern[SZ(pattern)-1] += s[j];
                pattern.push_back("");
            }
        }
        
        pattern.push_back("");
        int res = 0;
        for (int j = 0; j < SZ(a); ++j)
        {
            ++res;
            for (int k = 0; k < SZ(a[j]); ++k)
               if (pattern[k].find(a[j][k]) >= SZ(pattern[k]))
                {
                    --res;
                    break;
                }
        }
        cout << "Case #" << i+1 << ": " << res << endl;
    }

    return 0;
}