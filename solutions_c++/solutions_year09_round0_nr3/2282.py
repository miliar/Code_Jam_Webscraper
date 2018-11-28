#include<cstdio>
#include<iostream>
#include<string>
#include<sstream>
#include<vector>

#define PB push_back

using namespace std;

typedef vector<string> VS;
typedef vector<int> VI;
typedef vector<vector<int> > VVI;

inline string stringify(int x){ostringstream o; o << x; return o.str();}

const char pattern[]="welcome to code jam";
const int pl=19;

inline int matches(string w){
  VI r(w.size(), 0);
  VVI t(pl, r);
  int i=0, j=0, s=0;
  for(i=0; i<(int)w.size(); i++) if(pattern[0]==w[i]) t[0][i]=++s; else t[0][i]=s;
  for(i=1; i<pl; i++){
    for(j=1; j<(int)w.size(); j++) if(w[j]==pattern[i]) t[i][j]=(t[i][j-1]+t[i-1][j-1])%10000; else t[i][j]=t[i][j-1];
  }
  return t[pl-1][(int)w.size()-1];
}

int N=0;
int main(){
  string pom="",pom2="";
  int i=0;
  int w=0;
  cin >> N; 
  getline(cin,pom); 
  for(i=0; i<N; i++){
    getline(cin,pom);     
    cout << "Case #" << (i+1) << ": "; 
    w=matches(pom);
    pom2=stringify(w);
    switch((int)pom2.size()){
      case 1: pom2="000"+pom2; break;
      case 2: pom2="00"+pom2; break;
      case 3: pom2="0"+pom2; break;
      case 4: break;
      default: pom2="0000";
    }
    cout << pom2<< "\n";
  }
  return 0;
}
