#include<cstdio>
#include<cstring>
int t,ca,i,j,tmp,a,b;
long long tt,ans;
bool f[12210000];
int main(){
    //freopen("c.in","r",stdin);
    //freopen("c.out","w",stdout);
    scanf("%d",&t);
    for (ca=1;ca<=t;ca++){
        memset(f,0,sizeof(f));
        ans=0;
        scanf("%d%d",&a,&b);
        for (i=a;i<=b;i++) if (!f[i]&&i>9){
            tt=0; j=i;
            tmp=1; while (tmp*10<=i) tmp=tmp*10;
            
            do{
               if (j<=b&&j>=a) {tt++; f[j]=true;}
               j=j/10+(j%10)*tmp;
               }
            while (j!=i);
            ans+=tt*(tt-1)/2;
        }
        printf("Case #%d: %I64d\n",ca,ans);
    }
    return 0;
}
