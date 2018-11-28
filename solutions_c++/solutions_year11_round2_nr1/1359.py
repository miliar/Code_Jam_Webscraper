#include <cstdio>
#include <vector>
#include <set>
#include <queue>

using namespace std;

struct team {
  int id;
  vector<team*> wins;
  vector<team*> loses;

  double WP, OWP, OOWP;

  double gamesCount() {
    return (loses.size() + wins.size());
  }

  double winsCount() {
    return wins.size();
  }
  
  void computeWP() {
    WP =  winsCount() / gamesCount();
  }

  void computeOWP() {
    double tmpOWP = 0;
    for(int i = 0; i<wins.size(); i++) {
      team *opponent = wins[i];
      tmpOWP += opponent->winsCount() / (opponent->gamesCount()-1);
    }
    for(int i = 0; i<loses.size(); i++) {
      team *opponent = loses[i];
      tmpOWP += (opponent->winsCount()-1) / (opponent->gamesCount()-1);
    }
    OWP = tmpOWP / (wins.size() + loses.size());
  }

  void computeOOWP() {
    double tmpOOWP = 0;
    for(int i = 0; i<wins.size(); i++) {
      tmpOOWP += wins[i]->OWP;
    }
    for(int i = 0; i<loses.size(); i++) {
      tmpOOWP += loses[i]->OWP;
    }
    OOWP = tmpOOWP / (wins.size() + loses.size());
  }
  
  bool operator<(const team &other) const {
    return id < other.id;
  }
};

void solve() {
  int N; char c;
  scanf("%d\n", &N);
  vector<team> teams(N);
  for(int i = 0; i<N; i++) teams[i].id = i;
  
  for(int i = 0; i<N; i++) {
    teams[i].id = i;
    for(int j = 0; j<N; j++) {
      scanf("%c", &c);
      switch(c) {
      case '1':
	teams[i].wins.push_back(&teams[j]);
	break;
      case '0':
	teams[i].loses.push_back(&teams[j]);
	break;
      default: break;
      }
    }
    scanf("\n");
  }

  for(int i = 0; i<N; i++) {
    teams[i].computeWP();
    teams[i].computeOWP();
  }
  for(int i = 0; i<N; i++) {
    teams[i].computeOOWP();
  }
  for(int i = 0; i<N; i++) {
    team t = teams[i];
    printf("%.10g\n", 0.25 * t.WP + 0.50 * t.OWP + 0.25 * t.OOWP);
  }
}

int
main(int argc, char **argv) {
  int T;
  scanf("%d\n", &T);
  for(int i = 1; i <= T; i++) {
    printf("Case #%d:\n", i);
    solve();
  }
}
