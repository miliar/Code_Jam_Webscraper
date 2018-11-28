#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;
int main(){
    ifstream in("C:\\Documents and Settings\\Ankit Gupta\\Desktop\\C-large.in");  
    ofstream out("C:\\Documents and Settings\\Ankit Gupta\\Desktop\\C-large.out");
    long long int arr[1001],R,k,N,store[1001],last[1001];
    int notimes;
    in>>notimes;
    for(int cases=1;cases<=notimes;cases++){
            in>>R>>k>>N;
            for(int p=1;p<=N;p++)
                    in>>arr[p];
                    
            for(int p=1;p<=N;p++){
                    
                    int cond=1,q=p;
                    store[p]=0;
                    int flag=1;
                    
                    while(cond){
                                if( q==p && flag==0){
                                    if(p==1)
                                            last[p]=N;
                                    else
                                            last[p]=p-1;
                                    cond=0;
                                    continue;
                                }
                                            
                                if( (store[p]+arr[q]) > k ){
                                    last[p]=q;
                                    cond=0;
                                    continue;
                                }
                                
                                flag=0;
                                store[p]+=arr[q];
                                q=q+1;
                                if(q>N)
                                       q=1;
                    }
            }
            
      //      cout<<store[1]<<" "arr[1]<<" "<<last[1]<<endl;
            long long int sum=0;
            int i=1;
            for(long int r=1;r<=R;r++){
                     sum=sum+ store[i];
                     i = last[i];
            }
            out<<"Case #"<<cases<<": "<<sum<<endl;
    }
    
    out.close();
   // int pp;cin>>pp;
    return 0;
}                                
                                
            
    
