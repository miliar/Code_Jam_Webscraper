#include <fstream>
#include <limits>
#include <iostream>
#include <cassert>
#include <vector>
#include <map>
#include <string>

struct point
{
  point() { }
  point(int v) { coord[0] = v; coord[1] = v; }
  point(int r, int c) { coord[0] = r; coord[1] = c; }
  point& operator=(const point& r)
  {
    coord[0] = r[0];
    coord[1] = r[1];
    return *this;
  }
  int& operator[](unsigned i) { return coord[i]; }
  const int& operator[](unsigned i) const { return coord[i]; }
  int coord[2];
};

template <typename T>
struct image2d
{
  image2d(unsigned nrows_, unsigned ncols_)
    : ncols(ncols_),
      nrows(nrows_)
  {
    buffer = new T[ncols*nrows]();
  }

  bool has(int i, int j) const
  {
    return (i >= 0) && (j >= 0) && (i < nrows) && (j < ncols);
  }

  bool has(point p) const
  {
    return has(p[0], p[1]);
  }

  T& operator()(unsigned i, unsigned j)
  {
    return buffer[i * ncols + j];
  }

  T& operator()(point p)
  {
    return buffer[p[0] * ncols + p[1]];
  }

private:
  unsigned ncols, nrows;
  T* buffer;
};

char label = 'a';

void recursion(image2d<int>& ima, image2d<char>& labels, unsigned r, unsigned c)
{
  if (labels(r,c))
    return;

  std::vector<point> dps(4);
  dps[0] = point(-1, 0);
  dps[1] = point(0, -1);
  dps[2] = point(0, 1);
  dps[3] = point(1, 0);

  int min = 0;
  point p_min;
  for (unsigned i = 0; i < 4; i++)
  {
    point p;
    p[0] = r + dps[i][0];
    p[1] = c + dps[i][1];
    if (ima.has(p))
    {
      if ((ima(p) - ima(r,c)) < min)
      {
        min = ima(p) - ima(r,c);
        p_min = p;
	assert(min < 0);
      }
    }
  }

  if (min < 0)
  {
    recursion(ima, labels, p_min[0], p_min[1]);
    assert(!labels(r, c));
    labels(r, c) = labels(p_min[0], p_min[1]);
  }
  else
  {
    assert(!labels(r, c));
    labels(r, c) = label++;
  }
}

int main(int argc, char* argv[])
{
  std::ifstream file_in(argv[1]);

  unsigned n_cases;

  file_in >> n_cases;

  for (unsigned i = 0; i < n_cases; i++)
  {
    unsigned nrows, ncols;
    file_in >> nrows;
    file_in >> ncols;
    image2d<int> ima(nrows, ncols);
    for (unsigned r = 0; r < nrows; r++)
      for (unsigned c = 0; c < ncols; c++)
        file_in >> ima(r, c);

    image2d<char> labels(nrows, ncols);
    label = 'a';
    for (unsigned r = 0; r < nrows; r++)
      for (unsigned c = 0; c < ncols; c++)
        labels(r, c) = 0;

    for (unsigned r = 0; r < nrows; r++)
      for (unsigned c = 0; c < ncols; c++)
        recursion(ima, labels, r, c);

    std::cout << "Case #" << (i+1) << ":";
    for (unsigned r = 0; r < nrows; r++)
    {
      std::cout << std::endl;
      for (unsigned c = 0; c < ncols; c++)
        std::cout << labels(r,c) << " ";
    }
    std::cout << std::endl;

  }
}
