#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<cmath>
#include<map>
#include<cstdlib>
#include<climits>
#include<cstring>
#include<queue>
#include<deque>
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
#define INF 99999999
#define EPS 0.0001
using namespace std;
typedef long long ll;
map<char,char>tr;
map<char,char>ex;
int main(){
  tr['a']='y';  tr['b']='h';  tr['c']='e';
  tr['d']='s';  tr['e']='o';  tr['f']='c';
  tr['g']='v';  tr['h']='x';  tr['i']='d';
  tr['j']='u';  tr['k']='i';  tr['l']='g';
  tr['m']='l';  tr['n']='b';  tr['o']='k';
  tr['p']='r';  tr['q']='z';  tr['r']='t';
  tr['s']='n';  tr['t']='w';  tr['u']='j';
  tr['v']='p';  tr['w']='f';  tr['x']='m';
  tr['y']='a';  tr['z']='q';  
  int n; scanf("%d\n",&n);  
  REP(j,n){
    string st;
    string h;
    getline(cin,st);
    //    getline(cin,h);
    // cout<<"hoge";
    // REP(i,st.size())
    //   ex[st[i]]=h[i];
    // for(map<char,char>::iterator it=ex.begin();it!=ex.end();++it)
    //   cout<<(*it).first<<"->"<<(*it).second<<endl;
    string res=st;
    REP(i,res.size())
      if(tr.find(res[i])!=tr.end()) res[i]=tr[res[i]];
    
    cout<<"Case #"<<j+1<<": "<<res<<endl;
  }
}
