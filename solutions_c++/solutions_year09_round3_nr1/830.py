#include <cstdlib>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
 

long long MinValue(const string & num )
{
    string s;
    for (int i=0; i<num.length(); ++i)
    {
        bool find = false;
        for (int j=0; j<s.length(); ++j)
            if (s[j] == num[i])
            {
                     find = true;
                     break;
            }
        if (!find)   s.append(1, num[i]);
    }
    int base = s.length();
    if ( base == 1)
    {
         base = 2;
         s.append(1, s[0]);
         s[0] = ' ';
     }
     else 
     {
        char c = s[0];
        s[0] = s[1];
        s[1] = c;
     }
    long long value = 0;
    for (int i=0; i<num.length(); ++i)
    {
        for (int j=0; j<base; ++j)
        {
            if ( num[i] == s[j] )
            {
                 value = (long long)j + value*(long long)base;
                 break;
            }
        }
    }
    return value;
}

int main(int argc, char *argv[])
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    string s;
    int T;
    cin >> T;
    for (int t=1; t<=T; ++t)
    {
        cin >> s;
        cout << "Case #" << t << ": "<< MinValue( s ) << endl;
    }
}
