#include<stdio.h>
#include<string.h>
#include<map>
using namespace std;
int n,m,ans;
map <int,int> hash;
int main(){
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int cc=0,ca,i,j,t,a;
    int g,w;
    scanf("%d",&ca);
    while (ca--){
        cc++;
        printf("Case #%d: ",cc);
        scanf("%d%d",&n,&m);
        g=1;w=1;
        while (g<=n) {g=g*10;w++;}
        g=g/10;w--;
        ans=0;
        if (g==0) {printf("%d\n",ans);continue;}
        for (i=n;i<m;i++){
            t=i;
            hash.clear();
            for (j=1;j<w;j++){
                a=t%10;
                t=t/10+a*g;
                if (!hash[t]&&t<=m&&t>i) {hash[t]=1;ans++;}
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}
