#include <vector>
#include <string>
#include <iostream>

using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);

    int N, S, Q;
    int X,Y;
    int ax;
    string s;
    
    cin>>N;
    
    vector<string> v1;
    vector<string> v2;
    int ax2,ans;
    
    for(int i=0;i<N;i++){
        cin>>S;
        
        v1.clear(); v1.resize(S);
        
        getline(cin,s);
        for(int j=0;j<S;j++) getline(cin,v1[j]);
        
        
        cin>>Q;
        getline(cin,s);
        
        v2.clear(); v2.resize(Q);
        
        for(int j=0;j<Q;j++) getline(cin,v2[j]);
        
        ax=0; ans=0;
        while(ax<Q){
            if(ax!=0) ans++;
            vector<int> f(S,2001);
            
            int cont=0;
            
            for(int j=ax;j<Q;j++){
                for(int k=0;k<S;k++){
                    if(v1[k]==v2[j] && f[k]==2001){
                        f[k]=j;
                        cont++;
                    }
                }
                if(cont==S) break;
            }
            ax2=ax-1;
            for(int j=0;j<S;j++){
                ax2=max(ax2,f[j]);
            }
            ax=ax2;
        }
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }

    return 0;
}
