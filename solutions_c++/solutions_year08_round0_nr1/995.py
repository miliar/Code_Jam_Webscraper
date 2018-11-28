#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
using namespace std;

typedef vector<int> intlist;
typedef pair<int, int> intpair;

intpair select_engine(int start, int engine_n, const intlist & queries) {
    int engine = 0;
    int length = 0;
    int max = 0;
    intpair ret(0, 0);

    for (int engine = 0; engine < engine_n; ++engine) {
        length = 0;
        while ((start+length) < queries.size() && engine != queries[start+length])
            ++length;
        if (length > max) {
            ret = intpair(engine, length);
            max = length;
        }
    }

    return ret;
}

int solve(int engine_n, const intlist & queries) {
    int ret = 0;
    int cur = 0;
    int engine = 0;
    int length = 0;
    intpair onestep;

    while (cur < queries.size()) {
        onestep = select_engine(cur, engine_n, queries);
        engine = onestep.first;
        length = onestep.second;
        //cout << "engine " << engine << ", length " << length << endl;
        cur += length;
        ++ret;
    }

    return ret;
}

void load_case(ifstream & fin, int & engine_n, intlist & queries) {
    engine_n = 0;
    queries.clear();

    char buf[128];

    memset(buf, 0x00, 128);
    fin.getline(buf, 128);
    int e_n = atoi(buf);
    engine_n = e_n;
    map<string, int> name_to_n;
    for (int i = 0; i < e_n; ++i) {
        memset(buf, 0x00, 128);
        fin.getline(buf, 128);
        name_to_n[buf] = i;
    }

    memset(buf, 0x00, 128);
    fin.getline(buf, 128);
    int q_n = atoi(buf);
    for (int i = 0; i < q_n; ++i) {
        memset(buf, 0x00, 128);
        fin.getline(buf, 128);
        queries.push_back(name_to_n[buf]);
    }
}

int main(int argc, char * argv[]) {
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " [inputfile]" << endl;
        return -1;
    }

    ifstream fin(argv[1]);

    char buf[128];

    memset(buf, 0x00, 128);
    fin.getline(buf, 128);
    int case_n = atoi(buf);

    int engine_n = 0;
    intlist queries;

    for (int i = 0; i < case_n; ++i) {
        load_case(fin, engine_n, queries);
        cout << "Case #" << i+1 << ": " << max(solve(engine_n, queries)-1, 0) << endl;
    }

    fin.close();

    return 0;
}
