#include<iostream>
using namespace std;
int main(){
    int s[1000];
    int t,r,k,n,sum,cases=1;
    freopen("C-small-attempt1.in","rt",stdin);
    freopen("c.txt","wt",stdout);
    cin>>t;
    while(t--){
         sum=0;
         cin>>r>>k>>n;
         for(int i=0;i<n;i++)
               cin>>s[i];
         int i=0;
         while(r--){
              int j=0;
              for(int w=0;j<=k&&w<n;j+=s[i=i%n],i++,w++);
                   if(j>k)
                   j=j-s[--i];
              sum+=j;                
         } 
         cout<<"Case #"<<cases++<<": "<<sum<<endl;          
    }    
} 
