#include <string.h>
#include <iostream>
#include <cstdio>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <cmath>
#include <string>
#include <map>
#include <cassert>
#include <queue>

using namespace std;

#define forn(i, n)  for (int i = 0; i < int(n); i++)

map<string,string> rep;
vector<string> opp;
string s;
int n;

void read()
{
    rep.clear();
    opp.clear();
    
    int c;
    cin >> c;
    forn(i, c)
    {
        string t;
        cin >> t;
        string a = t.substr(0, 2);
        string b = t.substr(2, 1);
        assert(rep.count(a) == 0);
        rep[a] = b;
        reverse(a.begin(), a.end());
        //assert(rep.count(a) == 0);
        rep[a] = b;
    }

    int d;
    cin >> d;
    forn(i, d)
    {
        string a;
        cin >> a;
        assert(a[0] != a[1]);
        opp.push_back(a);
    }

    cin >> n;
    cin >> s;
}

void process()
{
    string result;
    forn(i, n)
    {
        result += s[i];
        if (result.length() > 1)
        {
            if (rep.count(result.substr(result.length() - 2, 2)))
            {
                string c = rep[result.substr(result.length() - 2, 2)];
                result.erase(result.length() - 2, 2);
                result += c;
                continue;
            }
        }

        forn(j, opp.size())
        {
            const string& p = opp[j];
            if (result[result.length() - 1] == p[0] && result.find(p[1]) != string::npos)
            {
                result.clear();
                break;
            }
            else
            {
                if (result[result.length() - 1] == p[1] && result.find(p[0]) != string::npos)
                {
                    result.clear();
                    break;
                }
            }
        }
    }
    cout << "[";
    forn(i, result.length())
    {
        if (i != 0)
            cout << ", ";
        cout << result[i];
    }
    cout << "]" << endl;
}

int main(int argc, char* argv[])
{
    freopen("input.txt", "rt", stdin);
    
    int cases;
    scanf("%d", &cases);

    int from = (argc > 1 ? atoi(argv[1]) : 1);
    int to = (argc > 2 ? atoi(argv[2]) : cases);

    for (int i = 1; i <= cases; i++)
    {
        read();
        if (from <= i && i <= to)
        {
            printf("Case #%d: ", i);
            process();
        }
    }

    return 0;
}

