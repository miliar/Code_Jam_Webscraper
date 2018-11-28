#include <iostream>
#include <vector>
#include <string>
#include <map>

//#include "cout.h"
using namespace std;

#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define tr(c,i)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

char msg[502], *salut="welcome to code jam";
int msg_len, salut_len=19;
map<pair<int,int>,long long> ht;

long long find_welcome(int msg_ix, int salut_ix)
{
  if (msg_len - msg_ix < salut_len - salut_ix) return 0LL;
  
  pair<int,int> key = make_pair(msg_ix,salut_ix);
  if (found(ht,key)) return ht[key];

  long long cnt = 0LL;
  if (msg[msg_ix] == salut[salut_ix]) {
    if (salut_ix == salut_len-1)
      cnt++;
    else
      cnt += find_welcome(msg_ix+1, salut_ix+1);
  }
  cnt += find_welcome(msg_ix+1, salut_ix);
  
  cnt %= 10000LL;
  
  ht[key] = cnt;

  return cnt;
}

main()
{
  int N;

  cin >> N;
  fgets(msg,501,stdin); // \n
  
  rep(n,N){
    ht.clear();
    
    fgets(msg,501,stdin);
    rep(i,strlen(msg)) if(msg[i]<0x20){ msg_len=i; msg[i]=0; break; }
    // printf("\nmsg#%d = \"%s\" (%d chars)\n", 1+n, msg, msg_len);

    long long cnt = find_welcome(0,0);
    printf("Case #%d: %04lld\n", 1+n, cnt);
  }
}
