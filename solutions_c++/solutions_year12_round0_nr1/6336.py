#include <iostream>
#include <cstdio>

using namespace std;

char flag[1005]
= {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
    //freopen("/home/zhj/gcj.in", "r", stdin);
    //freopen("/home/zhj/gcj.out", "w", stdout);
    int T;
    scanf("%d", &T);
    string ss;
    getline(cin, ss);
    for (int reg = 0; reg < T; reg++)
    {
        cout << "Case #" << reg+1 << ": ";
        string str;
        getline(cin, str);
        for (int i = 0; i < str.length(); i++)
        {
            if (str[i] == ' ')
            {
                cout << ' ';
                continue;
            }
            cout << flag[str[i]-'a'];
        }
        cout << endl;
    }
    return 0;
}
