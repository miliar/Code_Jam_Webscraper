#include<stdio.h>
#include<iostream.h>

long long cas,cas1,n,m,x,y,z,A[1009],B[1009],i;
long long count[1009],sum,j;
int main()
{
/////freopen("c.in.txt","r",stdin);
/////freopen("c_small_out.in","w",stdout);

cin>>cas;    

for(cas1=1;cas1<=cas;cas1++)
{
cin>>n>>m>>x>>y>>z;                            
                            
 for(i=0;i<m;i++)
 cin>>A[i];  
            
 for(i=0;i<n;i++)
 {
 B[i]=A[i%m];
 A[i%m] = (x * A[i % m] + y * (i + 1)) % z;                
 count[i]=1;
}                          
 sum=0;
 
 for(i=0;i<n;i++)
 {
 sum+=count[i];
 sum=sum%1000000007;
 for(j=i+1;j<n;j++)
 if(B[j]>B[i])                
 {
 count[j]+=count[i];
 count[j]=count[j]%1000000007;                             
 }                
 }                         
      
      
     cout<<"Case #"<<cas1<<": "<<sum<<endl;                      
                            
}    
    
    
    
    
return 0;    
}
