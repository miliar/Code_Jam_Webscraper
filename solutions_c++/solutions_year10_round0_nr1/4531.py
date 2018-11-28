#include<iostream>
#include<cstdlib>
#include<fstream>

using namespace std;
struct elex
{ int s;
  int p;
};

int main()
{   elex *snapper;
    fstream f;
    f.open("Output.txt",ios::out);
    int *n,*k,i,j,l,*a;
    int t;
    cin>>t;
    n= new int[t+1];
    k=new int[t+1];
    a=new int[t+1];
        
    for(i=1;i<=t;i++)
    cin>>n[i]>>k[i];
    
    for(i=1;i<=t;i++)
    {   snapper = new elex[n[i]+1];
        for(j=0;j<=n[i];j++)
        { snapper[j].s=snapper[j].p=0;
        }
        snapper[0].p=1;
    
        for(l=1;l<=k[i];l++)
        {  
          for(j=n[i];j>0;j--)
          { if(snapper[j-1].p==1)
             snapper[j].s=!(snapper[j].s) ;
          } 
          
          for(j=1;j<=n[i];j++)
          {  
              if((snapper[j-1].p==1) && (snapper[j].s==1)) 
               snapper[j].p=1;
              else  snapper[j].p=0;     
              
          }
          
        }    
        a[i]=snapper[n[i]].p;
    }
   for(i=1;i<=t;i++)
   {f<<"Case #"<<i<<":";
    if(a[i]==0) f<<" OFF";
    else  f<<" ON";
    f<<"\n";
   } 
   f.close();
 //cout<<(!(1));
    system("pause");
    return 0;
}
