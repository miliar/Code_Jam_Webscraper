#include <cstdio>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

int n,h,l;
int r,c;
int a[103];

bool cumple(int num)
{
       bool si=true;
       
       for(int i=0;i<n && si; i++)
       {
               if(num>=a[i])
               {
                       if(num%a[i]!=0) si=false;
               }
               else if(a[i]%num)
                       si=false;
       }
       return si;
}


int main()
{

       int t;
       cin>>t;
       
       for(int i=1;i<=t;i++)
       {
            
               cin>>n>>h>>l;
               
               for(int j=0; j<n; j++)
                       cin>>a[j];
				
			   int resp=0;
               bool no=false;
               
               for(int j=h; j<=l && !no; j++)
               {
                       if(cumple(j))
                       {
                               no=true;
                               resp=j;
                       }
               }
               
               cout<<"Case #"<<i<<": ";
               
               if(!no) cout<<"NO\n";
               else cout<<resp<<endl;
               
       }
       return 0;
}
