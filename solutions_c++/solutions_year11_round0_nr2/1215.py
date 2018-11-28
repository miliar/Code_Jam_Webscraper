#include <iostream>
#include <map>
#include <utility>
#include <string>
#include <cassert>
#include <vector>

typedef std::pair<char, char> Pair;
typedef std::map<char, char> CharMap;
typedef std::map<Pair, char> PairMap;
typedef std::vector<char> List;

CharMap opposed;
PairMap combine;

List compute(std::string op)
{
  List L;
  for(int i=0;i<op.size();i++) {
    L.push_back(op[i]);
    if(L.size() >= 2) {
      char e1 = L[L.size() - 2];
      char e2 = L[L.size() - 1];
      char r = combine[std::make_pair(e1, e2)];
      if(r > 0) {
	L.pop_back();
	L.pop_back();
	L.push_back(r);
      }
    }

    char e = L[L.size() - 1];
    for(int j=0;j<L.size()-1;j++) {
      if(opposed[e] == L[j]) {
	L.clear();
	break;
      }
    }
  }
  return L;
}

int main()
{
  int T;
  std::cin >> T;
  for(int i=0;i<T;i++) {
    opposed.clear();
    combine.clear();

    int C;
    std::cin >> C;
    for(int j=0;j<C;j++) {
      std::string op;
      std::cin >> op;
      char b1 = op[0];
      char b2 = op[1];
      char t = op[2];
      combine[std::make_pair(b1, b2)] = t;
      combine[std::make_pair(b2, b1)] = t;
    }

    int D;
    std::cin >> D;
    for(int j=0;j<D;j++) {
      std::string op;
      std::cin >> op;
      char b1 = op[0];
      char b2 = op[1];
      opposed[b1] = b2;
      opposed[b2] = b1;
    }

    int N;
    std::cin >> N;

    std::string op;
    std::cin >> op;
    assert(op.size() == N);
    
    List l = compute(op);
    std::cout << "Case #" << i+1 << ": [";
    for(int j=0;j<l.size();j++)
      std::cout << (j > 0 ? ", " : "") << l[j];
    std::cout << "]\n";
  }
  return 0;
}

