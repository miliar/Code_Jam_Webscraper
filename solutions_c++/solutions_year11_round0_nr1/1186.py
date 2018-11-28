#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
int n;
void init()
{

    int O=1,B=1,temp,lo=0,lb=0;
    int time1=0,time2=0;
    char c[3];
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        scanf("%s%d",c,&temp);
        int numo=0,numb=0;
        if(c[0]=='O')
        {
            time1=max(time1+abs(temp-O)+1,time2+1);
            O=temp;
        }
        else
        {
          time2=max(time2+abs(temp-B)+1,time1+1);
          B=temp;
        }
        //cout<<time1<<" "<<time2<<endl;
    }
    printf("%d\n",max(time1,time2));
}
int main()
{
    int Case;
   freopen("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\A-large.in","r",stdin);
    freopen("b.out", "w", stdout);
    scanf("%d",&Case);
    for(int i=1;i<=Case;i++)
    {
        printf("Case #%d: ",i);
        init();
    }
return 0;
}
