#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
#define SL size()
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MP make_pair
#define X first
#define Y second
#define LE length()
#define PB push_back

int L,D,Q;
char dic[5005][17];

int howMany(vector<string> &vs){
    int res=0;
    for(int d=0;d<D;d++){
       bool ok=true;
       for(int l=0;l<L;l++){
           if( vs[l].find(dic[d][l]) == string::npos){ ok=false; break;}
       }
       if(ok)res++;
    }
    return res;
}


int main(){
    cin>>L>>D>>Q;
    for(int d=0;d<D;d++) for(int l=0;l<L;l++)cin>>dic[d][l];
    for(int q=1;q<=Q;q++){
       string s; cin>>s;
       vector<string> vs;
       for(int i=0;i<(int)s.LE;i++){
          string ac="";
          if(s[i]!='('){ ac.PB(s[i]); vs.PB(ac); continue;}
          i++;
          while(i<(int)s.LE && s[i]!=')'){
              ac.PB(s[i]); i++;
          }
          vs.PB(ac);
          
       }
       int res = howMany(vs);
       cout<<"Case #"<<q<<": "<<res<<endl;
    }
}
