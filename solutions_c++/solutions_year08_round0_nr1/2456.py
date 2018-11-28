#include <iostream>
#include <map>
#include <string>
#include <limits>
#include <vector>

using namespace std;

typedef vector<int> vi;

class prob {
    int S;
    int Q;
    typedef map<string, int> nmap_t;

  public:
    int solve() {
        const int BUFSIZE = 100;
        char buf[BUFSIZE];
        buf[BUFSIZE-1] = 0;
        cin >> S;
        cin.ignore(numeric_limits<int>::max(), '\n');
        for (int s = 0; s < S; ++s) {
            cin.getline(buf, BUFSIZE);
        }

        cin >> Q;
        cin.ignore(numeric_limits<int>::max(), '\n');
        nmap_t nmap;
        int cnt = 0;
        for (int q = 0; q < Q; ++q) {
            cin.getline(buf, BUFSIZE);
            ++nmap[buf];
            if (nmap.size() == S) {
                ++cnt;
                nmap.clear();
                ++nmap[buf];
            }
        }

        return cnt;
    }
};

int main() {
    int n;
    cin >> n;
    for (int i = 1; i<=n; ++i) {
        prob p;
        cout << "Case #" << i << ": " << p.solve() << endl;
    }
    return 0;
}
