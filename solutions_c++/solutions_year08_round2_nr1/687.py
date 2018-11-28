#include <string>
#include <fstream>
#include <iostream>
#include <list>
#include <algorithm>


using namespace std;

static   ifstream input ("input_small");

char peek()
{
  return  input.peek();
}

int pos()
{
  return input.tellg();
}

typedef unsigned long int ulint;

struct Tree
{
  ulint x;
  ulint y;

  Tree(ulint x_, ulint y_)
    : x(x_)
    , y(y_)
  {
    //cout << t.back().x << " " << t.back().y << endl;
  }
};



ostream& operator<<(ostream& ostr, const Tree& t)
{
  return ostr << "{" << t.x << ", " << t.y << "}";
}


int main(int, char*)
{
  ulint nb_cases;
  ulint n;
  ulint A, B, C, D, x0, y0, M;

  list<Tree> t;

  input >> nb_cases;
  for (ulint c = 0; c < nb_cases; ++c)
  {
    input >> n;
    input >> A;
    input >> B;
    input >> C;
    input >> D;
    input >> x0;
    input >> y0;
    input >> M;

    t.clear();

    t.push_back(Tree(x0, y0));

    for (ulint i = 1; i < n; ++i)
      t.push_back(Tree((A * t.back().x + B) % M, (C * t.back().y + D) % M));

    for (ulint i = 0; i < n; ++i)
    {
      list<Tree>::iterator it = t.begin();
      advance(it, i);
      //cout << *it << " --> " << it->x % 3 << endl;
    }
    int res = 0;
    for (ulint i = 0; i < t.size(); ++i)
    for (ulint j = i+1; j < t.size(); ++j)
    for (ulint k = j+1; k < t.size(); ++k)
    {
      list<Tree>::iterator it0 = t.begin(); advance(it0, i);
      list<Tree>::iterator it1 = t.begin(); advance(it1, j);
      list<Tree>::iterator it2 = t.begin(); advance(it2, k);
      if ((it0->x + it1->x + it2->x) % 3 == 0 &&
	  (it0->y + it1->y + it2->y) % 3 == 0)
      {
	++res;
	//cout << *it0 <<  "  " << *it1 <<  "  "  << *it2 << endl;
      }

    }
    cout << "Case #" << (c+1) << ": " << res << endl;
  }


  input.close();

  return 0;
}

////////// RESOLUTION


int solve_case(string* servers, int nb_servers, string* queries, int nb_queries)
{
  // OPTIMIZATIONS : transforms all names in integers
  int* qs = new int[nb_queries];

  for (int q = 0; q < nb_queries; ++q)
  {
    int s = -1;
    while (++s < nb_servers)
      if (queries[q] == servers[s])
      {
	qs[q] = s;
	break;
      }

    if (s == nb_servers)
      qs[q] = nb_servers; // won't implode any server :) So qe associate this query to an arbitrary value
  }

  int res = 0;
  int count = 0;
  int* counts = new int[nb_servers + 1];

  for (int s = 0; s < nb_servers; ++s)
    counts[s] = 0;

  for (int q = 0; q < nb_queries; ++q)
  {
    if (counts[qs[q]] == 0 && qs[q] < nb_servers)
      ++count;
    ++counts[qs[q]];

    if (count == nb_servers)
    {
      res++;
      for (int s = 0; s < nb_servers; ++s)
	counts[s] = 0;
      count = 0;
      --q;
    }
  }

  delete[] qs;
  delete[] counts;

  return res;
}
