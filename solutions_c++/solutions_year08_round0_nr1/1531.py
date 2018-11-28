#include<iostream>
#include<string>
using namespace std;


int main()
{
int N=0,s=0,q=0,i=0,j=0,l=0,swi=0,ltemp=0,temp=0,k=0;

string S[100],Q[1000],t;
cin>>N;
//cout<<"N="<<N;
for(i=0;i<N;i++)
 {
  cin>>s;
  // cout<<"s="<<s;
    getline(cin,t);
   for(j=0;j<s;j++)
    {getline(cin,S[j]);
    //  cout<<j<<S[j];
     }
   cin>>q;
   //cout<<"q="<<q;
    getline(cin,t); 
   for(j=0;j<q;j++)
   {getline(cin,Q[j]);
     // cout<<j<<Q[j];
     }
    
  l=0;
   swi=0;
   
  while(l<q)
   { ltemp=0;
     for(j=0;j<s;j++)
     { t=S[j];
       k=l;
       
       
        
       
       while(t!=Q[k] && k<q )
        { //if((k+l)<q)
           //{ l=q;
            // break;
            // }
           
            k++;

         }
        if(k>ltemp)
         ltemp=k;
       //cout<<S[j]<<k;
     }
    l=ltemp;
    
   // cout<<l;
    if(l<q)
     swi++;
    }
   cout<<"Case #"<<i+1<<": "<<swi<<endl; 
  }
 
}
