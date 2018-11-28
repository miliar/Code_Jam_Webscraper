#include<cstdio>
#define MX 10002
int d[MX],l[MX],lhave[MX],touched[MX];
inline int minn(int aa,int bb) {
    if (aa<bb) return aa; else return bb;
}
inline int maxx(int aa,int bb) {
    if (aa>bb) return aa; else return bb;
}
int main() {
    int i,j,t,tt,n,dest,ans;
    scanf("%d",&tt);
    for(t=1;t<=tt;t++) {
        scanf("%d",&n);
        for(i=0;i<n;i++) {
            scanf("%d",&d[i]);
            scanf("%d",&l[i]);
            lhave[i] = 0;
            touched[i] = 0;
        }
        scanf("%d",&dest);
        d[n] = dest;
        l[n] = 0;
        lhave[n] = 0;
        touched[n] = 0;
        n++;
        lhave[0] = minn(d[0],l[0]);
        touched[0] = 1;
        for(i=0;i<n;i++) {
            if(!touched[i]) {
                continue;
            }
            for(j=i+1;j<n;j++) {
                if(d[j]>d[i]+lhave[i]) {
                    break;
                }else{
                    lhave[j] = maxx(lhave[j],minn(l[j],d[j]-d[i]));
                    touched[j] = 1;
                }
            }
        }
        
        printf("Case #%d: ",t);
        if(touched[n-1]) {
            printf("YES\n");
        }else{
            printf("NO\n");
        }
    }    
}
