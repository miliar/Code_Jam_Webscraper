#include <cstdio>
#include <cstring>

using namespace std;

#define MAX_SIZE 2000000

char    combo[255][255];
bool    opp[255][255];
char    s[MAX_SIZE];
char    a[MAX_SIZE];
int     was[255];
int     size;    
int     n, c, d, tc;

void clear_was()
{
    for(int i='A'; i <= 'Z'; ++i) was[i] = 0;
    size = 0;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%i", &tc);
    for(int t=1; t<=tc; ++t)
    {
        memset(combo, 0, sizeof(combo));
        memset(opp, 0, sizeof(opp));

        scanf("%i", &c);
        for(int i=0; i<c; ++i)
        {
            scanf("%s", s);
            combo[s[0]][s[1]] = s[2];
            combo[s[1]][s[0]] = s[2];
        }
        scanf("%i", &d);
        for(int i=0; i<d; ++i)
        {
            scanf("%s", s);
            opp[s[0]][s[1]] = true;
            opp[s[1]][s[0]] = true;
        }

        scanf("%i %s", &n, s);
        char *p = &s[0];
        clear_was();
        size = 0;

        while (*p)
        {
            
            a[size]=0;            
            /*
            printf("a=%s p=%c ", a, *p);
            for(char q='A'; q<='Z'; ++q) if (was[q]) printf("<%c> ", q);
            printf("\n");
            */
            if (size > 0)
            { 
                if (combo[a[size-1]][*p]) 
                { 
                    was[a[size-1]]--;
                    a[size-1] = combo[a[size-1]][*p]; 
                    was[a[size-1]]++;
                    p++; 
                    continue; 
                }                

                bool ok = false;
                for(char q='A'; !ok && q<='Z'; ++q) if (was[q] && opp[q][*p]) ok = true;
                if (ok) { clear_was(); p++; continue; }
                
            }
            a[size++] = *p;
            was[*p]++;
            p++;
        }
        printf("Case #%i: [", t);
        for(int i=0; i<size-1; ++i) printf("%c, ", a[i]);
        if (size) printf("%c", a[size-1]);
        printf("]\n");
        
    }
    return 0;
}