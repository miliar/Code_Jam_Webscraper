#include<iostream.h>
#include <fstream.h>
#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<vector>
#include<queue>
using namespace std;

int main(){
    freopen("A-large.in", "r", stdin);
//	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
    
    int t,caseno=0;
    cin>>t;
    
    while(t--){
               int ans=0;
               int n;
               cin>>n;
               int a[n+1],b[n+1],i,j;
               for(i=0;i<n;i++){
                                cin>>a[i]>>b[i];
                                //f[a[i]]=b[i];
               }
               
               for(i=0;i<n;i++){
                         for(j=i+1;j<n;j++){
                                           if(a[j]>a[i] && b[i]>b[j])
                                                        ans++; 
                                           if(a[j]<a[i] && b[i]<b[j])
                                                        ans++; 
                                            
                         }       
                                
               }
               
               caseno++;
                    cout<<"Case #"<<caseno<<": "<<ans<<endl;                      
    }
       
}
