#include<iostream>
#include<stdio.h>
#include<map>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<string>
#include<math.h>
using namespace std;


int main()
{
    freopen("C:\\Users\\Administrator\\Desktop\\B-small-attempt0.in","r",stdin);
    freopen("C:\\Users\\Administrator\\Desktop\\out","w",stdout);
    int t,k,i,j,T,L,N,C,a[1010],pre,b[1010],min,ans,t1,tmp;
    scanf("%d",&T);
    for(k=1;k<=T;k++) {
        scanf("%d%d%d%d",&L,&t,&N,&C);
        for(i=0;i<C;i++) scanf("%d",&a[i]);
        printf("Case #%d: ",k);
        b[0]=pre=0;
        for(i=1;i<=N;i++) {
            b[i]=b[i-1]+a[pre];
            pre=(pre+1)%C;
        }
        if(L==0) printf("%d\n",2*b[N]);
        else if(L==1) {
            min=2*b[N];
            for(i=0;i<N;i++) {
                if(2*b[i+1]>=t) {
                    if(t<=2*b[i]) ans=2*b[N]-b[i+1]+b[i];
                    else ans=2*b[N]-(b[i+1]-b[i]-(t-2*b[i])/2);
                    if(ans<min) min=ans;
                }
            }
            printf("%d\n",min);
        }
        else {
            min=2*b[N];
            for(i=0;i<N;i++) {
                if(2*b[i+1]>=t) {
                    if(t<=2*b[i]) t1=b[i+1]+b[i];
                    else t1=2*b[i+1]-(b[i+1]-b[i]-(t-2*b[i])/2);
                    for(j=i+1;j<N;j++) {
                        if(2*(b[j+1]-b[i+1])+t1>=t) {
                            if(t<=2*(b[j]-b[i+1])+t1) tmp=b[j+1]-b[j];
                            else tmp=(b[j+1]-b[j]-(t-2*(b[j]-b[i+1])-t1)/2);
                        }
                        if(t1+2*b[N]-2*b[i+1]-tmp<min) min=t1+2*b[N]-2*b[i+1]-tmp;
                    }
                }
            }
            printf("%d\n",min);
        }
        
    }
    //system("pause");
    return 0;
}
