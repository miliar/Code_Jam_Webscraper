#include <cstdlib>
#include <iostream>

using namespace std;
int T,n,res;
int P[50];
string s;
int main(int argc, char *argv[])
{
    scanf("%d",&T);
    
    for(int t=1;t<=T;t++)
    {
    
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {cin>>s;
     int pos=n-1;
     while(s[pos]!='1' && pos>=0)
       pos--;
     P[i]=pos+1;
    }
    // for(int i=1;i<=n;i++)cout<<P[i]<<endl;
    res=0;
     for(int i=1;i<=n;i++)
     {
      if(P[i]>i)
      {
      int j=i+1;
      while(P[j]>i)j++;
      while(i!=j){swap(P[j],P[j-1]); res++; j--; 
      //cout<<"swap "<<j<<endl;
       }       
      }      
     }
    
    
    
    printf("Case #%d: %d\n",t,res);   
 
    } 
    
   // system("PAUSE");
    return 0;
}
