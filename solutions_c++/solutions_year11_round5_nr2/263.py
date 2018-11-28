#include <cstring>
#include <cstdio>

int mark[100001],origin[100001],lab[100001];
int n,m,x;

bool judge(int mid)
{
     int start=0,cnt=0;
     while (1){
           while (mark[start]==0 && start<10000) start++;
           cnt++;
           if (start==10000) break;
           for (int i=start;i<=start+mid-1;i++) 
               if (!mark[i]) {lab[start]--;if (lab[start]<0) return 0;else break;}else{
                   mark[i]--;
                   //printf("%d %d\n",i,cnt);
               }
           lab[start+mid]++;         
     }
     return 1;
}

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&n);
    for (int Case=1;Case<=n;Case++){
        scanf("%d",&m);
        printf("Case #%d: ",Case);
        if (m==0) {printf("%d\n",0);continue;}
        memset(origin,0,sizeof(origin));
        for (int i=1;i<=m;i++){
            scanf("%d",&x);
            origin[x]++;
        }
        int st=1,ed=m;
        while (st<ed){
              int mid=(st+ed)/2;
              for (int i=1;i<=10000;i++) mark[i]=origin[i];
              memset(lab,0,sizeof(lab));
              //printf("\n!!!!! %d !!!!!\n",mid);
              if (judge(mid)) st=mid+1;else ed=mid;
        }
        for (int i=1;i<=10000;i++) mark[i]=origin[i];
        memset(lab,0,sizeof(lab));
        if (judge(st)) printf("%d\n",st);else printf("%d\n",st-1);
    }
}
