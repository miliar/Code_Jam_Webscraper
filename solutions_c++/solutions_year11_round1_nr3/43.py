#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

#define maxn 88
#define psb push_back

struct cardtype {
public:
  int c, s, t;
  cardtype() {}
  cardtype(int x, int y, int z) : c(x), s(y), t(z) {}
};

int T, n, m;
vector<cardtype> hand, deck;
int score, turns;

bool compare_s(const cardtype a, const cardtype b) {
  return a.s < b.s;
}

int find_turn(vector<cardtype> &h) {
  for(int i = 0; i < h.size(); i++)
    if (h[i].t > 0) return i;
  return -1;
}

int find_maxdraw(vector<cardtype> &h) {
  int max1 = -1, max2 = -1;
  for(int i = 0; i < h.size(); i++)
    if (h[i].c > 0 && h[i].s > max1) {
      max1 = h[i].s;
      max2 = i;
    }
  return max2;
}

void doit(vector<cardtype> &h, vector<cardtype> &d, cardtype &tmp, int &score, int &turns) {
  if (tmp.c > 0 && d.size() > 0) {
    h.psb(d[0]);
    d.erase(d.begin());
  }
  score += tmp.s;
  turns += tmp.t;
}

int evaluate(int remaining) {

  vector<cardtype> h;
  vector<cardtype> d;
  
  h = hand;
  d = deck;
  
  int score = 0, turns = 1;

  while (1) {
    int p = find_turn(h);
    if (p == -1) break;
    cardtype tmp = h[p];
    h.erase(h.begin() + p);
    doit(h, d, tmp, score, turns);
    turns --;
  }
  
 // cerr << "score1 = " << score << endl;
  
  while (d.size() > remaining && turns > 0) {
    int p = find_maxdraw(h);
    if (p == -1) break;
    cardtype tmp = h[p];
    h.erase(h.begin() + p);
    doit(h, d, tmp, score, turns);
    turns --;
    if (turns == 0) break;
    while (1) {
      int p = find_turn(h);
      if (p == -1) break;
      cardtype tmp = h[p];
      h.erase(h.begin() + p);
      doit(h, d, tmp, score, turns);
      turns --;
    }     
  }
  
 // cerr << "score2 = " << score << endl;  
 // cerr << "h.size = " << h.size() << endl;
  
  for(int i = 0; i < h.size(); i++)
    for(int j = i+1; j < h.size(); j++)
      if (h[j].s < h[i].s) swap(h[i], h[j]);
  while (h.size() > 0 && turns > 0) {
   /* doit(h, d, h[h.size()-1], score, turns);
    h.erase(h.end()-1);
    turns --;
    if (turns == 0) break;
    while (1) {
      int p = find_turn(h);
      if (p == -1) break;
      cardtype tmp = h[p];
      h.erase(h.begin() + p);
      doit(h, d, tmp, score, turns);
      turns --;
    } 
    sort(h.begin(), h.end(), compare_s);    */
    score += h[h.size()-1].s;
    h.erase(h.end()-1);
    turns --;
  }
  
 // cerr << "score3 = " << score << endl;  
  
  return score;

}

int main() {

  freopen("C-small.in", "rt", stdin);
  freopen("C-small.out", "wt", stdout);
  
  scanf("%d", &T);
  for(int cT = 0; cT < T; cT++) {
  
    scanf("%d", &n);
   // cerr << "n = " << n << endl;
    hand.clear(); deck.clear();
    for(int i = 0; i < n; i++) {
      int t1, t2, t3; scanf("%d%d%d", &t1, &t2, &t3);
      hand.psb(cardtype(t1, t2, t3));
    }
    scanf("%d", &m);
    for(int i = 0; i < m; i++) {
      int t1, t2, t3; scanf("%d%d%d", &t1, &t2, &t3);    
      deck.psb(cardtype(t1, t2, t3));
    }
    
    int tmax = 0;
    for(int i = deck.size(); i >= 0; i--) {
      int t = evaluate(i);
     // cerr << "t = " << t << endl;
      if (t > tmax) tmax = t;
    }
    printf("Case #%d: %d\n", cT+1, tmax);
  
  }
  
  return 0;

}
