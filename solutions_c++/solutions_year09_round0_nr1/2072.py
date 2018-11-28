#include <iostream>
#include <algorithm>
#include <stdio.h>
using namespace std;
const int N = 10000;
int L,D,n;
char s[N][15];
char t[N];

bool in(char* a,char *b)
{
    int ptr = 0,right=0;
    int i;
    for(i=0;i<L;i++)
    {
        if(a[ptr]=='(')
        {
            for(++ptr;a[ptr]!=')';ptr++)
            {
                if(a[ptr]==b[i])break;
            }
            if(a[ptr]==')')return 0;
            for(;a[ptr]!=')';ptr++);
            ptr++;
        }
        else
        {
            if(a[ptr]!=b[i])return 0;
            ptr++;
        }
    }
    return 1;
}
int main()
{
    int i,j,k;
    freopen("t1.in","r",stdin);
    freopen("t1.out","w",stdout);
    scanf("%d%d%d",&L,&D,&n);
    for(i=0;i<D;i++)
    {
        scanf("%s",s[i]);
    }
    for(i=0;i<n;i++)
    {
        k = 0;
        scanf("%s",t);
        for(j=0;j<D;j++)
            if(in(t,s[j]))k++;
        printf("Case #%d: %d\n",i+1,k);
    }
    return 0;
}
