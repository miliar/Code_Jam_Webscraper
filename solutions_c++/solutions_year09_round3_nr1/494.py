#include<cstdio>
#include<string.h>

long long int n,ch[130],base,tt[130];
bool zero;
long long int ans;
char tmp[105];

int main(){
    scanf("%d",&n); gets(tmp);
    for (int t=1;t<=n;++t){
        memset(tt,0,sizeof(tt)); zero=0;
        for (int i=0;i<=129;++i) ch[i]=(long long int)-1;
        ans=0; base=2;
        gets(tmp);
        long long int k=strlen(tmp);
        ch[tmp[0]]=1; tt[0]=1;
        for (int i=1;i<k;++i){
            if (ch[tmp[i]]==-1){
               if (!zero){
                  ch[tmp[i]]=0; zero=1; tt[i]=0;
               }
               else{
                    ch[tmp[i]]=base; tt[i]=base; ++base;
               }
            }
            else tt[i]=ch[tmp[i]];
        }
        
        long long int p=1;
        for (int i=k-1;i>=0;--i){
            ans+=p*tt[i]; p*=base;
        }
        printf("Case #%d: %I64d\n",t,ans);
        
    }
    return 0;
}
