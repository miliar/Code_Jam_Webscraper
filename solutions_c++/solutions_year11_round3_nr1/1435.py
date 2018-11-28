#include<iostream>
#include<fstream>
#include<cstring>
#include<cmath>
#include<cstdlib>

using namespace std;

bool solution()
{
 
}
int R,C;
char ar[100][100];
int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("output.txt");
    int T;
    fin>>T;
    int i,j,k;
    int flag;
    for(i=0;i<T;i++)
    {
                    fin>>R>>C;
                    for(j=0;j<R;j++)
                    {
                                    for(k=0;k<C;k++)
                                    {
                                                    fin>>ar[j][k];
                                                    //cout<<ar[j][k];
                                    }
                    }
                    
                    fout<<"Case #"<<i+1<<":\n";
                    ///////////////////////
                    flag=0;
                    for(j=0;j<R;j++)
                    {
                                    for(k=0;k<C;k++)
                                    {
                                                      if(ar[j][k]=='#')
                                                      {
                                                      if(j==R-1 || k== C-1)
                                                      {
                                                          fout<<"Impossible\n";
                                                          flag=1;
                                                          break;      
                                                      }
                                                      if(ar[j+1][k]=='#' && ar[j][k+1]=='#' && ar[j+1][k+1]=='#')
                                                      {
                                                         ar[j][k]='/';
                                                         ar[j][k+1]='\\';
                                                         ar[j+1][k]='\\';
                                                         ar[j+1][k+1]='/';               
                                                      }
                                                      else
                                                      {
                                                          fout<<"Impossible\n";
                                                          flag=1;
                                                          break;
                                                      }
                                                      }
                                    }
                                    if(flag==1)
                                    break;
                    }
                    if(flag==0)
                    {
                               for(j=0;j<R;j++)
                               {
                                               for(k=0;k<C;k++)
                                               fout<<ar[j][k];
                                               fout<<"\n";
                               }
                    }
//                    fout<<"Case #"<<i+1<<": "<<(solution()?"Possible":"Broken")<<"\n";
//                    cout<<"Case #"<<i+1<<": "<<ans<<"\n";
    }
    fin.close();
    fout.close();
    cin>>i;
    return 0;
}
