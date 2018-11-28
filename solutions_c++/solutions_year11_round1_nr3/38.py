
#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <cmath>
#include <complex>
#include <numeric>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
#define FOR(i,s) for(__typeof((s).begin()) i = (s).begin(); i != (s).end(); ++i)
#define ALLOF(s) ((s).begin()), ((s).end())

typedef long long integer;

struct Card {
  int c;
  int s;
  int t;
};

bool operator <(const Card& a, const Card& b) {
  return a.s < b.s;
}

typedef priority_queue<Card, vector<Card>, less<Card> > PQ;

int nHand;
int nDeck;
Card cards[100];

int solve(PQ rest0, PQ rest1, int pos, int turn) {
  if(turn <= 0)
    return 0;
//   cerr << rest0.size() << " " << rest1.size() << endl;
  
  if(pos >= nHand + nDeck){ // 全部手札。sが大きいものから使う
    PQ q;
    while(!rest0.empty()){
      q.push(rest0.top());
      rest0.pop();
    }
    while(!rest1.empty()){
      q.push(rest1.top());
      rest1.pop();
    }
    int res = 0;
    while(turn > 0 && !q.empty()){
      res += q.top().s;
      q.pop();
      turn--;
    }
    return res;
  }
  
  // rest1から使う場合
  int res1 = 0;
  if(!rest1.empty()){
    int draw = rest1.top().c; // 1
    res1 += rest1.top().s;
    int nextturn = turn + rest1.top().t;
    if(nextturn > 0){
      PQ nextrest0 = rest0;
      rest1.pop();
      for(int i = pos; i < pos + draw && i < nHand + nDeck; ++i){
	Card& c = cards[i];
	if(c.t >= 0){
	  res1 += c.s;
	  draw += c.c;
	  nextturn += c.t;
	}else{
	  if(c.c == 0){
	    nextrest0.push(c);
	  }else{
	    rest1.push(c);
	  }
	}
      }
      res1 += solve(nextrest0, rest1, pos+draw, nextturn);
    }
  }
  
  // rest1から使わない場合、rest0からできるだけ使う
  int res0 = 0;
  for(int t = 0; t < turn && !rest0.empty(); ++t){
    res0 += rest0.top().s;
    rest0.pop();
  }
  return max(res1, res0);
}



int main(void) {
  int nCases;
  cin >> nCases;
  REP(iCase, nCases) {

    cin >> nHand;
    REP(i, nHand){
      Card& c = cards[i];
      cin >> c.c >> c.s >> c.t;
      c.t--;
    }
    cin >> nDeck;
    REP(i, nDeck){
      Card& c = cards[i+nHand];
      cin >> c.c >> c.s >> c.t;
      c.t--;
    }
    
    PQ rest0, rest1;
    int res = 0;
    int turn = 1;
    int pos = nHand;
    for(int i = 0; i < pos && i < nHand + nDeck; ++i){
      Card& c = cards[i];
      if(c.t >= 0){
// 	cerr << "use(t>=0) " << i << endl;
	res += c.s;
	pos += c.c;
	turn += c.t;
      }else{
	if(c.c == 0){
	  rest0.push(c);
	}else{
	  rest1.push(c);
	}
      }
    }
    
    res += solve(rest0, rest1, pos, turn);
    cout << "Case #" << (iCase+1) << ": " << res << endl;
  }
  
  return 0;
}
