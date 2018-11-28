#include "template.cc"

/*
  straightforward. maintain list of opponents of each team, and total wins/losses. then if you played them, OWP = win-(1 if you lost to them, else 0) / total-1 (excluding your game)

  no teams play more than once

  avg OWP (OOWP) is easy
 */

double N;
typedef tuple<int,bool> T;
vector<vector<T> > played;
vector<double> owps;
struct wp {
  double won;
  double total;
  wp() : won(),total() {}
  void record(bool we_won) {
    if (we_won) ++won;
    ++total;
  }
  double WP() const { return won/total; }
  double forOWP(bool this_won) const {
    return (this_won ? (won-1) : won) / (total-1);
  }
};
vector<wp> rec;
void init(int N) {
  rec.clear();
  owps.clear();
  played.clear();
  rec.resize(N);
  owps.resize(N);
  played.resize(N);
}
void readwp(char c,int from,int to) {
  debugm("readwp",c,from,to);
  if (c=='.') return;
  bool from_won=(c=='1');
  rec[from].record(from_won);
  //rec[to].wp(to_won); // don't need reverse dir because full matrix is given as input.
  played[from].push_back(T(to,from_won)); // also don't need reverse of this
  wp &t=rec[to];
}

double OWP(int from) { // every team plays 2 other teams or more so excluding self is ok
  double sum=0;
  for(T p : played[from]) {
    int they=get<0>(p);
    bool they_won=!get<1>(p);
    sum+=rec[they].forOWP(they_won);
  }
  return sum/played[from].size();
}

double OOWP(int from) {
  double sum=0;
  for(T p : played[from]) // no team plays itself
    sum+=owps[get<0>(p)];
  return sum/played[from].size();
}

void solve()
{
  int N;
  read(N);
  init(N);
  char c;
  fi(N)
    for (int j=0;j<N;++j) {
      read(c);
      readwp(c,i,j);
    }
  fi(N)
    owps[i]=OWP(i);
  fi(N) {
    double rpi=(rec[i].WP()+2*owps[i]+OOWP(i))/4;
    cout<<'\n'<<setprecision(12)<<rpi;
  }
}

