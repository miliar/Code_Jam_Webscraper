#include<fstream>
using namespace std;
int main()
{
    int i,j,t,v=0,flag,r,c;
    ifstream fin("A-large.in");
    ofstream fout("outputq1l.txt");
    char ch[50][50];
    fin>>t;
    while(t--)
    {
              v++;
              flag=0;
              fin>>r>>c;
              for(i=0;i<r;i++)
              {
                              for(j=0;j<c;j++)
                              {
                                              fin>>ch[i][j];
                                              }}
                                              for(i=0;i<r-1;i++)
                                                {
                                                   for(j=0;j<c-1;j++)
                                                       {
                                                                   if(ch[i][j]=='#'&&ch[i+1][j]=='#'&&ch[i][j+1]=='#'&&ch[i+1][j+1]=='#')
                                                                   {
                                                                       ch[i][j]='/';
                                                                       ch[i][j+1]='\\';
                                                                       ch[i+1][j]='\\';
                                                                       ch[i+1][j+1]='/';
                                                                       }
                                                                       }}
                                                                        for(i=0;i<r;i++)
                                                                        {
                                                                    for(j=0;j<c;j++)
                                                                          {
                                                                                    if(ch[i][j]=='#')
                                                                                    flag=1;
                                                                                    }}
                                                                                    if(flag==1)
                                                                                    fout<<"Case #"<<v<<":"<<endl<<"Impossible"<<endl;
                                                                                    else
                                                                                    {fout<<"Case #"<<v<<":"<<endl;
                                                                                     for(i=0;i<r;i++)
              {
                              for(j=0;j<c;j++)
                              {fout<<ch[i][j];
                              }
                              fout<<endl;
                              }
                              }
                              }
                              return 0;
                              }
                              
                              
                                                       
                                                          
                              
                              
                                              
