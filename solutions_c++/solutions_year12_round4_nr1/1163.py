#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define FE(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define FI(c) for (ll i = 0; i < c; i++)
#define FJ(s,c) for (ll j = s; j < c; j++)
#define MP(X,Y) make_pair(X,Y)

#define _X(x,y) (((y)*DX)+(x))
// end boilerplate code...


// redo, reach a vine with the max swing
map<ll, ll> vines;
map<ll, ll> maxswing;

void swingat(ll pos, ll swing) {
  if (maxswing[pos] >= swing) return;
  maxswing[pos] = swing;
  map<ll, ll>::iterator newvine = vines.find(pos);
  while(1) {
    newvine++;
    if (newvine == vines.end()) break;
    if (newvine->first > (pos+swing)) break;

    // reachable
    swingat(newvine->first, min(newvine->second, newvine->first - pos));
  }
}

void runcase() {
  vines.clear();
  maxswing.clear();
  ll N, D;
  cin >> N;
  FI(N) {
    ll d, l;
    cin >> d >> l;
    vines[d] = l;
    maxswing[d] = 0;
  }
  cin >> D;

  swingat(vines.begin()->first, vines.begin()->first);

  FE(i, maxswing) {
    //cout << "max " << i->first << " is " << i->second << endl;
    if (i->first+i->second >= D) {
      cout << "YES"; return;
    }
  }
  cout << "NO";

  /*ll pos, swing;
  pos = vines.begin()->first;
  swing = pos;

  
  // swing as far as possible
  cout << "target is " << D << endl;
  FE(i, vines) {
    cout << i->first << "  " << i->second << endl;
  }

  while(1) {
    cout << "at " << pos << " with " << swing << endl;
    //map<ll, ll>::iterator newvine = vines.upper_bound(pos+swing);
    map<ll, ll>::iterator newvine = vines.find(pos);
    map<ll, ll>::iterator savevine = newvine;

    map<ll, ll>::iterator maxvine = newvine;
    ll maxnum = 0;

    while(1) {
      newvine++;
      if (newvine == vines.end()) break;
      //cout << "  reaaching for " << newvine->first << "  " << newvine->second << endl;
      if (newvine->first > (pos+swing)) break;

      // reachable
      //cout << "reached" << endl;

      ll tmaxnum = newvine->first + min(newvine->second, newvine->first-pos);
      if (tmaxnum > maxnum) {
        maxnum = tmaxnum;
        maxvine = newvine;
      }
    }

    if (maxvine == savevine) break;

    //if (newvine->first == pos) break;

    swing = min(maxvine->second, maxvine->first-pos);
    pos = maxvine->first;
  }

  if ((pos+swing) >= D) cout << "YES";
  else cout << "NO";*/
}

int main(int argv, char* argc[]) {
  cout << setprecision(9);
  int case_count;
  cin >> case_count;
  for (int i = 0; i < case_count; i++) {
    cout << "Case #" << (i+1) << ": ";
    runcase();
    cout << endl;
  }
}

