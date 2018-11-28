#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(){

    int ct=0;
    int g[1000];
    int next[1000];
    int sum[1000];
    
    int R,K,N,T;
    
    scanf("%d",&T);    
    
    while(ct<T){
        scanf("%d %d %d",&R,&K,&N);
        
        int st=0;
        for(int i=0; i<N; i++){
            scanf("%d",&g[i]);
            st+=g[i];
        }
        vector<int> v;
        for(int i=0; i<2*N; i++){
            v.push_back(g[i%N]);
        }
        memset(next,0,sizeof(next));
        memset(sum,0,sizeof(sum));
        
        int ok=1;
        int b=-1;
        
        for(int i=0; i<N ; i++){
            int s=0;
            for(int k=0; k<N  ; k++){
                int j=i+k;
                if(s+v[j]>K){
                    if(!next[i]){
                        next[i]=j%N;
                    }
                    else if(ok){
                        b=i;
                        ok=0;
                    }
                    break;
                }
                s+=v[j];
            }
            sum[i]=s;
        }
        if(st<=K) b=0;
        
        int s=0;
        int sacum=0;
        int ct1=0;
        int ok2=0;
        while(s!=b){
            sacum+=sum[s];
            s=next[s];
            ct1++;
            if(ct1==R){
                ok2=1;
                break;
            }
        }
        
        printf("Case #%d: ",ct+1);
        
        if(ok2){
            cout<<sacum<<endl;
        }
        else{
            R-=ct1;
            
            int sumab=0;
            int ctb=0;
            do{
                sumab+=sum[s];
                s=next[s];
                ctb++;
            }while(s!=b);
            
            //cout<<"hey"<<endl;
            sacum+=(R/ctb)*sumab;
            
            R=R%ctb;

            while(R--){
                sacum+=sum[s];
                s=next[s];
            }
            cout<<sacum<<endl;
            
        }
        
        
        ct++;
    }
    
    
}
