#include <iostream>
#include <cstring>
#include <map>
using namespace std;

const char *q = "ejp mysljylc kd kxveddknmc re jsicpdrysi"\
                "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"\
                "de kr kd eoya kw aej tysr re ujdr lkgc jv"\
                "y qee";

const char *a = "our language is impossible to understand"\
                "there are twenty six factorial possibilities"\
                "so it is okay if you want to just give up"\
                "a zoo";

int main()
{
    const int len = strlen(q);
    map<char, char> table;
    for (int i=0; i < len; ++i)
    {
        table[q[i]] = a[i];
    }
    table[' '] = ' ';
    table['z'] = 'q';

    int Q;
    cin >> Q;
    string buf;
    getline(cin, buf);
    for (int ct=0; ct < Q; ++ct)
    {
        getline(cin, buf);
        cout << "Case #" << ct+1 << ": ";
        for (int i=0; i < buf.length(); ++i)
        {
            putchar(table[buf[i]]);
        }
        cout << endl;
    }
    
    return 0;
}
