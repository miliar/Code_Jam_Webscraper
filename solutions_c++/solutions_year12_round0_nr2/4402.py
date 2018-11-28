#include<iostream>
using namespace std;

main()
{
      int t,tst; cin>>t;
      for(tst=1;tst<t+1;tst++)
      {
          
          int n,s,p,val,i;
          cin>>n>>s>>p;
          int t[n];
          int ans=0,sup=0;
         
          for(i=0;i<n;i++)
          {
               cin>>t[i];
              
               if(t[i]>3*p) ans++;
               
               if(t[i]==(3*p))
               { 
                 {ans++; 
                }}
                 
               if(t[i]==3*p-1)
               { 
                 if(p-1>=0) {ans++;}}
               
               if(t[i]==3*p-2)
               { 
                 if(p-2>=0) {ans++;}} 
               
               if(t[i]==3*p-3)
               { 
                 if(p-2>=0) {ans++;sup++;}}
               
               if(t[i]==3*p-4)
               { 
                 if(p-2>=0) {ans++;sup++;}}
                 
                 }//end of all ip processing
               
               if(sup>s) ans = ans - (sup-s);
               
               
               
               cout<<"Case #"<<tst<<": "<<ans<<endl;
               
               }//end of tstcase
               }//end
               
                  
                 
               
          
          
          
         
