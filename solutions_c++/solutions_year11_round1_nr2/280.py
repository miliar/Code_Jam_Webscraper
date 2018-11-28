#include <cstdio>
#include <cstring>

using namespace std;

#define MAXN 1000
char w[MAXN][20];
char s[100];
int n, m;
bool nn[MAXN];
int tc;


bool has(int word, char letter)
{
    char *p = &(w[word][0]);
    while (*p)
    {
        if (*p == letter) return true;
        p++;
    }
    return false;
}

bool same(int w1, int w2, char letter)
{
    char *p1 = &(w[w1][0]);
    char *p2 = &(w[w2][0]);
    while (*p1)
    {
        if ((*p1 == letter && *p2 != letter) || (*p2 == letter && *p1 != letter)) return false;
        p1++;
        p2++;
    }
    return true;
}

int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);
    //freopen("B.in", "r", stdin);
    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt)
    {
        scanf("%i %i", &n, &m);
        for(int i=0; i<n; ++i) scanf("%s", w[i]);
        printf("Case #%i:", tt);
        for(int i=0; i<m; ++i)
        {
            scanf("%s", s);
            int best = 0;
            int best_i = 0;
            for(int r=0; r<n; ++r)
            {
                int tmp = 0;
                int k = strlen(w[r]);
                for(int z=0; z<n; ++z)
                    nn[z] = (strlen(w[z]) == k);

                for(int j=0; j<26; ++j)
                {
                    bool ok = false;
                    for(int z=0; z<n; ++z) if (nn[z] && has(z, s[j])) { ok= true; break; }

                    if (ok)
                    {                        
                        if (has(r, s[j]))
                        {
                            for(int z=0; z<n; ++z) if (nn[z] && same(z, r, s[j])) nn[z] = true; else nn[z] = false;
                        }
                        else
                        {
                            tmp++;
                            for(int z=0; z<n; ++z) if (nn[z])
                                nn[z] = !has(z, s[j]);
                        }
                    }
                }
                if (tmp > best) best = tmp, best_i = r;
            }
            printf(" %s", w[best_i]);
        }
        printf("\n");
    }
}