#include<iostream>
#include<string>
#include<vector>
using namespace std;
int main()
{
     int l,d,n;
     cin>>l>>d>>n;
     int cas=1;
     
     vector <string> wd(d,"");
     
     while(cas<=d) {cin>>wd[cas-1];cas++;}
     
     cas=1;
     while(cas<=n)
     {
         
         string s;
         cin>>s;
         int cnt=0,i,j,k;
         for(k=0;k<wd.size();k++)
         {
           
           int m=0;
           bool deviate=false;
           for(i=0;i<s.size();)                      
           {
               bool cor=false;
               if(s[i]=='(')           
               {     
                     for(j=i+1;s[j]!=')';j++)
                      {
                            //cout<<"!!"<<s[j]<<" "<<wd[k][m]<<endl;
                            if(cor==true) continue;
                            if(s[j]==wd[k][m])                                     
                            {
                                 cor=true;   
                                 m++;                                                                                                
                            }
                      }
                      i=j+1;
               }
               else if(s[i]==wd[k][m])
               {
                    cor=true;
                    i++;
                    m++;
               }							
               if(cor!=true){deviate=true;break;} //else cout<<m<<" ";
               //cout<<"i="<<i-1<<" "<<s[i-1]<<" "<<m<<" "<<wd[k][m-1]<<endl;
               
              
           }
           if(deviate==false && m==l) cnt++;;
         }
         cout<<"Case #"<<cas<<": "<<cnt<<endl;
         cas++;
     }
     return 0;
}
