/**********************************************************************
Author: littlekid
Created Time: Thu 17 Jul 2008 08:31:49 AM CST
File Name: 
Description: 
**********************************************************************/
#include <iostream>
#include <string>
#include <fstream>
using namespace std;
#define out(x) printf("%s %lld\n", #x, (long long)(x))
const int maxint=0x7FFFFFFF;

template <class T> void get_max(T& _a, const T &_b) {_b > _a? _a = _b:1;}
template <class T> void get_min(T& _a, const T &_b) {_b < _a? _a = _b:1;}

const int MAXS = 100;

int s;
string name[MAXS+1];

void get_engines_name()
{
    cin >> s;
    getchar();
    for (int ix = 1; ix <= s; ++ ix)
    {
        getline(cin, name[ix]);
    }
}

int query()
{
    int q; cin >> q; getchar();
    string word;
    bool incur[s+1];
    memset(incur, false, sizeof(incur));
    int en = s, res = 0;
    while (q --)
    {
        getline(cin, word);
        for (int ix = 1; ix <= s; ++ ix)
        {
            if (!incur[ix])
            {
                if (word == name[ix])
                {
                    -- en;
                    if (en == 0)
                    {
                        ++ res; en = s-1;
                        memset(incur, false, sizeof(incur));
                    }
                    incur[ix] = true;
                    break;
                }
            }
        }
    }
    return res;
}

int main()
{
    int T; cin >> T;
 //   ofstream fout ("A.out");
    for (int ca = 1; ca <= T; ++ ca)
    {
        get_engines_name();
        cout << "Case #" << ca << ": " << query() << endl;
    }
    return 0;
}

