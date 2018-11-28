#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <fstream>
#include <vector>

#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define FR(i,a) for(int i = 0; i < (a); ++i)

#define FILENAME "A-large"
static const char* c_pszInFileName = FILENAME ".in";
static const char* c_pszOutFileName = FILENAME ".out";

using namespace std;

template<class T>
void GetLine(ifstream& ifs, T& t) {
    string line;
    getline(ifs, line);
    stringstream(line) >> t;
}

typedef map<long long, short>::iterator mit;
typedef set<long long>::iterator sit;

ostream& operator<< (ostream& os, pair<int, int> const& p) {
    return os << p.first << ", " << p.second;
}


struct Coord {
    int button;
    int time;
};

int calc(vector<pair<string,int> > const& instructions) {
    int time = 0;
    map<string, Coord> mem = map<string, Coord >();
    mem["O"] = {1, time};
    mem["B"] = {1, time};
    
    for_each(instructions.begin(), instructions.end(), [&mem, &time](pair<string,int> const& p) {
            int button = p.second;
            Coord &c = mem[p.first];
            int dist = max(0, abs(c.button - button) - (time - c.time));
            cout << "c.time: " << c.time << endl;
            cout << "dist: " << dist << endl;

            c.time = (time += (dist + 1));
            c.button = button;

            cout << "time: " << time << endl;
        });
    return time;
}

int main() {
    ifstream ifs(c_pszInFileName);
    ofstream ofs(c_pszOutFileName);
    FILE* pFile = fopen(c_pszOutFileName, "w");

    int T;
    GetLine(ifs, T);

    FR(t, T) {
        int N;
        ifs >> N;

        vector<pair<string,int> > instructions = vector<pair<string,int> >();

        FR(n, N) {
            string robot;
            int button;
            ifs >> robot;
            ifs >> button;
            
            instructions.push_back(make_pair(robot, button));
        }
        cout << endl;
        int ans = calc(instructions);
        ofs << "Case #" << (t+1) << ": " << ans << "\n";
    }
    cout.flush();
    fclose(pFile);
    return 0;
}
