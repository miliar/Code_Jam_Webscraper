#include <cassert>
#include <fstream>
#include <iostream>
#include <string>
#include <iomanip>

std::string p = "welcome to code jam";


template <typename T>
struct image2d
{
  image2d(unsigned nrows_, unsigned ncols_)
    : ncols(ncols_),
      nrows(nrows_),
      border(0)
  {
    buffer = new T[ncols*nrows]();
  }

  bool has(int i, int j) const
  {
    return (i >= 0) && (j >= 0) && (i < nrows) && (j < ncols);
  }

  T& operator()(unsigned i, unsigned j)
  {
    assert(has(i,j));
    return buffer[i * ncols + j];
  }

  const T& operator()(unsigned i, unsigned j) const
  {
    assert(has(i,j));
    return buffer[i * ncols + j];
  }

private:
  unsigned ncols, nrows;
  T* buffer;
  T border;
};

int main(int argc, char* argv[])
{
  std::ifstream file_in(argv[1]);

  unsigned n_cases;

  file_in >> n_cases;
  file_in.get();
  for (unsigned c = 0; c < n_cases; c++)
  {
    std::string s;

    std::getline(file_in, s);

    image2d<int> ima(p.size(), s.size());

    ima(p.size() - 1, s.size() - 1) = p[p.size() - 1] == s[s.size() - 1] ? 1 : 0;
    for (int i = s.size() - 2; i >= 0 ; i--)
    {
      if (p[p.size() - 1] == s[i])
	ima(p.size() - 1, i) = 1;
      ima(p.size() - 1, i) += ima(p.size() - 1, i + 1);
    }

    for (int i = p.size() - 2; i >= 0 ; i--)
    {
      for (int j = s.size() - 1; j >= 0; j--)
      {
	if (ima.has(i, j+1))
	  ima(i, j) = ima(i, j+1);
	else
	  ima(i, j) = 0;

	if (p[i] == s[j])
	  ima(i, j) += ima(i+1, j);
	ima(i, j) = ima(i, j) % 10000;
      }
    }

    std::cout << "Case #" << (c + 1) << ": "
	      << std::setw(4) << std::setfill('0') << ima(0, 0) << std::endl;
  }
}
