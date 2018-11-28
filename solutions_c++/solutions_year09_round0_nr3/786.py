#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
using namespace std;
char t[502];
char s[25]="welcome to code jam";
int a[19];
int main()
{    
     freopen("C-large.in","r",stdin);
     freopen("C-large.out","w",stdout);
     int p=strlen(s);
    // cout<<p<<endl;
     int n;
     scanf("%d",&n);
     gets(t);
     for(int i=1;i<=n;i++)
     {
             gets(t);
             int q=strlen(t);
             memset(a,0,sizeof(a));
             if(t[q-1]=='m')a[18]=1;
             for(int j=q-2;j>=0;j--)
             {
                     for(int k=0;k<18;k++)
                     {
                     if(t[j]==s[k])
                     {
                     a[k]+=a[k+1];
                     a[k]%=10000;
                    // cout<<k<<" "<<a[k]<<endl;
                     }
                     
                     }
                     if(t[j]=='m')
                     {
                     a[18]++;
                     a[18]%=10000;
                     }
                     
             }
             printf("Case #%d: ",i);
             int re=a[0]%10000;
             if(re<1000)
             {
                        if(re>99)printf("0");
                        else if(re>9)printf("00");
                        else printf("000");
             }
             printf("%d\n",re);
     }
   // system("pause");
    return 0;
}
