#include<stdio.h>
#include<algorithm>

using namespace std;

int in[5];

int sol[5];

int gcd(int a,int b){
    if(a%b==0) return b;
    else return gcd(b,a%b);
}

int main(){
    
    freopen("B-small-attempt3.in","r",stdin);
    freopen("B-small.out","w",stdout);
    
    int C;
    int n,a,b;
    scanf("%d",&C);
    for(int c=1;c<=C;c++){
        scanf("%d",&n);
        for(int i=0;i<n;i++) scanf("%d",&in[i]);
        sort(in,in+n);
        
        if(n==2){
            if(in[0]==in[1]) printf("Case #%d: 0\n",c);
            else {
                a=in[1]-in[0];
                b=in[0]%a;
                printf("Case #%d: %d\n",c,(a-b)%a);
            }
        } else {
            if(in[0]==in[1] && in[1]==in[2]) printf("Case #%d: 0\n",c);
            else if(in[0]==in[1]){
                a=in[2]-in[1];
                b=in[1]%a;
                printf("Case #%d: %d\n",c,(a-b)%a);
            } else if(in[1]==in[2]){
                a=in[1]-in[0];
                b=in[0]%a;
                printf("Case #%d: %d\n",c,(a-b)%a);
            } else {
                a=gcd(in[1]-in[0],in[2]-in[1]);
                b=in[0]%a;
                printf("Case #%d: %d\n",c,(a-b)%a);
            }   
        } 
    }
    
return 0;
}  
