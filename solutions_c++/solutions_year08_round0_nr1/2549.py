#include<iostream>
#include<vector>
#include<string>
#include<fstream>
#include<cstdio>
using namespace std;

int main()
{
    int num,x=0;
    cin>>num;
fflush(stdin);
    while(num--)
    {
                   int n;
                   cin>>n;
                   fflush(stdin);
                   x++;
                   vector <string> in(n,"");
                   for(int i=0;i<n;i++)
                   getline(cin,in[i]);
                   int ans=0;
                   int q;
                   cin>>q;
                   string str;
                   fflush(stdin);
                   vector <bool> cut(n,false);
                   for(int i=0;i<q;i++)
                   {
                     getline(cin,str);
                     for(int j=0;j<n;j++)if(in[j]==str){cut[j]=true;break;}
                     int flag=0;
                     for(int j=0;j<n;j++)if(cut[j]==false){flag=1;break;}
                     if(flag==0)
                     {for(int j=0;j<n;j++)cut[j]=false;ans++;
                      for(int j=0;j<n;j++)if(in[j]==str){cut[j]=true;break;}
                      }
                   }
                  cout<<"Case #"<<x<<": "<<ans<<endl;
    }
     return 0;
}
