#include <iostream>
#include <string>
#include <map>

using namespace std;

int main()
{
    string a = "qzejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string b = "zqour language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

    map<char, char> mapping;
    for (char c = 'a'; c <= 'z'; ++c)
    {
        int index = b.find(c);
        mapping.insert(make_pair(a[index], c));
    }

    freopen("A-small-attempt0.in","r",stdin);
    freopen("A_small.out","w",stdout);

    int t;
    cin >> t;
    char c = getchar();
    for (int i = 1; i <= t; ++i)
    {
        string s;
        getline(cin, s,'\n');
        cout << "Case #" << i << ": ";

        for (int j = 0; j < s.length(); ++j)
        {
            if (s[j] == ' ')
            {
                cout << ' ';
            }
            else
            {
                cout << mapping[s[j]];
            }
        }
        cout << endl;
    }

    return 0;

}