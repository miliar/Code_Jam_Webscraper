#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <list>
#include <queue>
#include <deque>

using namespace std;

#define FOR(i,a,b) for(int i=(a); i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define itype(c) __typeof((c).begin())
#define FORE(c,i) for(itype(c) i=(c).begin();i!=(c).end();++i)
#define PB push_back
#define PF pop_front
#define SORT(c) sort((c).begin(),(c).end());
#define SZ size()
#define PI acos(-1.)
#define HAS(c,e) (find((c).begin(),(c).end(),e)!=(c).end())
#define CHOMP string chomp;getline(cin,chomp)

typedef unsigned long long int ULL;

bool dividesEachOther(int x, int y) {
  if(x>y){ int tmp=x; x=y; y=tmp; }
  return y % x == 0;
}

int main()
{
  int Case;
  cin>>Case;
  REP(_case,Case)
  {
    int N,L,H; cin>>N>>L>>H;
    vector<int> notes;
    REP(i,N) { int tmp;cin>>tmp;notes.PB(tmp); }
    bool notesFound=false;
    int i=L;
    while(!notesFound && i<=H) {
      bool dividesAllNotes=true;
      FORE(notes,j) { if(!dividesEachOther(i,*j)) {dividesAllNotes=false;break;} }
      if(dividesAllNotes) { notesFound=true; }
      else { i++; }
    }

    
    printf("Case #%d: ",_case+1);
    if(!notesFound) cout << "NO"<<endl;
    else cout<<i<<endl;
  }

  return 0;
}
