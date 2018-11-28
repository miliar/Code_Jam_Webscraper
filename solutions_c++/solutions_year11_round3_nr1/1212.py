#include<iostream>
#include<fstream>
using namespace std;
#define R 60
#define C 60
char data[R][C],res[R][C];
int r,c;
bool find(int s,int t)
{
     while(s<r&&res[s][t]!='#')
     {
                          t++;
                          if(t>=c){t=0;s++;}
                          //cout<<s<<t<<endl;
     }
     if(s==r)return true;
     if(s==r-1||t==c-1||res[s][t+1]!='#'||res[s+1][t]!='#'||res[s+1][t+1]!='#')return false;
    // cout<<s<<' '<<t<<' '<<res[s][t]<<res[s][t+1]<<res[s+1][t]<<res[s+1][t+1]<<endl;
     res[s][t]='/';
     res[s][t+1]='\\';
     res[s+1][t]='\\';
     res[s+1][t+1]='/';
   //  for(t=0;t<r;t++)
   //                                     cout<<res[t]<<"\n";
     return find(s,t+2);
 }
int main()
{
    fstream  fout;
    fout.open("1.txt",ios::out);
    int T;
    cin>>T;
    int i;
    for(i=0;i<T;i++)
    {
                    fout<<"Case #"<<i+1<<":\n";
                    cin>>r>>c;
                    int j;
                    for(j=0;j<r;j++)
                    {
                                    cin>>data[j];
                                    strcpy(res[j],data[j]);
                    }
                    if(!find(0,0))fout<<"Impossible\n";
                                    else 
                                    {
                                         for(j=0;j<r;j++)
                                         fout<<res[j]<<"\n";
                                     }
                                    }
    fout.close();
   // cin>>i;
    return 0;
    
}
 
