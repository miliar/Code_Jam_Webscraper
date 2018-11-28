#include<iostream>
using namespace std;
char s[51][51];
int main()
 { int i,j,r,c,cc=0,n,f,t;
   cin>>t;  
   while(t--)
    { cin>>r>>c;cc++;//cout<<"\\"<<"//";
      for(i=1;i<=r;i++)for(j=1;j<=c;j++)cin>>s[i][j];f=1;
      for(i=1;i<=r;i++)for(j=1;j<=c;j++)if(s[i][j]=='#'){ if(i+1<=r && j+1<=c) {if(s[i+1][j]=='#' && s[i+1][j+1]=='#' && s[i][j+1]=='#') {
                                                          s[i+1][j]='\\';
                                                          s[i+1][j+1]='/'; s[i][j+1]='\\';s[i][j]='/';
                                                          } else {f=0;break;}  } else {f=0;break;}} 
      cout<<"Case #"<<cc<<":\n";
      if(f==0)cout<<"Impossible"<<endl;
      else {      for(i=1;i<=r;i++){for(j=1;j<=c;j++)cout<<s[i][j];cout<<endl;}}
    }
      return 0;
      }
