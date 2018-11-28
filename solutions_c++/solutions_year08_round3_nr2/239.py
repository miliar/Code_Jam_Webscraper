#include <cstdio>
#include <cstring>
const int inf = 0x3fffffff;
int len;
char seq[64];
inline int check(long long num)
{
    if( num%2==0 || num%3==0 || num%5==0 || num%7==0)
        return 1;
    else
        return 0;
}
inline long long str2int(int b, int e)
{
    long long res=0;
    for(int i=b;i<=e;i++)
        res=res*10+seq[i]-'0';
    return res;
}
long count(long long num, int index)
{
    int i, cc=0;
    long long tmp;
    if(index>=len)
        return check(num);
    for(i=index;i<len;i++)
    {
        tmp=str2int(index, i);
        cc+=count(tmp+num, i+1);
        if(index!=0)
            cc+=count(num-tmp, i+1);
    }
    return cc;
}
int main()
{
    int i, j, tmp;
    int n;

    int casenum, casei;
    scanf("%d", &casenum);
    for(casei=1;casei<=casenum;casei++)
    {
        scanf("%s", seq);
        len = strlen(seq);
        printf("Case #%d: %d\n", casei, count(0, 0));
    }
}
