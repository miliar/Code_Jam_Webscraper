#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    //freopen("B-large.in","r",stdin);
   //freopen("t.txt","w",stdout);
    int cas;int tem;
    int n,s,c;
    scanf("%d",&cas);
    for(int i=1;i<=cas;i++)
    {
        int sup=0;int count=0;
        scanf("%d%d%d",&n,&s,&c);
        int low1=c*3-2;
        int low2=c*3-4;
        if(c==1) low2=0x7ffffff;
        if(c==0) {low1=0;low2=0x7ffffff;}
        for(int j=0;j<n;j++)
        {
            scanf("%d",&tem);
            if(tem>=low1) count++;
            else if(tem>=low2) sup++;
        }
        tem=sup<s?sup:s;
        count+=tem;
        printf("Case #%d: %d\n",i,count);
    }
    return 0;
}
