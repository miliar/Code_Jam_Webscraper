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
    int t,t1;
    cin>>t;
    int pd,pg;
    long long n;
    int i,j;
    t1 = 1;
    while(t1<=t){
                 cin>>n>>pd>>pg;
                 int flag=0;
                 if(pg==100&&pd!=100)
                          flag=0;
                 else if(pg==0&&pd!=0)
                          flag=0;
                 else
                 {
                        if(n>100){
                                  n=100;
                                  flag=1;
                        }
                        else
                        {        
                                 for(i=1;i<=n;i++){
                                          if(fmod((pd*i*1.0)/(100.0),1.0)==0){
                                                           //cout<<i<<endl;                   
                                                           flag=1;
                                                           break;
                                          }
                                 }
                        }
                 }
                 cout<<"Case #"<<t1<<": ";
                 if(flag==1)
                            cout<<"Possible\n";
                 else
                            cout<<"Broken\n";
                 t1++;
    }
}
                              
                 
                                
                                     
      
