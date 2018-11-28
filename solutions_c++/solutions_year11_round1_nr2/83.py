#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<cstdio>
#include<climits>
#include<cmath>
#include<cstring>
#include<string>
#include<sstream>
#include<numeric>
#include<cassert>

#define f first
#define s second
#define mp make_pair

#define REP(i,n) for(int i=0; i<(int)(n); i++)
#define rep(i,s,n) for(int i=(s); i<(int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define ALL(c) (c).begin(), (c).end()
#define IN(x,s,g) ((x) >= (s) && (x) < (g))
#define ISIN(x,y,w,h) (IN((x),0,(w)) && IN((y),0,(h)))
#define print(x) printf("%d\n",x)

using namespace std;

typedef unsigned int uint;
typedef long long ll;

const int _dx[] = {0,1,0,-1};
const int _dy[] = {-1,0,1,0};

int getInt(){
  int ret = 0,c;
  c = getchar();
  while(!isdigit(c)) c = getchar();
  while(isdigit(c)){
    ret *= 10;
    ret += c - '0';
    c = getchar();
  }
  return ret;
}

char words[10000][12];
int lens[10000];
int id[10000];
int memo[10000][30];

int main(){
  int ccc; scanf("%d", &ccc);
  REP(cc, ccc){
    int n, m;
    scanf("%d%d", &n, &m);

    printf("Case #%d:", cc+1);

    REP(i, n){
      scanf("%s", words[i]);
      lens[i] = strlen(words[i]);
    }

    for(char c = 'a'; c <= 'z'; c++){
      REP(i,n){
        int flag = 0;
        REP(j,lens[i]){
          if(words[i][j] == c){
            flag |= (1 << j);
          }
        }
        memo[i][c - 'a'] = flag;
      }
    }

    int idCnt_s = 0;
    {
      map<int, int> mm;
      REP(i,n){
        if(mm.count(lens[i]) == 0){
          mm[lens[i]] = idCnt_s++;
        }
        id[i] = mm[lens[i]];
      }
    }

    REP(k, m){
      char buff[30]; scanf("%s", buff);
      int que[26];   REP(i, 26) que[i] = buff[i] - 'a';
      int idCnt = idCnt_s;

      vector<pair<int, list<int> > > group(n);
      REP(i,n)
        group[id[i]].s.push_back(i);

      REP(i,26){
        char q = que[i];
        int ggg = idCnt;

	bool ok = true;
	REP(gg, ggg){
	  if(group[gg].s.size() != 1){
	    ok = false;
	    break;
	  }
	}
	if(ok) break;

        REP(gg, ggg){
          int point = group[gg].f;
          list<int> &s = group[gg].s;
          map<int, int> mapping;

          // printf("group %d(%d): ", gg, point); FOR(it, s) printf("%s ", words[*it]); puts("");

          if(s.size() == 1) continue;

          list<int>::iterator it = s.begin();
          mapping[memo[*it][q]] = gg;

          while(it != s.end()){
            int i = *it;
            int next;

            if(mapping.count(memo[i][q]) == 0){
              mapping[memo[i][q]] = idCnt;
              group[idCnt++].f = point + (memo[i][q] == 0 ? 1 : 0);
            }

            next = mapping[memo[i][q]];
            if(next != gg){
              group[next].s.push_back(i);
              it = s.erase(it);
            }else{
              ++it;
            }

          }

          if(mapping.size() != 1 && memo[*s.begin()][q] == 0)
            group[gg].f++;
        }
      }

      int maxpoint = 0;
      int maxid    = 0;
      REP(i, idCnt){
        if(maxpoint < group[i].f){
          maxpoint = group[i].f;
          maxid    = *group[i].s.begin();
        }else if(maxpoint == group[i].f){
	  maxid    = min(maxid, *group[i].s.begin());
	}
      }

      printf(" %s", words[maxid]);
    }
    puts("");
  }

  return 0;
}
