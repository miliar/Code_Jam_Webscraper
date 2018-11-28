#include <cstdio>
#include <cstring>
using namespace std;

const char* pat = "welcome to code jam";
char text[512];
int table[512][32];

int calc(int l1, int l2)
{
    if(!pat[l2])    
        return 1;
    else if(!text[l1])
        return 0;
    else if(table[l1][l2])
        return table[l1][l2] - 1;
    else
        return (table[l1][l2] = (calc(l1 + 1, l2) + ((text[l1] == pat[l2])? calc(l1 + 1, l2 + 1): 0)) % 10000)++;
}

int main()
{
    int T;
    scanf("%d", &T);
    fgets(text, sizeof(text), stdin);
    for(int t = 1; t <= T; t++)
    {
        fgets(text, sizeof(text), stdin);
        memset(table, 0, sizeof(table));
        printf("Case #%d: %04d\n", t, calc(0, 0));                
    }
    return 0;    
}
