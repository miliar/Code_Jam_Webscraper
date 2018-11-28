#include <iostream>
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tt,i;
    scanf("%d",&tt);
    for(i=0;i<tt;i++) {
        int n,s,p,t[200]={0},sp[200]={0};
        int j, cnt=0;
        scanf("%d %d %d",&n,&s,&p);
        for(j=0;j<n;j++) {
            scanf("%d",&t[j]);
            sp[j]=(t[j]+2)/3;
            if(t[j]<29 && t[j]>1)
            if(t[j]<(p*3-2) && t[j]>(p*3-5) && s>0) {
                sp[j]++;
                s--;
            }
        }
        for(j=0;j<n;j++) {
            if(sp[j]>=p) cnt++;
        }
        printf("Case #%d: %d\n",i+1,cnt);
    }
    return 0;
}
