#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
#include<string>
#include<iomanip>
#define beginT int _T; cin>>_T; for(int _t=1;_t<=_T;_t++)
#define printT(_ans) cout<<"Case #"<<_t<<": "<<_ans<<endl
using namespace std;

int main()
{
    beginT
    {
          int N;
          cin>>N;
          char g[N][N];
          long double wp[N],owp[N],oowp[N];
          int a[N],s[N];
          for(int i=0;i<N;i++)
          {
                  a[i]=0,s[i]=0;
                  for(int j=0;j<N;j++)
                  {
                          cin>>g[i][j];
                          if(g[i][j]!='.')
                          {
                                          if(g[i][j]=='1')
                                                       a[i]++;
                                          s[i]++;            
                          }                                     
                  }
                  wp[i] = (long double)a[i]/(long double)s[i];
                  //cout<<wp[i]<<" ";
                  cin.ignore();
          }
          //cout<<endl;
          for(int i=0;i<N;i++)
          {
                  long double owpi=0;
                  int s1=0;
                  for(int j=0;j<N;j++)
                  {
                          if(i==j || g[j][i]=='.') continue;
                          owpi+=((long double)(a[j]-(g[j][i]=='1'))/(long double)(s[j]-(g[j][i]!='.')));
                          s1++;
                  }
                  owp[i] = owpi/(long double)(s1);
                  //cout<<owp[i]<<" ";
          }
          //cout<<endl;
          for(int i=0;i<N;i++)
          {
                  long double oowpi=0;
                  int s1=0;
                  for(int j=0;j<N;j++)
                  {
                          if(i==j || g[j][i]=='.') continue;
                          oowpi+=owp[j];
                          s1++;
                  }
                  oowp[i] = oowpi/(long double)(s1);
                  //cout<<oowp[i]<<" ";
          }
          //cout<<endl;
          printT("");
          for(int i=0;i<N;i++)
          {
                  long double rti = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
                  cout<<setprecision(12)<<rti<<endl;
          }
    }
    return 0;
}
