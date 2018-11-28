#include <iostream>
#include <map>
#include <set>
#include <string>

typedef std::map<std::pair<char, char>, char> Combine;
typedef Combine::const_iterator CIt;
typedef std::map<char, std::set<char> > Opposed;
typedef Opposed::const_iterator OIt;

void readInput(Combine& c,
               Opposed& o,
               std::string& s)
{
    int cCount;
    std::cin >> cCount;
    for (int i = 0; i < cCount; ++i) {
        std::string buf;
        std::cin >> buf;
        c[std::make_pair(buf[0], buf[1])] = buf[2];
        c[std::make_pair(buf[1], buf[0])] = buf[2];
    }
    int oCount;
    std::cin >> oCount;
    for (int i = 0; i < oCount; ++i) {
        std::string buf;
        std::cin >> buf;
        o[buf[0]].insert(buf[1]);
        o[buf[1]].insert(buf[0]);
    }
    std::cin >> oCount >> s;
}

void solve(const Combine& c,
           const Opposed& o,
           const std::string& s,
           std::string& l)
{
    std::set<char> opp;
    char prev = s[0];
    for (int i = 1; i < s.length(); ++i) {
        char cur = s[i];
        CIt cit = c.find(std::make_pair(cur, prev));
        if (cit != c.end()) {
            prev = cit->second;
            continue;
        }
        if (prev != '\0') {
            l.push_back(prev);
            OIt oit = o.find(prev);
            if (oit != o.end()) {
                opp.insert(oit->second.begin(), oit->second.end());
            }
        }
        if (opp.count(cur)) {
           opp.clear();
           l.clear();
           prev = '\0';
        } else {
            prev = cur;
        }
    }
    if (prev != '\0') {
        l.push_back(prev);
    }
}

int main() {
    int testCount;
    std::cin >> testCount;
    for (int t = 1; t <= testCount; ++t) {
        Combine c;
        Opposed o;
        std::string s, l;
        readInput(c, o, s);
        solve(c, o, s, l);
        std::cout << "Case #" << t << ": [";
        if (l.length()) {
            for (int i = 0; i < l.length() - 1; ++i) {
                std::cout << l[i] << ", ";
            }
            std::cout << l[l.length() - 1];
        }
        std::cout << "]" << std::endl;
    }
    return 0;
}
