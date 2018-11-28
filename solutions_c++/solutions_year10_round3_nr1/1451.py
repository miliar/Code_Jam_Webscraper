#include <iostream>
#include <vector>
#include <stdlib.h>
#include <list>
#include <algorithm>

using namespace std;

struct rope {
  int a;
  int b;
};

bool
cmpa(rope *r0, rope *r1)
{
  return r0->a < r1->a;
}

bool
cmpb(rope *r0, rope *r1)
{
  return r0->b < r1->b;
}

int
main()
{
  int ncases, i;

  cin >> ncases;
  for (i = 1; i <= ncases; i++) {
    int nropes;
    vector <rope *> ropes;
    cin >> nropes;

    for (int j = 0; j < nropes; j++) {
      rope *r = new rope;
      cin >> r->a >> r->b;
      ropes.push_back(r);
    }
    sort(ropes.begin(), ropes.end(), cmpb);
    for (int j = 0; j < nropes; j++) {
      ropes[j]->b = j;
    }

    int n = 0;
    sort(ropes.begin(), ropes.end(), cmpa);
    for (int j = 0; j < nropes; j++) {
      if (ropes[j]->b > j) {
	n += ropes[j]->b - j;
      }
    }
    cout << "Case #" << i << ": " << n << endl;
  }
  return 0;
}
