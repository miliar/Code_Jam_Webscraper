//A continuación, otra buena solución por andres.escobar
#include <algorithm>
#include <numeric>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cassert>
#include <cmath>
#include <complex>
#include <fstream>

using namespace std;

#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SIZE(t) ((int)((t).size()))
#define EMPTY(t) ((int)((t).empty()))
#define INF (1ll<<63)-1
#define x first
#define y second

#define sz(a)                   int(a.size())
#define all(a)                  (a).begin(), (a).end()
#define CL(a, b)                memset(a, b, sizeof a) 
#define UN(a)                   sort(all(a)), (a).erase(unique(all(a)), (a).end())
#define pb                              push_back
#define SORT(a)                 sort(all(a))

typedef long long ll;
typedef pair<int,int> ii;
typedef pair<ii,int> iii;
typedef vector<int> vi;
typedef vector<ii> vii;
const double eps = 1e-10;
double const pi = 3.14159265358979323846264338327950288419716939937510582097494;

int n,s,p;
vector < int > v;
int pun;
int ans=0;

int main(){
    freopen("B-small-attempt6.in","r",stdin);freopen("B-small-attempt6.out","w",stdout);
    int T; cin>>T;
    REP(cases,T){
                 cin>>n>>s>>p;
                 REP(i,n){
                          cin>>pun;
                          v.push_back(pun);
                          }
                 REP(j,n){
                          int i = v[j]/3;
                          if(i>p) ans++;
                          else if(p==0) ans++;
                          else{
                          if(i&&(i*3)==v[j]){
                                             if(p==i+1&&s){
                                                             //cout<<v[j]<<" 1.1\n";
                                                             ans++;
                                                             s--;
                                                             }
                                               else{
                                                    if(p<=i){
                                                             //cout<<v[j]<<" 1.2\n";
                                                             ans++;
                                                             }
                                                    }
                                             }
                          if(i&&(i*3)+1==v[j]){
                                               if(p==i+1&&s){
                                                             //cout<<v[j]<<" 2.1\n";
                                                             ans++;
                                                             }
                                               else{
                                                    if(p<=i+1){
                                                               //cout<<v[j]<<" 2.2\n";
                                                               ans++;
                                                               }
                                                    }
                                               }
                          if(i&&(i*3)+2==v[j]){
                                               if(p==i+2&&s){
                                                             //cout<<v[j]<<" 3.1\n";
                                                             ans++;
                                                             s--;
                                                             }
                                               else{
                                                    if(p<=i+1){
                                                               //cout<<v[j]<<" 3.2\n";
                                                               ans++;
                                                               }
                                                    }
                                               }
                          }
                          }
                 cout<<"Case #"<<cases+1<<": "<<ans<<endl;
                 ans=0;
                 v.clear();
                 }
    //system("PAUSE");
}
