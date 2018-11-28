#include <iostream>
#include <set>

std::set<unsigned> t[2<<20];

unsigned p[10];

inline unsigned width(unsigned x)
{
  unsigned i = 1;
  for (; i < 10; ++i) {
    if (p[i] > x)
      break;
  }
  return i;
}

inline unsigned rotate(unsigned i, unsigned w)
{
  return i/10 + (i%10) * p[w-1];
}

int main()
{
  p[0] = 1;
  for (int i = 0; i < 10; ++i) {
    p[i+1] = p[i] * 10;
  }

  for (unsigned i = 1; i <= 2000000; ++i) {
    unsigned n = i;
    unsigned w = width(n);

    std::set<unsigned>& s = t[i];
    for (int c = 0; c < w; ++c) {
      if (w == width(n)) {
	s.insert(n);
      }
      n = rotate(n, w);
    }
    s.erase(i);
  }

  unsigned nCase;
  std::cin >> nCase;
  for (unsigned iCase = 1; iCase <= nCase; ++iCase) {
    unsigned A, B;
    std::cin >> A >> B;

    unsigned long long c = 0;

    for (unsigned i = A; i <= B; ++i) {
      std::set<unsigned>& s = t[i];
      std::set<unsigned>::iterator it = s.begin(), eit = s.end();
      for (; it != eit; ++it) {
	if (*it >= A && *it <= B) {
	  ++c;
	}
      }
    }

    std::cout << "Case #" << iCase << ": " << (c / 2) << std::endl;
  }

  return 0;
}
