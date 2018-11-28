#include <iostream>
#include <fstream>
#include <vector>
#include <utility>

using namespace std;

pair<int,int> take_candy(vector<int> &candies, int i, int pile1_x, int pile1_s, int pile2_x, int pile2_s)
{
  pair<int,int> piles, p;
  if (i != -1)
  {
    int c = candies[i];
    pile1_x ^= c;
    pile1_s -= c;
    pile2_x ^= c;
    pile2_s += c;
    if (pile1_x == pile2_x)
    {
      piles.first = pile1_s;
      piles.second = pile2_s;
//      cout << i << ":" << pile1_s << ":" << pile2_s << " ";
      return piles;
    }
  }
  piles.first = piles.second = -1;
  int max_diff = -1, diff;
  for (int j = i + 1; j < (int)candies.size(); j++)
  {
    p = take_candy(candies, j, pile1_x, pile1_s, pile2_x, pile2_s);
    diff = p.first - p.second;
    if (diff < 0) diff = -diff;
    if (diff > max_diff)
    {
      max_diff = diff;
      piles = p;
    }
  }
  return piles;
}

int main(int argc, char *argv[])
{
  vector<int> candies;
  int T, N, C, pile1_x, pile1_s;//, pile2_x, pile2_s;
  pair<int,int> piles;

  ifstream in;
  ofstream out;

  if (argc == 3)
  {
    in.open(argv[1]);
    if (!in.is_open())
    {
      cerr << "Error opening " << argv[1] << endl;
      return 0;
    }
    out.open(argv[2]);
    if (!out.is_open())
    {
      in.close();
      cerr << "Error opening " << argv[2] << endl;
      return 0;
    }
  }
  else
  {
    in.open("in.txt");
    if (!in.is_open())
    {
      cerr << "Error opening in.txt" << endl;
      return 0;
    }
    out.open("out.txt");
    if (!out.is_open())
    {
      in.close();
      cerr << "Error opening out.txt" << endl;
      return 0;
    }
  }

  in >> T;
  for (int i = 0; i < T; i++)
  {
    out << "Case #" << i + 1 << ": ";
//    cout << "Case #" << i + 1 << ": ";
    candies.clear();
    pile1_x = pile1_s = 0;//pile2_x = pile2_s = 0;
    in >> N;
    for (int j = 0; j < N; j++)
    {
      in >> C;
      candies.push_back(C);
      pile1_x ^= C;
      pile1_s += C;
    }
    piles = take_candy(candies, -1, pile1_x, pile1_s, 0, 0);
    if (piles.first == -1)
      out << "NO" << endl;
    else
      out << (piles.first > piles.second ? piles.first : piles.second) << endl;
//    cout << endl;
  }

  return 0;
}

