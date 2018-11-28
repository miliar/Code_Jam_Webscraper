#include <iostream>
#include <fstream>
#include <set>

using namespace std;

using namespace std;
int main(int argc, char* argv[]) {
    int debug = atoi(argv[2]);
    ifstream fin(argv[1]);    
    int MAX_LENGTH = 100;
    char line[MAX_LENGTH];
    int step = 0;
    fin.getline(line, MAX_LENGTH);
    int num_cases = atoi(line);
    set<string> queries; 
    for (int i = 0; i < num_cases; i ++) {
        queries.clear();
        fin.getline(line, MAX_LENGTH);
        int num_engines = atoi(line);
        if (debug) cout << num_engines << endl;
        for (int j = 0; j < num_engines; j ++) {
            fin.getline(line, MAX_LENGTH);
        }
        fin.getline(line, MAX_LENGTH);
        int num_queries = atoi(line);
        if (debug) cout << num_queries << endl;
        int total = 0;
        int count = 0;
        for (int j = 0; j < num_queries; j ++) {
            fin.getline(line, MAX_LENGTH);
            if (debug) cout << "query " << line;
            if (queries.insert(line).second) {
                count ++;
                if (count == num_engines) {
                    total ++;
                    queries.clear();
                    queries.insert(line);
                    count = 1;
                }
           }
           if (debug) cout << " count " << count;
           if (debug) cout << " total " << total << endl;
        }
        cout << "Case #" << (i+1) << ": " << total << endl;
    }
}
