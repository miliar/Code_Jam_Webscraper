#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string> 
#include <vector>

using namespace std;

#include <iostream>
#include <cmath>
#include <vector>
#include <iterator>
#include <list>
#include <set>

using namespace std;


int* primes;
int prime_calc;
int num_primes;

void  prime_sieve (int in = 100000) {
  prime_calc = (in>>1)+1;
  num_primes = 1;

  bool* prime_mark = new bool[prime_calc];

  int s = (int)sqrt((double)in)/2 + 1;

  fill_n (prime_mark, prime_calc, true);
  prime_mark[0] = false;

  for( int i=1; i<s; ++i ) {
    if (prime_mark[i]) {
      num_primes++;

      for (int j=3*i+1; j<prime_calc; j+=(2*i+1) )
        prime_mark[j] = false;
    }
  }

  for (int i = s; i <prime_calc; ++i) if ( prime_mark[i] ) num_primes++;
  primes = new int[num_primes];
  num_primes = 0;
  primes[num_primes++] = 2;
  for (int i=1; 2*i+1<=in; ++i) if (prime_mark[i]) primes[num_primes++] = 2*i+1;
  delete[] prime_mark;
  prime_calc = in;

}

struct Ufs {
  vector<int> elem;
  vector<int> tree_size;
  int size;
  
  Ufs (int n) :
    elem (n), tree_size (n,1),size (n) {

    for(int i=0; i<n; i++) {
      elem[i]  = i;
      tree_size[i] = 1;
    }
  }

  int find (int k)  {
    int pt = k;
    while( elem[pt] != pt ) pt = elem[pt];

    // path-compression
    int root = pt;
    for( pt=k; elem[pt]!=pt; pt=k ) {
      k = elem[pt];
      elem[pt] = root;
    }

    return root;
  }

  void unite (int r, int s ) {
    r = find (r);
    s = find (s);
    if (r!=s) --size;
    if( tree_size[r] >= tree_size[s] ) {
      elem[s]  = r;
      tree_size[r] = max(tree_size[r], tree_size[s] + 1);
    }
    else
      elem[r]  = s;
  }
};


int main() {
  prime_sieve ();
  cerr << num_primes << endl;



  int num_cases;
  cin >> num_cases;
  for (int case_num = 1; case_num <=num_cases; ++case_num) {
    cout << "Case #" << case_num << ": ";

    int a,b,p;
    cin >>a >> b >> p;

    Ufs ufs (b-a+1);

    for (int i = 0; i < num_primes && primes[i] <= b; ++i) {
      if (primes[i]<p) continue;
      int first = a - (a%primes[i]);
      if (first <a) first += primes[i];
      for (int j = first; j <= b; j+=primes[i]) {
        ufs.unite (first-a,j-a);
      }
    }
    cout << ufs.size << "\n";
  }
}
