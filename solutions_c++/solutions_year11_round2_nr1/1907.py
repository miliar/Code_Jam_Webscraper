#include<fstream>
using namespace std;
int main()
{
    int t,n,i,j,k,z,v=0;
    ifstream fin("A-large (1).in");
    ofstream fout("output11q1l.txt");
    fin>>t;
    char ch[100][100];
    double wp[100][3],d,q,x,rpi,w,m;
    double owp[100];
    double oowp[100];
    while(t--)
    { v++;
              fin>>n;
              for(i=0;i<n;i++)
              {
                              for(j=0;j<n;j++)
                              {
                                              fin>>ch[i][j];
                                              }}
                                                            
                                  for(i=0;i<n;i++)
                                  {      w=0.0,m=0.0;
                                                  for(j=0;j<n;j++)
                                                  {
                                                                  if(ch[i][j]=='1')
                                                                  w++;
                                                                  if(ch[i][j]=='1'||ch[i][j]=='0')
                                                                  m++;
                                                                  }
                                                                  wp[i][0]=w/m;
                                                                  wp[i][1]=w;
                                                                  wp[i][2]=m;
                                                                  }
                                                                  for(i=0;i<n;i++)
                                                                  {
                                                                         q=0.0;     k=0;    
                                                                     for(j=0;j<n;j++)
                                                                     {
                                                                              if(ch[i][j]=='1'||ch[i][j]=='0')
                                                                              {
                                                                              d=(wp[j][1]-(ch[j][i]-48))/(wp[j][2]-1);
                                                                              q=q+d;
                                                                              k++;
                                                                              }
                                                                              }
                                                                              owp[i]=q/k;
                                                                              }
                                                                              for(i=0;i<n;i++)
                                                                              {x=0.0; z=0;
                                                                                              for(j=0;j<n;j++)
                                                                                              {
                                                                                                if(ch[i][j]=='1'||ch[i][j]=='0')
                                                                                                 {
                                                                                                   x=x+owp[j];
                                                                                                   z++;
                                                                                                   }
                                                                                                   }
                                                                                                   oowp[i]=x/z;
                                                                                                   
                                                                                                   }
                                                                                                   fout<<"Case #"<<v<<":"<<endl;
                                                                                                   for(i=0;i<n;i++)
                                                                                                   {               
                                                                                                                   rpi=wp[i][0]*0.25+owp[i]*.5+oowp[i]*.25;
                                                                                                                   fout.precision(6);
                                                                                                                   fout<<fixed<<rpi<<endl;
                                                                                                                   
                                                                                                                   
                                                                                                                   
                                                                                                                   }
                                                                                                                   
                                                                                                                   }
                                                                                                                   return 0;
                                                                                                                   }
                                                                                                                           
                                                                              
                                                                              
                                                                              
                                                                                   
                                                                                   
                                                                  
