#include <cstdio>
#include <algorithm>
const int inf = 0x3fffffff;

int snum, qnum;
char* slist[100], sname[100][104], cur[104];
int dp[100];
inline bool cmp(char *x, char *y)
{
    while(*x == *y&&*y&&*x)x++, y++;
    return *x < *y;
}
inline int cmpx(char *x, char *y)
{
    while(*x == *y&&*y&&*x)x++, y++;
    return *x - *y;
}
int main()
{
    int i, j, b, e, m, tmp;
    int casenum, casei;
    scanf("%d", &casenum);
    for(casei=1;casei<=casenum;casei++)
    {
        scanf("%d", &snum);gets(cur); //get the \n of this line
        for(i=0;i<snum;i++)
        {
            fgets(sname[i], 103, stdin);
            slist[i] = sname[i];
			dp[i] = 0;
        }
        std::sort(slist, slist+snum, cmp);
	/*	for(i=0;i<snum;i++)
			printf("%s", slist[i]);*/
        scanf("%d", &qnum);gets(cur);
        for(i=0;i<qnum;i++)
        {
            fgets(cur, 103, stdin);
            for(b=0, e=snum;;)
            {
                m = (b+e)>>1;
                tmp = cmpx(cur, slist[m]);
                if(tmp>0)b = m;
                else if(tmp<0)e=m;
                else break;
            }
			for(tmp = inf, j = m+1;j = j>=snum?j-snum:j, j != m;j++)
            {
                if(tmp > dp[j]+1)
                    tmp = dp[j] + 1;
            }
            dp[m] = tmp;
        }
        for(tmp = inf, i=0;i<snum;i++)
            if(tmp > dp[i])
                tmp = dp[i];
        printf("Case #%d: %d\n", casei, tmp);
    }
}
