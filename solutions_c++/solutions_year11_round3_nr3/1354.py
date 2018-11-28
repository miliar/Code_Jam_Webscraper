#include<iostream>
#include<fstream>
#include<cstring>
#include<cmath>
#include<cstdlib>

using namespace std;
long long fr[10009];
long long N,L,H;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("output.txt");
    int T;
    fin>>T;
    long long i,j;
    long long g,k;
    int flag1,flag;
    for(i=0;i<T;i++)
    {
                    fout<<"Case #"<<i+1<<": ";
                    fin>>N>>L>>H;
                    for(j=0;j<N;j++)
                    {
                                    fin>>fr[j];
                    }
                    flag1=0;
                    for(j=L;j<=H;j++)
                    {
                                     flag=0;
                                     for(k=0;k<N;k++)
                                     {
                                                     if(!(fr[k]%j==0 || j%fr[k]==0))
                                                     {
                                                                     flag=1;
                                                                     break;
                                                                                   
                                                     }
                                                     
                                     }
                                     if(flag==0)
                                      {
                                                          fout<<j<<"\n";
                                                          flag1=1;
                                                          break;
                                      }
                    }
                    if(flag1==0)
                                fout<<"NO\n";
    }
    fin.close();
    fout.close();
    cout<<"done";
    cin>>i;
    return 0;
}
