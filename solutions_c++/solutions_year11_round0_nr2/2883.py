#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int MAX_CHAR = 128;
char combine [MAX_CHAR][MAX_CHAR];
bool oppose [MAX_CHAR][MAX_CHAR];

int main()
{
    int nTests;
    cin >> nTests;
    for (int test = 0; test < nTests; test++)
    {
        memset(combine, 0, sizeof(combine));
        memset(oppose, 0, sizeof(oppose));

        int c;
        cin >> c;

        for (int i = 0; i < c; i++)
        {
            string s;
            cin >> s;
            combine[s[0]][s[1]] = s[2];
            combine[s[1]][s[0]] = s[2];
        }                

        int d;
        cin >> d;

        for (int i = 0; i < d;  i++)
        {
            string s;
            cin >> s;
            oppose[s[0]][s[1]] = true;
            oppose[s[1]][s[0]] = true;
        }

        int n;
        cin >> n;

        string s;
        cin >> s;

        string a;
        for (int i = 0; i < n; i++)
        {
            a += s[i];

            if (a.size() >= 2)
            {
                char u = a[a.size() - 2];
                char v = a[a.size() - 1];
                if (combine[u][v])
                {
                    a.erase(a.size() - 2);
                    a += combine[u][v];
                }
            }

            for (int j = 0; j + 1 < a.size(); j++)
            {
                char u = a[j];
                char v = a[a.size() - 1];
                if (oppose[u][v])
                {
                    a = "";
                    break;
                }
            }
        }

        printf("Case #%d: [", test + 1);
        for (int i = 0; i < a.size(); i++)
        {
            if (i) printf(", ");
            printf("%c", a[i]);
        }
        printf("]\n");
    }

    return 0;
}