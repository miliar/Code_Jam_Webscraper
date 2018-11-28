#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t;
    scanf("%i\n", &t);
    string s;
    /*ejp mysljylc kd kxveddknmc re jsicpdrysi
    rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
    de kr kd eoya kw aej tysr re ujdr lkgc jv
Output
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
*/
    char a[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w',
    //             a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t
                  'j','p','f','m','a','q'};
    //             u   v   w   x   y   z
    for (int i=1; i<=t; i++)
    {
        getline(cin, s);
        printf("Case #%i: ", i);
        for (int j=0; j<s.length(); j++)
            if (s[j] >= 'a' && s[j] <= 'z')
                cout << a[s[j]-'a'];
            else
                cout << s[j];
        cout << endl;
    }
    return 0;
}
