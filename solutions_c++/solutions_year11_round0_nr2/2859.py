#include <cstdio>
#include <cstring>

void can(char s[])
{
    int i = 0;
    while (s[i])
    {
        s[i] = s[i]-'A';
        i++;
    }
}

void solve()
{
    int c, d, n;
    char M['Z'-'A'+1]['Z'-'A'+1];
    bool D['Z'-'A'+1]['Z'-'A'+1];
    
    for (char a = 'A'; a <= 'Z'; a++)
        for (char b = 'A'; b <= 'Z'; b++)
        {
            M[a-'A'][b-'A'] = -1;
            D[a-'A'][b-'A'] = false;
        }
    
    scanf("%d", &c);
    for (int i = 0; i < c; i++)
    {
        char v[4];
        scanf("%s", v);
        //printf("%s\n", v);
        can(v);
        M[v[0]][v[1]] = v[2];
        M[v[1]][v[0]] = v[2];
    }
    
    scanf("%d", &d);
    for (int i = 0; i < d; i++)
    {
        char v[3];
        scanf("%s", v);
        //printf("%s\n", v);
        can(v);
        D[v[0]][v[1]] = D[v[1]][v[0]] = true;
    }
    
    char s[100];
    int l = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf(" %c", &s[l]);
        s[l] -= 'A';
        l++;
        while (l >= 2 && M[s[l-1]][s[l-2]] >= 0)
        {
            //printf("Trocou %c e %c por %c.\n", s[l-2]+'A', s[l-1]+'A', M[s[l-1]][s[l-2]]+'A');
            s[l-2] = M[s[l-1]][s[l-2]];
            l--;
        }
        for (int a = 0; a < l; a++)
            for (int b = a+1; b < l; b++)
                if (D[s[a]][s[b]])
                    l = 0;
    }
    
    if (l == 0)
    {
        printf("[]\n");
        return;
    }
    
    printf("[%c", s[0]+'A');
    for (int i = 1; i < l; i++)
        printf(", %c", s[i]+'A');
    printf("]\n");
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++)
    {
        printf("Case #%d: ", t);
        solve();
    }
    
    return 0;
}

