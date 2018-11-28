#include <iostream>
#include <string>

using namespace std;

int t;

string combine(int length, string *strs, string str)
{
    int len = str.length();
    if (len >= 2)
    {
        char last = str[len -1];
        char blast = str[len -2];
        for(int i=0; i<length; i++)
        {
            if((last == strs[i][0] && blast == strs[i][1]) || (last == strs[i][1] && blast == strs[i][0]))
            {
                string res = str.substr(0, len - 2) + strs[0][2];
                return res;
            }
        }
    }
    return str;
}

string oppose(int length, string *strs, string str)
{
    int len = str.length();
    if (len >= 2)
    {
        for(int i = 0; i < length; ++i)
        {
            if(str.find(strs[i][0]) != string::npos && str.find(strs[i][1]) != string::npos)
            {
                return string("");
            }
        }
    }
    return str;
}

string pretty(string ugly)
{
    string res = "[";
    int len = ugly.length();
    if(len > 0)
    {
        res += ugly[0];
        for(int i=1; i<len; i++)
        {
            res += ", ";
            res += ugly[i];
        }
    }
    res += "]";
    
    return res;
}

int main()
{
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    
    cin >> t;
    for(int i = 0; i < t; ++i)
    {
        int c,d,n;
        string str;
        string *cstrs;
        string *dstrs;
        
        cin >> c;
        cstrs = new string[c];
        for(int j = 0; j < c; j++)
        {
            string cstr;
            cin >> cstr;
            cstrs[j] = cstr;
        }
        
        cin >> d;
        dstrs = new string[d];
        for(int j = 0; j < d; j++)
        {
            string dstr;
            cin >> dstr;
            dstrs[j] = dstr;
        }
        
        cin >> n;
        str = "";
        for(int j = 0; j < n; j++)
        {
            char ch;
            cin >> ch;
            str += ch;
            str = combine(c, cstrs, str);
            str = oppose(d, dstrs, str);
        }
        
        cout << "Case #" << i+1 << ": " << pretty(str) << endl;
        
        delete [] cstrs;
        delete [] dstrs;
    }
}