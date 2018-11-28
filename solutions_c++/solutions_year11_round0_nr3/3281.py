#include<stdio.h>
#include<math.h>

int add(int a,int b) {
    if(a==0) return b;
    int c=0;
    int pow=1;
    while(a!=0 && b!=0){
        if((a%2)^(b%2))
            c+=pow;
        pow*=2;
        a/=2;
        b/=2;
    }
    return c;
}

int main() {
    freopen("D://test.txt","r",stdin);
    freopen("D://testout.txt","w",stdout);
    int t;
    int c[20];
    scanf("%d\n",&t);
    for(int i=0;i<t;i++) {
        int n;
        int max=0;
        scanf("%d",&n);
        for(int j=0;j<n;j++) //{
            scanf("%d",&c[j]); //printf("%d ",c[j]);}
        //printf("\n");
        int ans=c[0];
        for(int j=1;j<n;j++) ans^=c[j];
        if(ans!=0) printf("Case #%d: NO\n",i+1);
        else {
        int npow=pow(2,n)/2;
        for(int j=1;j<npow;j++) {
            int temp=j,a=0,b=0;
            for(int k=0;k<n;k++) {
                if(temp%2)
                    a^=c[k];
                else
                    b^=c[k];
                temp/=2;
            }
            if(a==b && a>0 && b>0) {
                temp=j,a=0,b=0;
                for(int k=0;k<n;k++) {
                    if(temp%2)
                        a+=c[k];
                    else
                        b+=c[k];
                    temp/=2;
                }
                int tpMax=a>b? a:b;
                if(tpMax>max) //{
                    max=tpMax; //printf("Yeah = %d\n",j);}
            }
        }
        //if(max==0)
        //    printf("Case #%d: NO\n",i+1);
        //else
            printf("Case #%d: %d\n",i+1,max);
        }
    }
    fclose(stdout);
    fclose(stdin);
    return 0;
}
