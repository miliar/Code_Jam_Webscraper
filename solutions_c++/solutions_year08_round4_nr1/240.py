#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <iostream>

const size_t IMPOSSIBLE = 100000;

class Node {
public:
  virtual size_t make(bool val) = 0;
  virtual bool precalc() = 0;
};

class Interior: public Node {
public:
  Interior(bool ia, bool c): is_and(ia), changeable(c) {}
  size_t make(bool v)
  {
    if (v == val) {
      //std::cerr << "Already done" << std::endl;
      return 0;
    }
    if (v == is_and) {
      //std::cerr << "Hard case" << std::endl;
      // Both inputs must equal intended output, or we must change the
      // type of this node
      size_t make_left = left->make(v);
      size_t make_right = right->make(v);
      size_t best = make_left + make_right;
      if (changeable) {
        size_t other = 1 + std::min(make_left, make_right);
        if (other < best)
          best = other;
      }
      return best;
    } else {
      //std::cerr << "Easy case" << std::endl;
      // Just one must equal intended output
      return std::min(left->make(v), right->make(v));
    }
  }
  bool precalc() {
    bool l = left->precalc();
    bool r = right->precalc();
    val = is_and ? (l && r) : (l || r);
    //std::cerr << "precalc: " << val << std::endl;
    return val;
  }
  Node *left, *right;
private:
  bool is_and, changeable;
  bool val;
};

class Leaf: public Node {
public:
  Leaf(bool v): val(v) {}
  size_t make(bool v) {
    if (v == val)
      return 0;
    else
      return IMPOSSIBLE;
  }
  bool precalc() { return val; }
private:
  bool val;
};

void calc()
{
  size_t m;
  bool v;
  std::cin >> m >> v;
  Node *root = 0;
  std::vector<Node *> nodes;
  std::list<Interior *> queue;
  bool odd = false;
  for (size_t i = 0; i < (m - 1) / 2; i++) {
    bool g, c;
    std::cin >> g >> c;
    Interior *node = new Interior(g, c);
    nodes.push_back(node);
    if (!queue.empty()) {
      if (odd) {
        queue.front()->right = nodes.back();
        queue.pop_front();
      } else {
        queue.front()->left = nodes.back();
      }
      odd = !odd;
    } else {
      root = nodes.back();
    }
    queue.push_back(node);
  }
  for (size_t i = 0; i < (m + 1) / 2; i++) {
    bool i;
    std::cin >> i;
    nodes.push_back(new Leaf(i));
    if (odd) {
      queue.front()->right = nodes.back();
      queue.pop_front();
    } else {
      queue.front()->left = nodes.back();
    }
    odd = !odd;
  }
  root->precalc();
  size_t res = root->make(v);
  if (res >= IMPOSSIBLE)
    std::cout << "IMPOSSIBLE";
  else
    std::cout << res;
}

int main()
{
  size_t count;
  std::cin >> count;
  for (size_t i = 0; i < count; i++) {
    std::cout << "Case #" << (i + 1) << ": ";
    calc();
    std::cout << std::endl;
  }
}
