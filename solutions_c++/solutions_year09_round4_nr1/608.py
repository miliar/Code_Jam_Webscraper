#include<iostream>
int a[1000];
main(){
    int n,i,j,ti,tt,cnt,r;
    char s[1000];
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);
    scanf("%d",&tt);
    for(ti=1;ti<=tt;ti++){
        cnt=0;
        scanf("%d",&n);
        for(i=0;i<n;i++){
            scanf("%s",s);
            for(a[i]=n;a[i]>0;a[i]--){
                if(s[a[i]-1]=='1'){
                    break;
                }
            }
        }
        for(i=0;i<n;i++){
            if(a[i]>i+1){
                for(j=i+1;j<n;j++){
                    if(a[j]<=i+1){
                        break;
                    }
                }
                for(;j>=i+1;j--){
                    r=a[j];
                    a[j]=a[j-1];
                    a[j-1]=r;
                    cnt++;
                }
            }
        }
        printf("Case #%d: %d\n",ti,cnt);
    }
}
