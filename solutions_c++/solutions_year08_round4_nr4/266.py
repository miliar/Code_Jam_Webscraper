#include<stdio.h>
#include<memory.h>
#include<set>
#include<map>
#include<vector>
#include<string.h>
#include<string>
#include<iostream>
#include<algorithm>
using namespace std;

int n1,i1,xiao,now,k,j,i,p;
int a[17];
char s[50010],s1[50010];

int main()
{
    scanf("%d",&n1);
    for(i1=1;i1<=n1;i1++)
    {
        scanf("%d",&k);
        for(i=0;i<k;i++)
            a[i]=i;
        scanf("%s",&s);
        p=strlen(s);
        xiao=p;
        do
        {
            for(i=0;i<p;i+=k)
            {
                for(j=0;j<k;j++)
                {
                    s1[i+j]=s[i+a[j]];
                }
            }
            now=1;
            for(i=1;i<p;i++)
            {
                if(s1[i]!=s1[i-1])
                    now++;
            }
            if(now<xiao)
                xiao=now;
        }while(next_permutation(a,a+k));    
        printf("Case #%d: %d\n",i1,xiao);
    }    
    return 0;
}
