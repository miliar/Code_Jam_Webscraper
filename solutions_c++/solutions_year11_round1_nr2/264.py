#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <cmath>

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define gp(ans) {cout << "Case #" << ((test)+1) << ": " << (ans) << endl;}

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

int contain (string s, char c){
  int n=s.size();
  int i;
  int r=0;
  REP(i,n){
    if(s[i]==c){
      r += (1 << i);
    }
  }
  return r;
}

int main () {
  int test, T;

  cin >> T;
  REP (test, T) {
    int n,m;
    string r ="";
    cin >> n >> m;
    vs wv(n);
    int i,j;
    REP(i,n){
      string s;
      cin >> s;
      wv[i] = s;
    }
    REP(i,m){
      string l;
      cin >> l;
      int maxp=-1;
      string maxw;
      REP(j,n){
        // check when select the j'th word
        int point=0;
        vi cand(n);
        string w=wv[j];
        //printf("check %s\n", w.c_str());
        int p,q;
        int size = w.size();
        REP(p,n){
          if(wv[p].size() == size){
            cand[p]=1;
          }
        }
        int k;
        REP(k,l.size()){
          //try k'th letter
          int find=0;
          char c=l[k];
          vi posvec(n);
          REP(p,n){
            if(cand[p]){
              // is possible
              int pos = contain(wv[p], c);
              posvec[p]=pos;
              if (pos) find=1;
            }
          }
          if(find){
            //printf("  find cand\n");
            //printf(" try %c\n", c);
            int same=0;
            if(!posvec[j]){
              //printf(" #loose point\n");
              point++;
            }
            REP(p,n){
              if(p==j) continue;
              if(posvec[p]==posvec[j]){
                same++;
              }else{
                cand[p]=0;
              }
            }
            if(same){
              continue;
            }else{
              //end
              goto A;
            }
          }
        }
      A:
        if(maxp < point){
          maxp=point;
          maxw=w;
        }
      } // j'th word end
      if (r != "") r += " ";
      r+= maxw;
    }
    gp(r);
  }
  return 0;
}

