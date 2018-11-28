
const int N_ROBOTS = 2;

#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

class Order
{
public:
  Order(int pos, int prio): _pos(pos), _prio(prio) { }
  Order(const Order& order): _pos(order.getPos()), _prio(order.getPrio()) { }
  int getPos() const { return _pos; }
  int getPrio() const { return _prio; }
protected:
  int _pos;
  int _prio;
};

class Robot
{
public:
  Robot(char index): _index(index), _pos(1) { }
  void addOrder(int pos, int prio) { _orders.push(Order(pos, prio)); }
  bool execute(int prio)
  {
    if (_orders.empty())
    {
//      cout << "Robot " << _index << " is dormant.\n";
      return false;
    }
    Order& next = _orders.front();
    int pos = next.getPos();
    if (pos == _pos)
    {
      if (next.getPrio() > prio)
      {
//        cout << "Robot " << _index << " waits at a position " << _pos << ".\n";
        return false;
      }
//      cout << "Robot " << _index << " pushes the button " << _pos << ".\n";
      _orders.pop();
      return true;
    }
    if (pos > _pos) ++_pos; else --_pos;
//    cout << "Robot " << _index << " moves to the position " << _pos << ".\n";
    return false;
  }
protected:
  char _index;
  int _pos;
  queue<Order> _orders;
};

int main(int argc, char *argv[])
{
  if (argc < 2)
    return 1;
  ifstream in(argv[1]);

  int t;
  in >> t;
  for (int i = 0; i < t; ++i)
  {
    int n, s = 0, c = 0;

    Robot *robots[N_ROBOTS] = { new Robot('O'), new Robot('B') };

    in >> n;
    for (int j = 0; j < n; ++j)
    {
      char r;
      int p;
      in >> r >> p;
      robots['B' == r]->addOrder(p, j);
    }

    while (c < n)
    {
      bool exec = false;
      for (int k = 0; k < N_ROBOTS; ++k)
      {
        if (robots[k]->execute(c))
        {
          exec = true;
//          cout << "Order " << 1 + c << " has been processed.\n";
        }
      }
      if (exec)
        ++c;
      ++s;
//      cout << s << " seconds have passed.\n";
    }

    for (int k = 0; k < N_ROBOTS; ++k)
      delete robots[k];

    cout << "Case #" << 1 + i << ": " << s << "\n";
  }
  return 0;
}

