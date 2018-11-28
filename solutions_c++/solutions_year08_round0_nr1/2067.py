#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <map>
#include <stack>
#include <climits>

using namespace std;

struct Case {
    int             *queries;
    int             num_engines;
    int             num_queries;
};

class Solver {
public:
    static float    solve(Case &c);
};

float Solver::solve(Case &c) {
    // We use dynamic programming (or sort of) to solve this...
    int min_switches = 0;
    bool active[c.num_engines];
    int num_active = c.num_engines;
    for (int i = 0; i < c.num_engines; i++) {
        active[i] = true;
    }
    // Calculate solution
    for (int i = c.num_queries - 1; i >= 0; i--) {
        if (active[c.queries[i]]) {
            active[c.queries[i]] = false;
            num_active--;
        }
        if (num_active == 0) {
            min_switches++;
            for (int j = 0; j < c.num_engines; j++) {
                if (c.queries[i] != j) {
                    active[j] = true;
                }
            }
            num_active = c.num_engines - 1;
        }
    }
    // Return solution
    return min_switches;
}

int main(int argc, char** argv) {
    ifstream input;
    string engine_name;
    map<string, int> engines_map;
    int num_engines, num_queries;
    int N;

    // Open input file
    input.open(argv[1]);

    // Get number of cases and start running them
    input >> N;
    for (int i = 0; i < N; i++) {
        Case cur_case;
        // Read number of engines
        input >> num_engines;
        input.get();
        // Read names of search engines
        for (int j = 0; j < num_engines; j++) {
            getline(input, engine_name);
            engines_map[engine_name] = j;
        }
        // Read sequence of queries
        input >> num_queries;
        input.get();
        cur_case.queries = new int[num_queries];
        for (int j = 0; j < num_queries; j++) {
            getline(input, engine_name);
            cur_case.queries[j] = engines_map[engine_name];
        }
        cur_case.num_engines = num_engines;
        cur_case.num_queries = num_queries;
        // Solve current case
        cout << "Case #" << i+1 << ": " << Solver::solve(cur_case) << endl;
    }

    // Close input file and finish
    input.close();
    return 0;
}

// END OF qualround1.cpp
