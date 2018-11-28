#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <utility>
#include <sstream>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <stack>
#include <algorithm>
#include <math.h>
#include <conio.h>
#include <fstream>


using namespace std;


int main()
{
          int i,j,k,convert,n,a,b,ta,poolA,poolB,totA,totB,test;
          vector <int> dA,dB,temp;
          char cc[100];
          string t;
          for(i=0;i<2*24*60;i++)
          {
                              temp.push_back(0);
          }
          fstream fin("B-large.in");
          fin>>n;
          
          for(i=0;i<n;i++)
          {
                          // fetch data
                          dA=dB=temp;
                          poolA=poolB=0;
                          fin>>ta;
                          fin>>a;
                          fin>>b;
                          totA=totB=0;
                          //cout<<"n: "<<n<<" ta:"<<ta<<" a:"<<a<<" b:"<<b<<endl;
                          //getch();
                          // for A
                          for(j=0;j<=a;j++)
                          {
                                          t.resize(0);
                                          fin.getline(cc,100);
                                          for(k=0;k<strlen(cc);k++)
                                                         t.push_back(cc[k]);
                                          if(j==0)
                                                  continue;
                                          //cout<<t<<endl;
                                          convert=(t[0]-'0')*10+(t[1]-'0');
                                          convert*=60;
                                          convert+=((t[3]-'0')*10+(t[4]-'0'));
                                          dA[convert]--;
                                          test=convert;
                                          
                                          convert=(t[6]-'0')*10+(t[7]-'0');
                                          convert*=60;
                                          convert+=((t[9]-'0')*10+(t[10]-'0'));
                                          convert+=ta;
                                          if(convert>=test)
                                                           dB[convert]++;
                          }
                          //for B
                          for(j=0;j<b;j++)
                          {
                                          t.resize(0);
                                          fin.getline(cc,100);
                                          for(k=0;k<strlen(cc);k++)
                                                         t.push_back(cc[k]);
                                          //cout<<t<<endl;
                                          convert=(t[0]-'0')*10+(t[1]-'0');
                                          convert*=60;
                                          convert+=((t[3]-'0')*10+(t[4]-'0'));
                                          dB[convert]--;
                                          test=convert;
                                          
                                          convert=(t[6]-'0')*10+(t[7]-'0');
                                          convert*=60;
                                          convert+=((t[9]-'0')*10+(t[10]-'0'));
                                          convert+=ta;
                                          if(convert>=test)
                                                           dA[convert]++;
                          }
                          // fetching over
                          // process data
                          for(j=0;j<dA.size();j++)
                          {
                                                  if(dA[j]<0)
                                                  {
                                                               k=poolA+dA[j];
                                                               poolA+=dA[j];
                                                               if(poolA<0)
                                                                          poolA=0;
                                                               if(k<0)
                                                                      totA-=k;
                                                   }
                                                  if(dA[j]>0)
                                                  {
                                                               poolA+=dA[j];
                                                  }  
                                                  if(dB[j]<0)
                                                  {
                                                               k=poolB+dB[j];
                                                               poolB+=dB[j];
                                                               if(poolB<0)
                                                                          poolB=0;
                                                               if(k<0)
                                                                      totB-=k;
                                                  }
                                                  if(dB[j]>0)
                                                  {
                                                               poolB+=dB[j];
                                                  }                        
                          }
                          // processing over
                          // give result
                   
                          cout<<"Case #"<<i+1<<": "<<totA<<" "<<totB<<endl;
                          // result over
                          // reinitialize vars
                          //getch();

          }
    
    
    /* Debug
    for(i=0;i<n;i++)
    {
                    for(j=0;j<s;j++)
                                    cout<<se[j]<<endl;
                    cout<<endl;
                    for(j=0;j<q;j++)
                                    cout<<qw[j]<<endl;
    }
    */
    //cout<<"done";
    getch();
    return 1;  
}
