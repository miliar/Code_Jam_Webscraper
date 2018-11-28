#include <iostream>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <cstdlib>

using namespace std;

int n,i,j,r,c,test,dd,t;
int d[51][51];
string s[51];

int main(){
    freopen("c://input.txt","r",stdin);
    freopen("c://output.txt","w",stdout);
    cin>>t;
    for(test=1;test<=t;test++){
       for (i=0;i<51;i++)
           for (j=0;j<51;j++)
               d[i][j]=0;
       cin>>r>>c;
       
       for (i=0;i<r;i++)
           cin>>s[i];
       cout<<"Case #"<<test<<":"<<endl;
       dd=0;
       for (i=0;i<r;i++)
           for (j=0;j<c;j++)
               if (s[i][j]=='#' && d[i][j]==0){
                   if (j<c-1 && s[i][j+1]=='#' && i<r-1 && s[i+1][j]=='#' && s[i+1][j+1]=='#'){
                      s[i][j]='/';
                      s[i][j+1]='\\';
                      s[i+1][j]='\\';
                      s[i+1][j+1]='/';
                      d[i][j]=1;
                      d[i+1][j]=1;
                      d[i+1][j+1]=1;
                      d[i][j+1]=1;          
                   } else
                   {
                     dd=1;
                     break;      
                   }   
               } 
       if (dd){
          cout<<"Impossible"<<endl;           
       } else
       {
            for (i=0;i<r;i++)
                cout<<s[i]<<endl;      
       }
    }
    return 0;    
}
