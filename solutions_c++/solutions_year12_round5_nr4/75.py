#include <iostream>
#include <string.h>

using namespace std;

char s[1024];

char* r = "oieastbg";

int a[128][128];

int main()
{
    int t;
    cin >> t;
    for (int tt=1; tt<=t; tt++)
    {   
        int k;
        cin >> k >> s;

        int ans = 1;

        if (!s[1])
            ans += !strchr(r, s[0]);

        memset(a, 0, sizeof(a));

        for (int i=0; s[i+1]; i++)
        {
            a[s[i]][s[i+1]] = 1;
            if (strchr(r, s[i]))
                a[strchr(r, s[i]) - r][s[i+1]] = 1;

            if (strchr(r, s[i+1]))
            {
                a[s[i]][strchr(r, s[i+1]) - r] = 1;
                if (strchr(r, s[i]))
                    a[strchr(r, s[i]) - r][strchr(r, s[i+1]) - r] = 1;
            }
        }

        bool f = false;
        for (int i=0; i<128; i++)
        {
            int in = 0;
            int out = 0;

            for (int j=0; j<128; j++)
            {
                in += a[j][i];
                out += a[i][j];
            }

            ans += max(in, out);

            f |= in != out;
        }
        if (f)
            ans--;

        cout << "Case #" << tt << ": " << ans << endl;
    }
    return 0;
}
