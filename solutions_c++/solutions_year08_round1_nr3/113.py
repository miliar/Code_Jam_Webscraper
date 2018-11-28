#include<iostream>
#include<string>
#include<map>

using namespace std;

int main(){
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    int T,n;
    
    int ans;
    
    cin>>T;
    
    int a[3000];
    
    a[0]=2;
    a[1]=6;
    
    for(int i=2;i<700;i++){
        a[i]=(6*a[i-1]%1000-4*a[i-2]%1000)%1000;
        while(a[i]<0) a[i]+=1000;
    }
    
    for(int i=0;i<T;i++){
        cin>>n;
        while(n>=166) n-=100;
        
        ans=(a[n]-1)%1000;
        
        while(ans<0) ans+=1000;
        
        string s="";
        
        for(int j=0;j<3;j++){
            s+='0'+ans%10;
            ans/=10;
        }
        cout<<"Case #"<<i+1<<": ";
        for(int j=2;j>=0;j--) cout<<s[j];
        cout<<endl;
    }
}
