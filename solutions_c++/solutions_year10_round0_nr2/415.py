#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>

using namespace std;


int gcd(int a, int b){
    if(b==0)
        return a;
    return  gcd(b,a%b);
}

int main(){
    int t,v[1010];
    scanf("%d",&t);
    for(int c=1;c<=t;c++){
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%d",&v[i]);
        }
        sort(v,v+n);
        int maxT;
        int y=0;
        maxT= gcd(v[0],v[1]);
        for(int i=2;i<n;i++)
            maxT=gcd(maxT,v[i]);
        
        int g;
        if(n==2)
            g=v[1]-v[0];
        else{
             g = gcd(v[1]-v[0],v[2]-v[1]);
             for(int i=3;i<n;i++)
                g=gcd(g,v[i]-v[i-1]); 
        }
        y = g-v[0]%g;  
        if(maxT>=g)
            y=0;
        /*
        for(int i=0;i<n-1;i++){
            int T=v[i+1]-v[i];
            if(T==0 || T<maxT)continue;
             //  printf("aqui\n");
            int ref = v[0]%T;
            //printf("resto de %d por %d = %d\n",v[0],T,v[0]%T);
            
            int j;
            for(j=1;j<n;j++){
                //printf("resto de %d por %d = %d\n",v[j],T,v[j]%T);
                if(v[j]%T!=ref)
                    break;
            }
            if(j==n){
               // printf("Candidato T=%d\n",T);
                //T eh candidato.
                int cand;
                if(v[0]<T)
                    cand=T-v[0];
                else cand=T-ref;
                if(T>maxT || cand<y){
                    y=cand;          
                    maxT=T;
                }   
            }
        }   
*/
        
        
             
        printf("Case #%d: %d\n",c,y);
    }
    return 0;
}
