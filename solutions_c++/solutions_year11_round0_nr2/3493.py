#include "template.cc"

/* actual solution follows */

const int A=26;
typedef int elt;

void init() {  }

#define readord(a) readq(ch);a=ucord(ch)
void solve()
{
  vector<vector<elt> > destroys(A); // list of things that can destroy[e]
  vector<vector<elt> > trans(A,vector<elt>(A)); // 0 = no transformation. i>0 = transforms to i-1
  char ch;
  elt a,b,c;
  for_fields(i) {
    readord(a);readord(b);readord(c);
    trans[a][b]=trans[b][a]=c+1;
    debug(a,b,trans[a][b],trans[b][a]);
  }
  read(nfields);
  for_fields(i) {
    readord(a);readord(b);
    destroys[a].push_back(b);
    destroys[b].push_back(a);
    debug(a,b,destroys[a]);
    debug(a,b,destroys[b]);
  }
  read(nfields);
  counted_stack<elt,vector<int> > ords(A);
  for_fields(i) {
    readord(a);
    debug(ords,a);
    if (!ords.empty()) {
      b=ords.back();
      elt c=trans[b][a];
      if (c) {
        debugm(translate,b,a,c);
        ords.pop();
        ords.push_back(c-1);
        goto next;
      } else {
        for (elt d : destroys[a]) {
          if (ords.n[d]) {
            debugm(clear,d,a);
            ords.clear();
            assert(ords.n[d]==0);
            goto next;
          }
        }
      }
    }
    ords.push(a);
  next: ;
  }
  cout<<mapv(ords,orduc);
}
