#include <iostream>
#include <set>

using namespace std;

const int INF = 200000000;

struct Node
{
  int type;
  int time;
  int end;

  Node(int type, int time, int end):
    type(type), time(time), end(end)
  {
  }
};

struct ltnode
{
  bool operator()(const Node &a, const Node &b) const
  {
    if (a.time != b.time)
    {
      return a.time < b.time;
    }
    else
    {
      return a.type < b.type;
    }
  }
};

int
timecvt(string s)
{
  int a = (s[0] - '0') * 10 + (s[1] - '0');
  int b = (s[3] - '0') * 10 + (s[4] - '0');
  return a * 60 + b;
}

int n, na, nb;
int T;
multiset<Node, ltnode> iset;

int cnt[2];
int result[2];

int main()
{
  cin >> n;
  for (int e = 1; e <= n; ++e)
  {
    cout << "Case #" << e << ": ";
    cin >> T;
    cin >> na >> nb;
    for (int i = 0; i < na; ++i)
    {
      string t1, t2;
      cin >> t1 >> t2;
      Node *p = new Node(2, timecvt(t1), timecvt(t2) + T);
      iset.insert(*p);
    }
    for (int i = 0; i < nb; ++i)
    {
      string t1, t2;
      cin >> t1 >> t2;
      Node *p = new Node(3, timecvt(t1), timecvt(t2) + T);
      iset.insert(*p);
    }
    /*
    for (multiset<Node, ltnode>::iterator p = iset.begin(); p != iset.end(); ++p)
    {
      cout << p->type << " " << p-> time << " " << p->end << endl;
    }
    cout << endl;
    */
    Node *p;
    result[0] = result[1] = 0;
    cnt[0] = cnt[1] = 0;
    while (iset.size() > 0)
    {
      multiset<Node, ltnode>::iterator now;
      now = iset.begin();
      switch (now->type)
      {
	case 0:
	case 1:
	  ++cnt[now->type];
	  break;
	case 2:
	case 3:
	  if (cnt[now->type % 2] == 0)
	  {
	    ++result[now->type % 2];
	    ++cnt[now->type % 2];
	  }
	  p = new Node((now->type + 1) % 2, now->end, INF);
	  iset.insert(*p);
	  --cnt[now->type % 2];
	  break;
      }
      iset.erase(now);
    }
    cout << result[0] << ' ' << result[1] << endl;
  }
  return 0;
}

