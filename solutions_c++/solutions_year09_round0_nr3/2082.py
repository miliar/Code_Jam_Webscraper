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

const string text = "welcome to code jam";
string s;
int count(int p1, int p2)
{
    if (p2 == SZ(text))
        return 1;
    if (p1 == SZ(s))
        return 0;
    if (s[p1] == text[p2])
        return count(p1, p2+1)+count(p1+1, p2);
    else
        return count(p1+1, p2);
}
int main()
{
    int n;
    cin >> n;
    getline(cin, s);
    for (int i = 0; i < n; ++i)
    {
        getline(cin, s);
        string res = convert<string>(count(0, 0)%1000);
        while (SZ(res) < 4) res = '0' + res;
        cout << "Case #" << i+1 << ": " << res << endl;

    }
    return 0;
}