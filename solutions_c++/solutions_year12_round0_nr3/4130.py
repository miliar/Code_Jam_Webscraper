#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

bool renum(int start, int end)
{
    int cmp[10]={0};
    int i = start;
    char s1[50],s2[50];
    //判断位数与数字是否一样
    while(i!=0)
    {
        cmp[i%10]++;
        i/=10;
    }
    i = end;
    while(i!=0)
    {
        if(cmp[i%10]==0)
            return false;
        else
            cmp[i%10]--;
        i/=10;
    }
    itoa(start,s1,10);
    itoa(end,s2,10);
    int len1 = strlen(s1);
    for(i=0;i<len1;i++)
    {
        int flag = 0;
        if(s1[0]==s2[i])
        {
            flag = 1;
            int j,k;
            for(j=i,k=0;j<len1;j++,k++)
            {
                if(s1[k]!=s2[j])
                {
                    flag = 0;
                    break;
                }
            }
            for(j=0;k<len1&&flag;j++,k++)
            {
                if(s1[k]!=s2[j])
                {
                    flag = 0;
                    break;
                }
            }
        }
        if(flag ==1)
            return true;
    }
    return false;
    //return true;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        int t = 1;
        while(n--)
        {
            int start,end,i,j;
            int sum = 0;
            scanf("%d%d",&start,&end);
            for(i=start;i<=end;i++)
            {
                for(j=i+1;j<=end;j++)
                    if(true == renum(i,j))
                    {
                        sum++;
                        //break;
                    }
            }
            printf("Case #%d: %d\n",t++,sum);
        }
    }
    return 0;
}
