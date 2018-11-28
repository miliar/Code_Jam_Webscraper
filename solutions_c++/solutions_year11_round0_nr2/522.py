#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
using namespace std;

int C, D, n;
map<string, string> change;
set<string> clear;

string S;

void init()
{
    string str;

    cin >> C;
    change.clear();
    for (int i = 0; i < C; i ++)
    {
        cin >> str;
        change[ str.substr(0, 1) + str.substr(1, 1) ] = str.substr(2, 1);
        change[ str.substr(1, 1) + str.substr(0, 1) ] = str.substr(2, 1);
    }
    cin >> D;
    clear.clear();
    for (int i = 0; i < D; i ++)
    {
        cin >> str;
        clear.insert( str.substr(0, 1) + str.substr(1, 1) );
        clear.insert( str.substr(1, 1) + str.substr(0, 1) );
    }
    cin >> n;
    cin >> S;
}

void solve()
{
    string target = "";

    for (int i = 0; i < n; i ++)
    {

        target += S[i];
        if (target.length() >= 2 && change.count( target.substr( target.length() - 2, 2 ) ) )
        {
            target = target.substr(0, target.length() - 2) + change[ target.substr( target.length() - 2, 2 ) ];
        }
        else
        {
            string tmp = S.substr(i, 1);
            for (int x = 0; x + 1 < target.length(); x ++)
            {
                if (clear.count( tmp + target[x] ))
                {
                    target = "";
                    break;
                }
            }
        }
    }

    printf("[");
    for (int i = 0; i < target.length(); i ++)
        printf("%c%s", target[i], i + 1== target.length() ? "" : ", ");
    printf("]\n");
//    printf("%s\n", target.c_str());
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T;
    cin >> T;
    for (int t = 1; t <= T; t ++)
    {
         printf("Case #%d: ", t);

         init();
         solve();
    }

    return 0;
}