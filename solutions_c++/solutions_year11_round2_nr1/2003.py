#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<sstream>
#include<cctype>
#include<stack>
#include<cmath>
#include <queue>
#include<string.h>

#define pb push_back
#define pi 3.14159265
#define x first
#define y second
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++)

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector< vector<int> > vii;
typedef vector<string> vs;
typedef vector< vector<string> > vss;
typedef vector<long> vl;
typedef vector< vector<long> > vll;

int main()
{
    freopen("input(1).in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    int t1=1;
    while(t1<=t){
                 int n;
                 cin>>n;
                 double wp[n+1];
                 char a[n+1][n+1];
                 int num[n+1],den[n+1];
                 int i,j;
                 cin.ignore();
                 string s;
                 for(i=1;i<=n;i++){
                                   getline(cin,s,'\n');
                                   for(j=1;j<=n+1;j++)
                                                      a[i][j] = s[j-1];
                 }
                 for(i=1;i<=n;i++){
                            num[i]=0,den[i]=0;
                            for(j=1;j<=n;j++){
                                              if(a[i][j]=='1'){
                                                              num[i]++;
                                                              den[i]++;
                                              }
                                              else if(a[i][j]=='0'){
                                                   den[i]++;
                                              }
                            }
                            //cout<<num[i]<<"  "<<den[i]<<endl;
                            wp[i] = (num[i]*1.0)/(den[i]*1.0);
                 }
                 
                 //owp calculate
                 int down;
                 double up;
                 double owp[n+1];
                 //cout<<n<<endl;
                 for(i=1;i<=n;i++){
                                   up=0.0;
                                                     down=0;
                                   for(j=1;j<=n;j++){
                                                     
                                                     
                                                     if(a[i][j]!='.'){
                                                                      
                                                                     if(a[i][j]=='1'){
                                                                                      down++;
                                                                                      up = up+(num[j]*1.0)/((den[j]-1)*1.0);
                                                                                     // cout<<up<<"  "<<down<<"  "<<j<<endl;
                                                                                      //system("pause");
                                                                     }
                                                                     else
                                                                     {
                                                                                       down++;
                                                                                      up = up+((num[j]-1)*1.0)/((den[j]-1)*1.0);
                                                                                      //cout<<up<<"  "<<down<<"  "<<j<<endl;
                                                                                      //system("pause");
                                                                     }
                                                     }
                                   }
                                   //cout<<up<<"  "<<down<<endl;
                                   owp[i]=(up*1.0)/(down*1.0);
                 }
                 //cout<<"hi";
                 double oowp[n+1];
                 for(i=1;i<=n;i++){
                                   up=0.0;
                                   down=0;
                                   for(j=1;j<=n;j++){
                                                     if(a[i][j]!='.'){
                                                                      up =up+owp[j];
                                                                      down++;
                                                     }
                                   }
                                   oowp[i] = up/down;
                 }
                 double ans;
                 cout<<"Case #"<<t1<<":"<<endl;
                /* for(i=1;i<=n;i++)
                                  cout<<wp[i]<<"  ";
                 cout<<endl;
                 
                 for(i=1;i<=n;i++)
                                  cout<<owp[i]<<"  ";
                 cout<<endl;
                 
                 for(i=1;i<=n;i++)
                                  cout<<oowp[i]<<"  ";
                 cout<<endl;*/
                 
                 for(i=1;i<=n;i++){
                                   ans = 0.25*wp[i]+0.50*owp[i]+0.25*oowp[i];
                                   //printf("%0.12lf\n",ans);
                                   cout.setf(ios::fixed,ios::floatfield);
                                   cout.precision(12);
                                   cout<<ans<<endl;
                 }
                 t1++;
    }
}
                                                                                                        
                 
                                                   
                                                         
                   
