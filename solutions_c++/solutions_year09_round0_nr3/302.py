#include<iostream>
#include<cstring>
#define MOD 10000
using namespace std;
char pat[]={" welcome to code jam"};
char s[600];
int cnt[30];
int main()
{  int N,CASE,i,j;
freopen("C.in","r",stdin);
      freopen("C.out","w",stdout);
    scanf("%d",&N);
     gets(s);
     for(CASE=1;CASE<=N;++CASE)
    {   printf("Case #%d: ",CASE);
       gets(s);
        memset(cnt,0,sizeof(cnt));
        cnt[0]=1;
        for(i=0;s[i];++i)
          for(j=19;j>0;--j)
              if(s[i]==pat[j])
                 cnt[j]=(cnt[j]+cnt[j-1])%MOD;
        
         printf("%04d\n",cnt[19]);
    
    }
}
