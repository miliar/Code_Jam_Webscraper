#include<iostream>
#include<fstream>
using namespace std;

int main()
{ ifstream fin;
  ofstream fo;
  int i,j,k,t,ans,n;
  fin.open("A-large.in");
  fo.open("A-large.out");
  fin>>t;
  for(i=0;i<t;i++)
  { fin>>n;
    int A[n],B[n];
    for(j=0;j<n;j++) fin>>A[j]>>B[j];
    ans=0;
    
    for(j=0;j<n;j++)
    {
       for(k=j+1;k<n;k++) 
       {  
          if( A[j]>A[k] && B[k]>B[j])ans+=1;
          else if(A[k]>A[j] && B[j]>B[k])ans+=1;
       }  
     }
    
  
    fo<<"Case #"<<i+1<<": "<<ans<<endl;
  }
fo.close();
fin.close();                                     
return 0;
}
