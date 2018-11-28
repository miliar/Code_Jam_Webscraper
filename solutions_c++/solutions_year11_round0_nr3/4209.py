#include<iostream>
#include<algorithm>
using namespace std;


int a[1020];
int main(){
    int Cas;
    freopen("C-large.in","r",stdin);
    freopen("Cout2.txt","w",stdout);
    scanf("%d",&Cas);

    int cas=0;
    while(Cas--){
        printf("Case #%d: ",++cas);
        int n;
        scanf("%d",&n);
        int x=0,sum=0;
        for(int i=0;i<n;++i){
            scanf("%d",a+i);
            x^=a[i];
            sum+=a[i];
        }
        if(x){
            puts("NO");
        }else{
            sort(a,a+n);
            printf("%d\n",sum-a[0]);
        }
    }
    return 0;
}
            
            
            
    
