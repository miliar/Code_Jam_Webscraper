#include <iostream>
#include <numeric>
#include <vector>
#include <map>


#define ALL(x) (x).begin(), (x).end()
#define EACH(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); ++ i)


std::vector<long long> S;

int N;

long long s;


typedef std::pair<long long, std::pair<long long, long long> > key_t;

std::map<key_t, bool> memo;


bool search(int i, long long j, long long k)
{
  key_t key(i, std::make_pair(j, k));

  if (memo.count(key))
    return memo[key];

  bool& r = memo[key];

  if (j > s / 2 || k > s / 2)
    return r = false;

  if (i && j == k)
    return r = true;

  if (i == N)
    return r = false;

  return r =
    search(i + 1, j + S[i], k)        ||
    search(i + 1, j,        k + S[i]) ||
    search(i + 1, j,        k);
}


int main(int argc, char** argv)
{
  int T;

  std::cin >> T;

  for (int t = 0; t < T; t ++) {
    std::cin >> N;

    S.resize(N);
    
    EACH(it, S)
      std::cin >> *it;

    std::random_shuffle(ALL(S));

    s = std::accumulate(ALL(S), 0);

    memo.clear();

    std::cout << "Case #" << t + 1 << ':' << std::endl;
    
    if (search(0, 0, 0)) {
      std::vector<long long> a, b;

      long long j = 0, k = 0;

      for (int i = 0; i == 0 || j != k; i ++) {
	key_t key;

	key = key_t(i + 1, std::make_pair<long long, long long>(j + S[i], k));

	if (memo[key]) {
	  a.push_back(S[i]);

	  j += S[i];

	  continue;
	}

	key = key_t(i + 1, std::make_pair<long long, long long>(j, k + S[i]));

	if (memo[key]) {
	  b.push_back(S[i]);

	  k += S[i];

	  continue;
	}
      }

      for (int i = 0; i < a.size() - 1; i ++)
	std::cout << a[i] << ' ';

      std::cout << a.back() << std::endl;

      for (int i = 0; i < b.size() - 1; i ++)
	std::cout << b[i] << ' ';

      std::cout << b.back() << std::endl;
    }
    else {
      std::cout << "Impossible" << std::endl;
    }
  }
}
