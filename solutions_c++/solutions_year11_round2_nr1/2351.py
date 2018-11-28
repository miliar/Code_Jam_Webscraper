#include<iostream>
#include<fstream>
#include<cstring>
#include<cmath>
#include<cstdlib>

using namespace std;
//RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
char sc[100][100];
int N;
double wp[100],owp[100],oowp[100];
int n[100];

bool solution()
{
     int i,j;
     int win,lost;
      for(i=0;i<N;i++)
      {
                      wp[i]=owp[i]=oowp[i]=0;
      }
      for(i=0;i<N;i++)
      {
                      win=0;
                      lost=0;
                      for(j=0;j<N;j++)
                      {
                       if(sc[i][j]=='1')
                       {
                                       ++win;
                       }
                       if(sc[i][j]=='0')
                       {
                                       ++lost;
                       }
                       
                      }
                      wp[i]=win;
                      n[i]=win+lost;
      }
      for(i=0;i<N;i++)
      {
                      int nop=0;
                      double avg=0;
                      for(j=0;j<N;j++)
                      {
                        if(i!=j)              
                        {
                                              if(sc[j][i]=='0')
                                              {
                                                               owp[i]+=(double)wp[j]/(n[j]-1);
                                                               nop++;
                                              }
                                              if(sc[j][i]=='1')
                                              {
                                                               owp[i]+=(double)(wp[j]-1)/(n[j]-1);
                                              nop++;
                                              }
                        }
                      }
                      owp[i]=owp[i]/nop;
      }
      for(i=0;i<N;i++)
      {
                      int nop=0;
                      for(j=0;j<N;j++)
                      {
                                      if(sc[i][j]!='.')
                                      {
                                                       oowp[i]+=owp[j];
                                                       nop++;
                                      }
                      }
                      oowp[i]=oowp[i]/nop;
      //                cout<<oowp[i]<<"\n";
      }
      for(i=0;i<N;i++)
      {
                      cout<<(0.25*((double)wp[i]/n[i])+0.5*owp[i]+.25*oowp[i])<<"\n";
      }
      
}

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("output.txt");
    int T;
    fin>>T;
    int i,j,k;
    for(i=0;i<T;i++)
    {
                    fin>>N;
                    //cout<<N;
                    for(j=0;j<N;j++)
                    {
                                    for(k=0;k<N;k++)
                                    {
                                                    fin>>sc[j][k];
                                    }
                    }
                    cout<<"Case #"<<i+1<<":\n";
                    solution();
                    //fout<<"Case #"<<i+1<<":\n";
                    
    }
    fin.close();
    fout.close();
    cin>>i;
    return 0;
}
