#include<iostream>
#include<complex>
#include<vector>
#include<string>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
#define SZ(X) ((int)X.size())
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define REP(I,N) for(int I=0;I<(N);I++)
#define SRT(X) sort((X).begin(),(X).end())
#define PB push_back
typedef vector<int> VI;
inline VI parsei(string s,char ch=' '){string a="";VI wyn;REP(i,(int)s.size()) if(s[i]!=ch) a+=s[i];else if(!a.empty()){wyn.PB(atoi(a.c_str()));a="";} if(!a.empty()) wyn.PB(atoi(a.c_str()));return wyn;}

int main(){
  int T;
  cin>>T;
  REP(TT,T){
    int N;
    string lin;
    VI plin;
    cin>>N;
    getline(cin,lin);
    getline(cin,lin);
    plin=parsei(lin);
    SRT(plin);
    int sum=0,x=0;
    FOR(i,1,SZ(plin)-1){sum+=plin[i];x^=plin[i];}
    if(plin[0]!=x) printf("Case #%d: NO\n",TT+1);
    else printf("Case #%d: %d\n",TT+1,sum);
  }
  return 0;
}
