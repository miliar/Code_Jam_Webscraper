#include <iostream>
#include <algorithm>

using namespace std;

struct str
{
    bool a;
    bool b;
    int t;
    bool operator <(const str &x) const
    {
        return t != x.t ? t < x.t : a > x.a;
    }
} a[512];

int main()
{
    int t;
    cin >> t;
    for (int tt=1; tt<=t; tt++)
    {
        int na, nb, i, n, x;
        cin >> x >> na >> nb;
        n = na+nb;
        for (i=0; i<na; i++)
        {
            char s[10];
            cin >> s;
            int t = (s[0]-'0')*600 + (s[1]-'0')*60 + (s[3]-'0')*10 + (s[4]-'0');
            a[2*i].a = false;
            a[2*i].b = false;
            a[2*i].t = t;
            cin >> s;
            t = (s[0]-'0')*600 + (s[1]-'0')*60 + (s[3]-'0')*10 + (s[4]-'0');
            a[2*i+1].a = true;
            a[2*i+1].b = true;
            a[2*i+1].t = t+x;
        }
        for (; i<n; i++)
        {
            char s[10];
            cin >> s;
            int t = (s[0]-'0')*600 + (s[1]-'0')*60 + (s[3]-'0')*10 + (s[4]-'0');
            a[2*i].a = false;
            a[2*i].b = true;
            a[2*i].t = t;
            cin >> s;
            t = (s[0]-'0')*600 + (s[1]-'0')*60 + (s[3]-'0')*10 + (s[4]-'0');
            a[2*i+1].a = true;
            a[2*i+1].b = false;
            a[2*i+1].t = t+x;
        }
        sort(a, a+2*n);
        int ansa = 0, ansb = 0;
        int ka = 0, kb = 0;
        for (i=0; i<2*n; i++)
        {
            if (a[i].a)
                if (a[i].b)
                    kb++;
                else
                    ka++;
            else
                if (a[i].b)
                    if (kb)
                        kb--;
                    else
                        ansb++;
                else
                    if (ka)
                        ka--;
                    else
                        ansa++;
        }
        cout << "Case #" << tt << ": " << ansa << " " << ansb << endl;
    }

    return 0;
}
