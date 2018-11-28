#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;
int max(int i,int j) {return i>=j?i:j;}
int main()
{
    int tc,n;
    int curtime[2], curpos[2];
    //freopen("A-large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    scanf("%d", &tc);
    for (int cas=1;cas<=tc;++cas)
    {
        curtime[0]=curtime[1]=0;
        curpos[0]=curpos[1]=1;
        scanf("%d", &n);
        for (int i=0;i<n;++i)
        {
            char s[10];
            int pos, idx;
            scanf("%s%d", s, &pos);
            if (*s == 'O') idx=0;
            else idx=1;
            curtime[idx] = max(curtime[idx] + abs(curpos[idx]-pos), curtime[idx^1])+1;
            curpos[idx] = pos;
        }
        printf("Case #%d: %d\n", cas, max(curtime[0],curtime[1]));
    }
    return 0;
}
