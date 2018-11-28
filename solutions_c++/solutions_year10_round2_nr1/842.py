#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <iterator>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <queue>
#include <vector>
using namespace std;
 
typedef long long LL;
 
#define MP make_pair
#define ST first
#define ND second
#define ALL(k) k.begin(),k.end()
#define PB push_back
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOREACH(i,v) for(__typeof((v).begin())i=(v).begin();i!=v.end();++(i))
#define SZ(a) (int)((a).size())

int main()
{
  int tst,tstn;
  cin >> tstn;

  REP(tst,tstn)
  {
    LL wyn = 0;
    cout << "Case #" << tst+1 << ": ";
    set < string > S;
    int N,M;
    cin >> N >> M;
    REP(i,N)
    {
      string tmp;
      cin >> tmp;
      REP(i,tmp.size()) if(tmp[i] == '/') tmp[i] = ' ';
      istringstream is(tmp);
      string W = "";
      string pam;
      while( is >> pam)
      {
        W += pam + " ";
        S.insert(W);
      }
    }
    
    REP(i,M)
    {
      string tmp;
      cin >> tmp;
      REP(i,tmp.size()) if(tmp[i] == '/') tmp[i] = ' ';
      istringstream is(tmp);
      string W = "";
      string pam;
      while( is >> pam)
      {
        W += pam + " ";
        if(S.count(W) == 0) wyn++;
        S.insert(W);        
      }
    }    
     
    cout << wyn << endl;
  }
  return 0;
}
