#include <iostream>
#include <cstddef>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <utility>
#include <boost/unordered_map.hpp>
#include <boost/foreach.hpp>

using namespace std;

typedef vector<char> Row;
typedef vector<Row> Table;


bool paint(Table& t, long R, long C)
{
    for (long i = 0; i < R; ++i) {
        for (long j = 0; j < C; ++j) {
            if (t[i][j] == '#') {
                if (i < R - 1 && j < C - 1 && t[i+1][j] == '#' && t[i][j+1] == '#' && t[i+1][j+1] == '#') {
                    t[i][j] = '/'; t[i][j+1] = '\\';
                    t[i+1][j] = '\\'; t[i+1][j+1] = '/';
                } else
                    return false;
            } 
        }
    }
    return true;
}

void output(const Table& t)
{
    for (size_t i = 0; i < t.size(); ++i) {
        for (size_t j = 0; j < t[i].size(); ++j) {
            cout << t[i][j];
        }
        cout << endl;
    }
}

int main(int argc, const char* argv[])
{
    size_t T;
    cin >> T;
    for (size_t test = 1; test <= T; ++test) {
        long R, C;
        cin >> R >> C;
        Table table(R);
        for (long i = 0; i < R; ++i) {
            table[i] = Row(C);
            string tmp;
            cin >> tmp;
            for (long j = 0; j < C; ++j) {
                table[i][j] = tmp[j];
            }
        }
        
        //output(table);
        bool ok = paint(table, R, C);
        cout << "Case #" << test << ":" << std::endl;
        if (ok) {
            output(table);
        } else {
            cout << "Impossible" << endl;
        }

    }
    return 0;
}
