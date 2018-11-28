#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
#define forn(i,n) for(int i=0; i<(int)(n); i++)
#define pb push_back
int main(){
    ifstream in("gcj.in");
    ofstream out("gcj.out");
    int m; in>>m;
    forn(t,m){
      out<<"Case #"<<t+1<<": ";
      int n, p, s;
      in>>n>>s>>p;
      vector<int> v;
      forn(i,n){
        int val; in>>val;
        v.pb(val);
      }
      sort(v.rbegin(), v.rend());
      int res=0;
      forn(i,n){
        if(v[i]==0 && p==0)res++;
        int k=v[i]/3;
        if(v[i]%3==0 && v[i]!=0){
          if(k>=p)res++;
          else if(k+1>=p && s>0){s--; res++;}
        }
        if(v[i]%3 == 1){
          if(k+1>=p)res++;
          }
        if(v[i]%3 == 2){
            if(k+1>=p)res++;
            else if(k+2>=p && s>0){s--; res++;}
          }
      }
    out<<res<<endl;
    }
    }
