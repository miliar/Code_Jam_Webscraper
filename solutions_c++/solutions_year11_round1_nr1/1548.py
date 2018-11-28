#include<fstream>
using namespace std;
int main()
{
    int i,t,n,pd,pg,g,flag,q=0,k;
    double d,x;
    ifstream fin("A-small-attempt1.in");
    ofstream fout("output11.txt");
    fin>>t;
    
    while(t--)
    {
              fin>>n>>pd>>pg;
              flag=0;
              q++;
              for(i=1;i<=n;i++)
              {
                               d=i*pd/100.0;
                                k=(int)d;
                                if((d-k)==0.0)
                                {
                                              if((pg==100&&pd!=100)||(pg==0&&pd!=0))
                                              flag=0;
                                              else
                                              flag=1;
                                              }
                                              if(flag==1)
                                              break;
                                              }
                                               if(flag==1)
                                               fout<<"Case #"<<q<<":"<<" Possible"<<endl;
                                               else
                                               fout<<"Case #"<<q<<":"<<" Broken"<<endl;
                                              
                                              }
                                              fout<< flush;
                                              fout.close();
                                              return 0;
                                              }                
                                              
                               
