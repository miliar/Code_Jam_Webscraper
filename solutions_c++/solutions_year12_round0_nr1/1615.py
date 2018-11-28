#include <iostream>
#include <string>

using namespace std;


int main()
{
    string in("ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv");
    string out("our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up");
    char x[256] = {0};
    for (int i = 0; i < in.size(); ++i) x[in[i]] = out[i];
    x['z'] = 'q';
    x['q'] = 'z';
    int T;
    cin >> T;
    char s[500] = {0};
    cin.getline(s, 500);
    for (int t = 1; t <= T; ++t)
    {
        cin.getline(s, 500);
        cout << "Case #" << t << ": ";
        for (int i = 0; i < strlen(s); ++i) 
        {
            if (isalpha(s[i])) cout << x[s[i]];
            else cout << s[i];
        }
        cout << endl;
    }
    return 0;
}