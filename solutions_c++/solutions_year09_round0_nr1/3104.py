#include<iostream>
#include<string>
#include<cstdio>
#include<stdlib.h> 
using namespace std;
int main()
  {  int l,d,n,i;string c1;
     char a[5001][20],s[450],c;
     int co,j,k,nc,f,cas=0;
     cin>>l>>d>>n;getline(cin,c1,'\n');
     for(i=1;i<=d;i++) cin.getline(a[i],20);  
     while(n--)
     {  cin.getline(s,450);
       co=0;cas++; 
        for(j=1;j<=d;j++)
          { k=0;nc=0;
            for(i=0;s[i]!='\0';i++)
             {  if(s[i]=='(')
                 { f=0;
                   while(s[i]!=')')
                      { if(a[j][k]==s[i]) {f++;if(f==1)k++;
                                          }i++;}
                   if(f==0) {nc=1;break;
                            }
                 }
               else if(s[i]==')')continue;
               else if(s[i]==a[j][k]) k++;
               else {nc=1;break;
                    }
             }
            if(nc==0)co++;
          }
         cout<<"Case #"<<cas<<": "<<co;if(n!=0)cout<<endl;      
     }
     return 0;
  }   
         
