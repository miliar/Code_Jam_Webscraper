#include "template.cc"

/*

 */


const char ul='/',ur='\\';
const char ll=ur,lr=ul;
const char w='.';
const char b='#';
char rc[50][50];

void solve()
{
  U R,C;
  read(R);read(C);
  U r,c;
  forn(r,R) {
    forn(c,C) {
      readq(rc[r][c]);
    }
  }
  forn(r,R) {
    forn(c,C) {
      if (rc[r][c]==b) {
        U r2=r+1,c2=c+1;
        if (r2<R&&c2<C&&rc[r2][c]==b&&rc[r2][c2]==b&&rc[r][c2]==b) {
          rc[r][c]=ul;
          rc[r][c+1]=ur;
          rc[r+1][c]=ll;
          rc[r+1][c+1]=lr;
        } else
          goto fail;
      }
    }
  }
  forn(r,R) {
    cout<<endl;
    forn(c,C) {
      cout<<rc[r][c];
    }
  }
  return;
fail:
  cout<<"\nImpossible";
}

