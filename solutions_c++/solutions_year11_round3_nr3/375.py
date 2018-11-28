#include <vector>
#include <cmath>
#include <limits>
#include <iostream>
#include <algorithm>
#include <stdint.h>

using namespace std;


typedef uint64_t Int;

const Int infty = Int(-1);
const Int Big = 10000000000000000UL;

Int safe_mult(Int a, Int b)
{
  if ( a == 0 or b == 0 )
    return 0;
  if ( a > Big/b or b > Big/a )
    return infty;
  return a*b;
}


Int gcd(Int a, Int b)
{
  while ( b > 0 )
  {
    Int r = a % b;
    a = b; b = r;
  }
  return a;
}


Int lcm(Int a, Int b)
{
  Int g = gcd(a, b);
  return safe_mult(a/g, b);
}


struct Note
{
  Note(Int n)
    : value(n)
  {}
  Int value;
  Int gcd;
  Int lcm;
};


inline bool operator<(Note const &n1, Note const &n2)
{
  return n1.value < n2.value;
}

vector<Note> read_data(Int &L, Int &H)
{
  int N;
  cin >> N >> L >> H;
  vector<Note> res;
  for ( int i = 0; i < N; ++i )
  {
    Int v;
    cin >> v;
    res.push_back(Note(v));
  }
  sort(res.begin(), res.end());
  res[N - 1].gcd = res[N - 1].value;
  for ( int i = N - 2; i >= 0; --i )
    res[i].gcd = gcd(res[i].value, res[i + 1].gcd);
  res[0].lcm = res[0].value;
  for ( int i = 1; i < N; ++i )
    res[i].lcm = lcm(res[i].value, res[i - 1].lcm);
  return res;
}


Int first_try(vector<Note> const &notes, Int L, Int H)
{
  Int g = notes[0].gcd;
  Int x = 1;
  Int best = infty;
  while ( safe_mult(x, x) <= g )
  {
    if ( g % x == 0 )
    {
      if ( x >= L and x <= H )
        best = min(best, x);
      Int y = g/x;
      if ( y >= L and y <= H )
        best = min(best, y);
    }
    ++x;
  }
  return best;
}


Int second_try(vector<Note> const &notes, Int L, Int H, int idx)
{
  Int l = notes[idx].lcm;
  Int g = notes[idx + 1].gcd;
  if ( l == infty )
    return infty;
  if ( g % l != 0 )
    return infty;
  Int p = g/l;
  Int x = 1;
  Int best = infty;
  while ( safe_mult(x, x) <= p )
  {
    if ( p % x == 0 )
    {
      Int n = x*l;
      if ( n >= L and n <= H )
        best = min(best, n);
      Int y = p/x;
      n = y*l;
      if ( n >= L and n <= H )
        best = min(best, n);
    }
    ++x;
  }
  return best;
}


Int last_try(vector<Note> const &notes, Int L, Int H)
{
  int N = notes.size();
  Int l = notes[N - 1].lcm;
  Int m = (L + l - 1)/l;
  m *= l;
  if ( m >= L and m <= H )
    return m;
  return infty;
}


Int try_all(vector<Note> const &notes, Int L, Int H)
{
  int N = notes.size();
  Int best = first_try(notes, L, H);
  for ( int i = 0; i < N - 1; ++i )
    best = min(best, second_try(notes, L, H, i));
  best = min(best, last_try(notes, L, H));
  return best;
}


int main()
{
  int T;
  cin >> T;
  for ( int t = 1; t <= T; ++t )
  {
    Int L, H;
    vector<Note> r = read_data(L, H);
    cout << "Case #" << t << ": ";
    Int best = try_all(r, L, H);
    if ( best != infty )
      cout << best << '\n';
    else
      cout << "NO\n";
  }
  return 0;
}
    
