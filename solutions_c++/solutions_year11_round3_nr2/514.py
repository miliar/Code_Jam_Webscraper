#include<iostream>

using namespace std;

long long d[10000];

int main(){
    freopen("B-small-attempt1.in","r",stdin);
    freopen("x.out","w",stdout);
    int tc;
    cin>>tc;
    for(int q=1;q<=tc;q++){
        long long l,t,n,c,a;
        cin>>l>>t>>n>>c;
        for(int i=0;i<c;i++){
            cin>>a;
            d[i]=a;
        }    
        long long res=-1u/2;
        long long sum=0;
        for(int i=0;i<n;i++)
            sum+=d[i%c]*2;
        if(l==0)
            res=sum;
        else if(l==1){
            for(int i=0;i<n;i++){
                long long r=0;
                for(int j=0;j<n;j++)
                    if(j!=i)
                        r+=d[j%c]*2;
                    else{
                        long long e=max(2*d[i%c]-max(t-r,0ll),0ll);
                        r+=2*d[i%c]-e;
                        r+=e/2;
                    }
                res=min(res,r);
            }
        }
        else if(l==2){
            for(int i=0;i<n;i++)
                for(int j=i+1;j<n;j++){
                    long long r=0;
                    for(int k=0;k<n;k++){
                        if(k<i)
                            r+=d[k%c]*2;
                        else if(k==i){
                            long long e=max(2*d[i%c]-max(t-r,0ll),0ll);
                            r+=2*d[i%c]-e;
                            r+=e/2;
                        }
                        else if(k<j)
                            r+=d[k%c]*2;
                        else if(k==j){
                            long long e=max(2*d[j%c]-max(t-r,0ll),0ll);
                            r+=2*d[j%c]-e;
                            r+=e/2;
                        }
                        else
                            r+=d[k%c]*2;    
                    }
                    res=min(res,r);
                }
        }
        printf("Case #%d: ",q);
        cout<<res<<endl;
    }    
    return 0;
}
