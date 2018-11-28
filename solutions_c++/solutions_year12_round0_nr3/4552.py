#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <sstream>
using namespace std;

string inttostr(unsigned int number)
{
    stringstream str;
    str << number;
    return str.str();
}
unsigned int strtoint(string str)
{
    istringstream s(str);
    unsigned int ret;
    s >> ret;
    return ret;
}

string recycle(const string s, int n)
{
    string res = "";
    res += s.substr(s.length()-n,n);
    res += s.substr(0, s.length()-n);
    return res;
}

int main2()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int T; scanf("%d", &T);
    for(int ti= 1; ti<=T; ++ti)
    {
        int a, b, ret = 0, w;
        cin >> a >> b;
        int len = inttostr(a).length();
        for(int i=a; i<=b; ++i)
        {
            for(int q = 1; q < len; q++)
            {
                string sss = inttostr(i);
                sss = recycle(sss, q);
                if(sss.at(0)!='0') {
                    w = strtoint(sss);
                    if(i<w && w<=b) ret++;
                }
            }
        }
        printf("Case #%d: %d\n", ti, ret);
    }
    return 0;
}

int main()
{
    return main2();
}
