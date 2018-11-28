#include <cstdio>

int l[2000],r[2000],n,test,tst,ans;

int main(){
//    freopen("input.txt","r",stdin);
//    freopen("output.txt","w",stdout);
//        freopen("A-small-attempt0.in","r",stdin);
//    freopen("A-small-attempt0.out","w",stdout);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    scanf("%d",&tst);
    for(int test=1;test<=tst;test++){
        ans = 0;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%d %d",&l[i],&r[i]);
        for(int i=0;i<n-1;i++)
            for(int j=i+1;j<n;j++)
                if( (l[i]-l[j])*(r[i]-r[j])<0 )
                    ans++;
        printf("Case #%d: %d\n",test,ans);
    }
}
