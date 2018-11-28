#include <iostream>
#include <vector>
#include <utility>

typedef std::vector< std::pair<int, int> > Commands;

int abs(int v) {
    return v > 0 ? v : -v;
}

int readCommands(Commands& b, Commands& o) {
    int commandCount;
    std::cin >> commandCount;
    for (int i = 0; i < commandCount; ++i) {
        char color;
        std::cin >> color;
        Commands& current = (color == 'B') ? b : o;
        current.resize(current.size() + 1);
        std::cin >> current.back().first;
        current.back().second = i; 
    }
}

void move(Commands::const_iterator& n,
          const Commands::const_iterator& o,
          int& npos,
          int& opos,
          int& time,
          bool onlyOne)
{
    int toPress = abs(npos - n->first) + 1;
    npos = n->first;
    time += toPress;
    ++n;
    if (!onlyOne) {
        int distToButton = abs(opos - o->first);
        if (distToButton <= toPress) {
            opos = o->first;
        } else {
            opos += (opos > o->first) ? -toPress : toPress;
        } 
    }
}

int solve(const Commands& b, const Commands& o) {
    int bpos = 1;
    int opos = 1;
    int time = 0;
    Commands::const_iterator bc = b.begin();
    Commands::const_iterator oc = o.begin();
    while (bc != b.end() || oc != o.end()) {
        if ((oc == o.end()) || (bc != b.end() && bc->second < oc->second)) {
            move(bc, oc, bpos, opos, time, oc == o.end());
        } else {
            move(oc, bc, opos, bpos, time, bc == b.end());
        }
    }
    return time;
}

int main() {
    int testCount;
    std::cin >> testCount;
    for (int t = 1; t <= testCount; ++t) {
        Commands b, o;
        readCommands(b, o);
        std::cout << "Case #" << t << ": " << solve(b, o) << std::endl;
    } 
    return 0;
}

