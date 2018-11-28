#include <stdio.h>
#include <string.h>
int cnt = 0;
char *strWel="welcome to code jam";
int lenObj, lenWel;
char strObj[510];
void search(int idx1, int idx2)
{
    if (idx2 >= lenWel)
    {
        cnt ++;
        return;
    }
    if (idx1 >=lenObj)
        return;
    if (lenObj - idx1 < lenWel - idx2)
        return;
    if (strObj[idx1] == strWel[idx2])
        search(idx1+1, idx2+1);
    search(idx1 +1, idx2);
};
int main()
{
    int T;
    int i,j;

    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);

    lenWel = strlen(strWel);
    scanf("%d",&T);
    gets(strObj);
    for (i = 1; i <=T; i ++)
    {
        gets(strObj);
        cnt = 0;
        lenObj = strlen(strObj);
        search(0,0);
        cnt %= 10000;
        printf("Case #%d: %04d\n", i,cnt);
    }
    return 0;
}
