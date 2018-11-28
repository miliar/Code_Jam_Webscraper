#include<iostream>
using namespace std;

int N,P,Q;
int q[10],q1[10];
bool used[128];
int mini=10000000;

int  sol()
{ int sum=0;       
 for(int i=1;i<=Q;i++)
  {
   for(int j=q[i]-1;j>=1 && !used[j];j--)
    sum++;
   for(int j=q[i]+1;j<=P && !used[j];j++)
    sum++;
                   
  used[q[i]]=1;         
}      // if(sum==31) {for(int i=1;i<=Q;i++) cout<<q[i]<<" ";  cout<<endl;}
return sum;
}

int main()
{
 cin>>N;
 
  for(int i=1;i<=N;i++) {
   cin>>P>>Q;  mini=10000000;   memset(used,0,sizeof(used));
   
    for(int j=1;j<=Q;j++){
     cin>>q[j]; q1[j]=q[j];}
     
            bool f=0;
        mini=min(mini,sol());
      
      while(next_permutation(q+1,q+Q+1)){   f=1;
        memset(used,0,sizeof(used));     
            
          mini=min(mini,sol());
           
          }
   
  /* if(f==0) {
      for(int j=1;j<=Q;j++)
       q[j]=q1[j];
       
       
         mini=min(mini,sol());
       
       }  */
   cout<<"Case #"<<i<<": "<<mini<<endl;
    }
    
         
return 0;
}     
