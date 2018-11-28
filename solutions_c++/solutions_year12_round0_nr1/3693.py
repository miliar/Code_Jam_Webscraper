#include <cstring>
#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("i.txt","r",stdin);
    freopen("o.txt","w",stdout);
    char a[30] = {'y','h','e','s','o', 'c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

    int t;

    cin >> t;

    getchar();

    char s[200];

    for(int i = 1; i <= t; i++)
    {
        gets(s);

        cout << "Case #"<< i <<": ";

        for(int i = 0; i < strlen(s); i++)
        {
            if( s[i]!=' ') cout << a[ s[i]-'a'];
            else cout << ' ';
        }
        cout << endl;

    }

    return 0;
}
