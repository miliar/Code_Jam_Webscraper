#include <iostream>

using namespace std;

const int maxl = 15;
const int maxd = 5000;
const int maxn = 500;
char word[maxd][maxl];
char pattern[maxl][26];

int main()
{
    int l, d, n;
    int i, j, k;
    int count;
    bool inbracket;
    char curch;

    cin >> l >> d >> n;
    for (i = 0; i < d; i++)
    {
        for (j = 0; j < l; j++)
        {
            cin >> word[i][j];
        }
    }

    for (j = 1; j <= n; j++)
    {
        for (i = 0; i < l; i++)
        for (k = 0; k < 26; k++)
        {
            pattern[i][k] = 0;
        }

        for (i = 0; i < l;)
        {
            cin >> curch;
            switch (curch)
            {
            case '(':
                inbracket = true;
                break;
            case ')':
                inbracket = false;
                i++;
                break;
            default:
                pattern[i][curch - 'a'] = 1;
                if (!inbracket)
                    i++;
            }
        }
        
        count = 0;
        for (i = 0; i < d; i++)
        {
            for (k = 0; k < l; k++)
            {
                if (!pattern[k][word[i][k] - 'a'])
                    break;
            }
            if (k == l)
                ++count;
        }
        cout << "Case #" << j << ": " << count << endl;
    }

    return 0;
}

