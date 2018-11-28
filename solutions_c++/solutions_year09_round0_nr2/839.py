#include <cassert>
#include <iostream>
#include <vector>
//#include <ctypes>

using namespace std;
typedef vector<int> vi_t;
typedef vector<char> vc_t;

void update_basis(const vector<vi_t>& mmap,
                  int h, int w, vector<vc_t>& basis)
{
  int h1 = h, w1 = w;
  if (basis[h][w] != '\0') 
  {
    return;
  }
  int m = min(mmap[h-1][w], mmap[h][w+1]);
  m = min(m, mmap[h][w-1]);
  m = min(m, mmap[h+1][w]);
  if (mmap[h-1][w] == m)
  {
    --h1; 
  }
  else
    if (mmap[h][w-1] == m)
    {
      --w1;
    }
    else if (mmap[h][w+1] == m)
    {
      ++w1;
    }
    else
    {
      assert(mmap[h+1][w] == m);
      ++h1;
    }
    assert(h1 >= 1 && w1 >= 1);
    if (basis[h1][w1] == '\0')
    {
      update_basis(mmap, h1, w1, basis);
    }
    basis[h][w] = basis[h1][w1];
}

void subst(vector<vc_t>& b, char s, char d)
{
  for (size_t h = 1; h < b.size() -1; ++h)
    for (size_t w = 1; w < b[h].size() - 1; ++w)
    {
      if (b[h][w] == s) b[h][w] = d;
    }
}
int main()
{
  int T; cin >> T;
  cin.ignore();
  for (int n = 1; n <= T; ++n)
  {
    int H, W;
    cin  >> H >> W;
    vector<vi_t> mmap(H + 2, vi_t(W + 2, 100000));
    for (int h = 1; h <= H; ++h)
    {
      for (int w = 1; w <= W; ++w)
        cin >> mmap[h][w];
    }
    vector<vector<char> > basis(H+2, vector<char>(W+2, '\0'));
    char BC = 'A';
    for (int h = 1; h <= H; ++h)
    {
      for (int w = 1; w <= W; ++w)
      {
        int m = min(mmap[h-1][w], mmap[h][w+1]);
        m = min(m, mmap[h][w-1]);
        m = min(m, mmap[h+1][w]);
        if (m >= mmap[h][w]) 
        {
          basis[h][w] = BC++;
        }
      }
    }
    for (int h = 1; h <= H; ++h)
    {
      for (int w = 1; w <= W; ++w)
      {
        if (basis[h][w] == '\0')
        {
          update_basis(mmap, h, w, basis);
        }
      }
    }
    char bc = 'a';
    for (int h = 1; h <= H; ++h)
    {
      for (int w = 1; w <= W; ++w)
      {
        if (isupper(basis[h][w]))
        {
          subst(basis, basis[h][w], bc);
          ++bc;
        }
      }
    }
    cout << "Case #" << n << ":\n";
    for (int h = 1; h <= H; ++h)
    {
      for (int w = 1; w <= W; ++w)
      {
        cout << basis[h][w];
        if (w != W) cout << ' ';
      }
      cout << endl;
    }
  }
  return 0;
}