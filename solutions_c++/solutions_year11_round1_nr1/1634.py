#include <cstdio>
#include <cstring>

int T;
int n,d,g;

void work(int Case)
{
     if (d==100 && g==100) {printf("Case #%d: Possible\n",Case);return;}
     if (g==100){printf("Case #%d: Broken\n",Case);return;}
     if (d==0 && g==0){printf("Case #%d: Possible\n",Case);return;}
     if (g==0){printf("Case #%d: Broken\n",Case);return;}
     if (n<100){
        for (int i=1;i<=n;i++) if (i*d%100==0){printf("Case #%d: Possible\n",Case);return;}
        printf("Case #%d: Broken\n",Case);
     }else printf("Case #%d: Possible\n",Case); 
     
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);
    for (int Case=1;Case<=T;Case++){
        scanf("%d%d%d",&n,&d,&g);
        work(Case);
    }
}
