#include <iostream>
#include <string>
#include <memory>
using namespace std;
string list [10000];
int fc[10000];
int br[10000];
int e = 0 ;
string getfir(string s) {
  unsigned int loc = s.find('/');
  if (loc == string::npos) return s;
  //cout << s.substr(0,loc)<< endl;
  return (s.substr(0,loc));
}
string getnxt(string s) {
  unsigned int loc = s.find('/');
  if (loc == string::npos) return "";
 // cout << s.substr(loc+1)<<endl; 
  return (s.substr(loc+1));
}

int it(int x, string s) {
    if (s.size()==0) return 0;
    string sq = getfir(s);
    string nxt = getnxt(s);    
    if (fc[x] == 0 ) {
      list[e] = sq;
      fc[x] = e;
      e++;  
      return it(fc[x],nxt)+1; 
    }
    int i = fc[x];
    while (br[i]!=0) {
       if (list[i]== sq) return it(i,nxt);
       i  = br[i];
    }
    if (list[i]==sq) return it(i,nxt);
    list[e] = sq;
    br[i] = e;
    e++;
    return it(br[i],nxt)+1;
}
int main()
{
    int nn; cin >> nn ; for (int n0= 1; n0<=nn; n0++) {
   int    ans = 0 ;
    e = 1 ;
    memset(fc,0,sizeof(fc));
    memset(br,0,sizeof(br));
    int n,m;
    cin >> n >> m;
    string k;
    for (int i = 0 ; i <n;  i++) {
        cin >> k;
        k = k.substr(1);
        it(0,k);
    }
    for (int i = 0 ; i <m; i++) {
        cin >> k;
        k = k .substr(1);
        ans+= it(0,k);
    }
    cout <<"Case #"<<n0<<": "<<ans<<endl;
    }
}
