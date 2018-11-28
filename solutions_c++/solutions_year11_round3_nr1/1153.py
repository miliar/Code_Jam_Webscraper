#include<iostream>
#include<cstdio>
#include<string>

using namespace std;


int t,tc,r,c,cnt,i,j,cn;
bool poss=true;
main()
{
      char inp[51][51];
      char ch;
      cin>>t;
      
      string s;
      cn=0; cnt=0;
      for(tc=1;tc<=t;++tc)
      {
        //cout<<tc<<"----------n";
         cin>>r>>c;
         cn=0; cnt=0;
         for(i=0;i<r;++i)
         {
            cin>>inp[i];
          //  cout<<inp[i]<<"\n\n";
            for(j=0;j<c;++j)
            {   
                //inp[i][j]=;
                if(inp[i][j]=='#') ++cn;
            }
            //cout<<"done"<<r<<" "<<c<<"\n";
         }
         
         //cout<<"cn : "<<cn<<"\n";
         
         if(cn%4==0)
         {
             poss=true;
             cnt=0;
           //  cout<<"Entered....\n\n";
             for(i=0;i<r-1 && poss;++i)
             {   for(j=0;j<c-1 && poss;++j)
                 {
                    if(inp[i][j]=='#')
                    {   if(inp[i][j+1]=='#' && inp[i+1][j+1]=='#' && inp[i+1][j]=='#')
                        {
                           inp[i][j]='/'; inp[i][j+1]='\\'; inp[i+1][j]='\\'; inp[i+1][j+1]='/';
                           cnt+=4;
                        }
                        else poss=false;
                    }
                 }
             }
             
             if(cnt!=cn) { poss=false; /*cout<<"cnt!=cn"<<"\n"; */}
         }
         else { poss=false; /*cout<<"cn%4!=0"<<"\n\n"; */}
         
         cout<<"Case #"<<tc<<":\n";
         
         if(poss)
         {   for(i=0;i<r;++i)
                cout<<inp[i]<<"\n";
                
         }
         else 
         {   cout<<"Impossible\n";
         }
      
      
      }
      
}
