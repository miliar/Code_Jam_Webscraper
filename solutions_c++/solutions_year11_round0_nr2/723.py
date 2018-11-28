#include<iostream>
#include <fstream>
using namespace std;
struct rp{
       char e1;
       char e2;
       char ne;
       }a[36];

struct op{
       char e;
       char oe;
       }b[28];

int main()
{
    int c,d,n,t,i,j,k,l,m,p;
    char temp[5],s[105];
    ifstream in;
    ofstream o("output1.txt");
    in.open("B-large.in");
    in>>t;
    i=1;
    while(i<=t)
    {
               in>>c;
               for(j=0;j<c;++j)
               {
                               in>>temp;
                               a[j].e1=temp[0];
                               a[j].e2=temp[1];
                               a[j].ne=temp[2];
                               }
                               in>>d;
                               for(j=0;j<d;++j)
                               {
                                               in>>temp;
                                               b[j].e=temp[0];
                                               b[j].oe=temp[1];
                                               }
                               in>>n>>s;
                               for(j=1;j<n;++j)
                               {
                                  for(k=0;k<c;++k)
                                  {
                                       if((s[j]==a[k].e1&&s[j-1]==a[k].e2)||(s[j-1]==a[k].e1&&s[j]==a[k].e2))
                                       {
                                              s[j-1]=a[k].ne;
                                              for(l=j;l<n;++l)s[l]=s[l+1];
                                              --n;
                                              break;                                                                                                       
                                                                                 }
                                                                               }
                                  
                                  for(l=j-1;l>=0;--l)
                                  {
                                                     for(k=0;k<d;++k)
                                                     {
                                                                     if((s[j]==b[k].e&&s[l]==b[k].oe)||(s[l]==b[k].e&&s[j]==b[k].oe))
                                                                     {
                                                                         for(m=j+1;m<n;++m)s[m-j-1]=s[m];
                                                                         //cout<<j<<endl;
                                                                         n=n-j-1;
                                                                         j=0;
                                                                         p=1;
                                                                         //cout<<n<<endl;
                                                                         break;
                                                                                                    }
                                                                     }
                                                                     if(p==1){p=0;break;}
                                                     }
                                                               }
               if(n<=0)o<<"Case #"<<i<<": []"<<endl;
               else 
               {
                    o<<"Case #"<<i<<": [";
                    if(n==1)o<<s[0]<<"]"<<endl;
                    else 
                    {
                         for(m=0;m<n-1;++m)o<<s[m]<<", ";
                         o<<s[m]<<"]"<<endl;
                         }
                    }
                    ++i;
               }
               system("pause");
               return 0;
    }
