#include <stdio.h>
#include <set>
#include <string>
#include <algorithm>

using namespace std;

struct node
{
    double w;
    string s;
    int l, r;
} a[1024];

int main()
{
    int t;

    int n = 0;
    
    scanf("%d", &t);
    for (int tt=1; tt<=t; tt++)
    {
        for (int i=0; i<n; i++)
        {
            a[i].l = a[i].r = 0;
            a[i].s = "";
        }

        int k = 0;
        char s[1024];
        scanf("%d", &k);
        gets(s);


        int st[1024];
        int t = 0;
        int cur = 0;
        n = 1;

        for (; k--;)
        {
            char *w = gets(s);

            for (; *w; w++)
            {
                if (*w == '(')
                {
                    st[t++] = cur;
                    if (!a[cur].l)
                        cur = a[cur].l = n++;
                    else
                        cur = a[cur].r = n++;
                    continue;
                }
                if (*w >= '0' && *w <= '9')
                {
                    sscanf(w, "%lf", &a[cur].w);
                    for (; *w >= '0' && *w <= '9' || *w == '.'; w++);
                    w--;
                    continue;
                }
                if (*w >= 'a' && *w <= 'z')
                {
                    for (; *w >= 'a' && *w <= 'z'; w++)
                        a[cur].s += *w;
                    w--;
                    continue;
                }
                if (*w == ')')
                {
                    cur = st[--t];
                    continue;
                }
            }
        }


        printf("Case #%d:\n", tt);
        scanf("%d", &k);
        for (; k--;)
        {
            int n;
            scanf("%s%d", s, &n);

            set<string> x;
            for (; n--;)
            {
                scanf("%s", s);
                x.insert(s);
            }

            double p = 1;

            for (cur = 1; cur; )
            {
                p *= a[cur].w;
                if (x.count(a[cur].s))
                    cur = a[cur].l;
                else
                    cur = a[cur].r;
            }

            printf("%.8lf\n", p);
        }
       
    }
    return 0;
}
