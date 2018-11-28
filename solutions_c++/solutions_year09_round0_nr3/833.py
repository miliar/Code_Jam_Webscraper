#include<iostream>
#include<string>
using namespace std;
#define REP(i,b,n) for(int i=b;i<n;i++)
#define rep(i,n)   REP(i,0,n)

string tar="welcome to code jam";
int table[20][500];

int solve(string & a){
  rep(i,tar.size()){
    rep(j,a.size()){
      table[i][j]=0;
    }
  }

  if ( a[0]==tar[0])table[0][0]=1;
  REP(i,1,a.size()){
    table[0][i]=table[0][i-1];
    if ( a[i] == tar[0])table[0][i]++;
    table[0][i]%=10000;
  }
  

  REP(i,1,tar.size()){
    REP(j,1,a.size()){
      if ( tar[i]==a[j])table[i][j]=(table[i][j]+table[i-1][j-1])%10000;
      table[i][j]=(table[i][j]+table[i][j-1])%10000;
    }
  }
  /*
  rep(i,tar.size()){
    rep(j,a.size()){
      cout << table[i][j]<< " " ;
    }
    cout << endl;
  }
  */

  return table[tar.size()-1][a.size()-1];
}

main(){
  string in;
  int te,tc=1;
  cin>>te;getline(cin,in);
  while(getline(cin,in)){
    printf("Case #%d: %04d\n",tc++,solve(in));
  }

}
