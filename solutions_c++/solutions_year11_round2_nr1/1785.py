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

typedef vector<vector<unsigned int> > Table;
typedef vector<double> OWPTable;

void output(const Table& t)
{
    for (size_t i = 0; i < t.size(); ++i) {
        for (size_t j = 0; j < t[i].size(); ++j) {
            cout << t[i][j] << " ";
        }
        cout << endl;
    }
    cout << "--" << endl;
}

double WP(const Table& win, const Table& loss, const unsigned int team)
{
    return double(win[team].size()) / (win[team].size() + loss[team].size());
}

double _OWP(const Table& win, const Table& loss, const unsigned int team1, const unsigned int team2)
{
    size_t wins = win[team2].size();
    size_t losses = loss[team2].size();
    for (size_t i = 0; i < wins; ++i) {
        if (win[team2][i] == team1) {
            --wins;
            break;
        }
    }
    for (size_t i = 0; i < losses; ++i) {
        if (loss[team2][i] == team1) {
            --losses;
            break;
        }
    }
    return double(wins) / (wins + losses);
}
    
double OWP(const Table& win, const Table& loss, const unsigned int team)
{
    size_t count = 0;
    double owp = 0;
    for (size_t i = 0; i < win[team].size(); ++i) {
        owp += _OWP(win, loss, team, win[team][i]);
        ++count;
    }
    for (size_t i = 0; i < loss[team].size(); ++i) {
        owp += _OWP(win, loss, team, loss[team][i]);
        ++count;
    }
    // cout << "owp " << team << " " << owp << " " << count << endl;
    return owp / count;
}

double OOWP(const OWPTable& owpTable, const Table& win, const Table loss, const unsigned int team)
{
    size_t count = 0;
    double oowp = 0;
    for (size_t i = 0; i < win[team].size(); ++i) {
        oowp += owpTable[win[team][i]];
        ++count;
    }
    for (size_t i = 0; i < loss[team].size(); ++i) {
        oowp += owpTable[loss[team][i]];
        ++count;
    }
    // cout << "oowp " << team << " " << oowp << " " << count << endl;
    return oowp / count;
}

int main(int argc, const char* argv[])
{
    size_t T;
    cin >> T;
    for (size_t test = 1; test <= T; ++test) {
        size_t N;
        cin >> N;
        Table win(N);
        Table loss(N);
        for (size_t i = 0; i < N; ++i) {
            string tmp;
            cin >> tmp;
            for (unsigned int j = 0; j < N; ++j) {
                if (tmp[j] == '1')
                    win[i].push_back(j);
                else if (tmp[j] == '0')
                    loss[i].push_back(j);
            }
        }

        // output(win);
        // output(loss);

        OWPTable wpTable(N);
        OWPTable owpTable(N);
        OWPTable oowpTable(N);
        OWPTable rank(N);
        for (size_t i = 0; i < N; ++i) {
            wpTable[i] = WP(win, loss, i);
        }
        
        for (size_t i = 0; i < N; ++i) {
            owpTable[i] = OWP(win, loss, i);
        }

        for (size_t i = 0; i < N; ++i) {
            oowpTable[i] = OOWP(owpTable, win, loss, i);
        }

        for (size_t i = 0; i < N; ++i) {
            rank[i] = 0.25 * wpTable[i] + 0.50 * owpTable[i] + 0.25 * oowpTable[i];
        }
        
        cout << "Case #" << test << ":" << std::endl;

        for (size_t i = 0; i < N; ++i) {
            cout << rank[i] << endl;
        }
    }
    return 0;
}
