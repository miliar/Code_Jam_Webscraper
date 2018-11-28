#include <iostream>
#include <iomanip>
#include <sstream>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

typedef long long LL;

int main()
{
  string a[3],b[3];
  int c[256];
  memset(c,-1,sizeof(c));
  a[0]=string("ejp mysljylc kd kxveddknmc re jsicpdrysi");
  a[1]=string("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
  a[2]=string("de kr kd eoya kw aej tysr re ujdr lkgc jv");
  b[0]=string("our language is impossible to understand");
  b[1]=string("there are twenty six factorial possibilities");
  b[2]=string("so it is okay if you want to just give up");

  for(int i=0;i<3;i++){
    for(int j=0;j<a[i].size();j++){
      c[a[i][j]]=b[i][j];
    }
  }
  c['q']='z';
  c['z']='q';
/*
  for(int i='a';i<='z';i++){
    cout<<(char)i<<"->";
    if(c[i]!=-1)cout<<(char)c[i];
    cout<<endl;
  }
*/

  int T;
  string S;
  cin>>T;
  getline(cin,S);

  for(int i=0;i<T;i++){
    getline(cin,S);
    cout<<"Case #"<<i+1<<": ";
    for(int k=0;k<S.size();k++){
      cout<<(char)c[S[k]];
    }
    cout<<endl;
  }

  return 0;
}
