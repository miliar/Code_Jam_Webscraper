#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>

class node {
public:
    int d;
    int v;

    node(int d, int v) {
        this->d = d;
        this->v = v;
    }

    friend bool operator< (const node & self, const node & other) {
        return self.d < other.d;
    }

    friend bool operator== (const node & self, const node & other) {
        return self.d == other.d && self.v == other.v;
    }
};

class jungle {
public:
    int finald;
    int nvines;
    std::vector<int> vined;
    std::vector<int> vinel;

    jungle(int nvines) { this->nvines = nvines; }

    bool solve() {
        std::priority_queue<node> todo;
        std::set<int> seen[this->nvines];

        todo.push(node(0, 0));
        for (;;) {
            if (todo.empty())
                return false;
            node next = todo.top();
            todo.pop();
            std::cerr << "Looking " << next.v << " " << next.d << "\n";
            int span = (this->vined[next.v] - next.d) * 2;
            int reachd = next.d + span;
            std::cerr << "Reaches " << reachd << " (span " << span << ")\n";
            if (reachd >= this->finald)
                return true;
            for (int v = next.v+1; v < this->nvines && this->vined[v] <= reachd; v++) {
                int dist = this->vined[v] - this->vined[next.v];
                if (this->vinel[v] < dist)
                    dist = this->vinel[v];
                node move(this->vined[v] - dist, v);
                std::cerr << "Considering " << move.v << " " << move.d << "\n";
                if (!seen[move.v].count(move.d)) {
                    todo.push(move);
                    seen[move.v].insert(move.d);
                } else
                    std::cerr << "Seen!\n";
            }
        }
    }
};

int main(void)
{
    int ncases;

    std::cin >> ncases;
    std::cin.ignore();
    for (int casenr = 1; casenr <= ncases; casenr++) {
      int nvines, finald;

      std::cin >> nvines;
      std::cin.ignore();
      jungle j(nvines);
      for (int i = 0; i < nvines; i++) {
          int vined, vinel;
          std::cin >> vined >> vinel;
          j.vined.push_back(vined);
          j.vinel.push_back(vinel);
      }

      std::cin >> finald;
      j.finald = finald;

      if (j.solve()) {
          std::cerr << "Case #" << casenr << ": YES\n";
          std::cout << "Case #" << casenr << ": YES\n";
      } else {
          std::cerr << "Case #" << casenr << ": NO\n";
          std::cout << "Case #" << casenr << ": NO\n";
      }
    }
}
