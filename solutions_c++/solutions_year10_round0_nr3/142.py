// theme
// srh

#include <iostream>
#include <vector>
#include <stdint.h>

using std::vector;
using std::pair;

typedef int64_t state;

// Doubles the effects, using tmp as a temporary buffer.
void doubleTheEffects(vector< pair<state, int64_t> >& effects,
		      vector< pair<state, int64_t> >& tmp) {
  int64_t n = effects.size();
  // We'd like to fill tmp[i] with the answer "what is the effect
  // after two state changes from i through effects?"

  for (int64_t i = 0; i < n; ++i) {
    pair<state, int64_t> e1 = effects[i];
    pair<state, int64_t> e2 = effects[e1.first];
    tmp[i] = pair<state, int64_t>(e2.first, e1.second + e2.second);
  }

  effects.swap(tmp);
}


vector< pair<state, int64_t> >
computeOneRideEffects(int64_t k, const vector<int64_t>& g) {
  int64_t totalPassengers = 0;
  int64_t n = g.size();
  for (int64_t i = 0; i < n; ++i) {
    totalPassengers += g[i];
  }
  if (totalPassengers <= k) {
    // Pathological case
    vector< pair<state, int64_t> > effects;
    for (state s = 0; s < n; ++s) {
      effects.push_back(pair<state, int64_t>(s, totalPassengers));
    }
    return effects;
  } else {
    // We have to do this in O(n) time and not O(n^2) time,
    // unfortunately.

    vector< pair<state, int64_t> > effects;

    int64_t i = 0;
    int64_t j = 0;
    // p is the number of passengers in g in the range [i,j)
    int64_t p = 0;
    // We're going to increment i one step at a time...
    while (i < n) {
      // Increment j until just before p has passed k.
      for (;;) {
	int64_t tmp = g[j % n];
	if (p + tmp > k) {
	  goto done;
	}
	p = p + tmp;
	j = j + 1;
      }
    done:
      // j is the state that follows from i, with p being the
      // population that rides.
      effects.push_back(pair<state, int64_t>(j % n, p));

      // Now increment i and do it again.
      p = p - g[i];
      i = i + 1;
    }

    return effects;
  }
}

int64_t calculate_euros(int64_t R, int64_t k, const vector<int64_t>& g) {
  int64_t eurocount = 0;
  int64_t numRides = 1;
  state theState = 0;
  vector< pair<state, int64_t> > effects = computeOneRideEffects(k, g);
  vector< pair<state, int64_t> > tmp(effects);

  while (numRides <= R) {
    if (R & numRides) {
      state nextState = effects[theState].first;
      eurocount = eurocount + effects[theState].second;
      theState = nextState;
    }
    doubleTheEffects(effects, tmp);
    numRides = (numRides << 1);
  }
  return eurocount;
}


int main() {

  /*
    Input

    The first line of the input gives the number of test cases, T.
  */
  // 1 <= T <= 50
  int64_t T;
  std::cin >> T;

  /*
    T test cases follow, with each test case consisting of two lines.
  */

  for (int64_t caseNumber = 1; caseNumber <= T; ++caseNumber) {
    /*
      The first line contains three space-separated integers: R, k and
      N.
    */
    // 1 <= R <= 10^8
    int64_t R;
    std::cin >> R;
    // 1 <= k <= 10^9
    int64_t k;
    std::cin >> k;
    // 1 <= N <= 1000
    int64_t N;
    std::cin >> N;

    /* The second line contains N space-separated integers gi, each of
       which is the size of a group that wants to ride. */
    // 1 <= g_i <= 10^7.
    vector<int64_t> g;
    for (int64_t i = 0; i < N; ++i) {
      int64_t g_i;
      std::cin >> g_i;
      g.push_back(g_i);
    }

    // The number of euros paid is no greater than R*k, which is
    // 10^17.

    int64_t euros = calculate_euros(R, k, g);

    std::cout << "Case #" << caseNumber << ": " << euros << "\n";
  }
}
