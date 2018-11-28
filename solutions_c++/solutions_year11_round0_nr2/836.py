#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <deque>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <ctime>

using namespace std;

#define all(v) (v).begin(), (v).end()

const double PI = 3.1415926535897932384626433832795;
const double EPS = 1e-9;
const int INF = 1000 * 1000;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<char, char> pcc;

struct button {
    int owner_id, number;
    button(int some_owner_id, int some_number) 
        : owner_id(some_owner_id)
        , number(some_number)
    {}
};

const char NONE = '$';

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cerr << test << endl;
        int c;
        cin >> c;
        map<pcc, char> combination;
        for (int i = 0; i < c; ++i) {
            string next_token;
            cin >> next_token;
            char first = next_token[0], second = next_token[1], result = next_token[2];
            combination[pcc(first, second)] = combination[pcc(second, first)] = result;
        }
        int D;
        cin >> D;
        vector<vector<char> > opposed(256);
        for (int i = 0; i < D; ++i) {
            string next_token;
            cin >> next_token;
            char first = next_token[0], second = next_token[1];
            opposed[first].push_back(second);
            opposed[second].push_back(first);
        }
        string invoke, spam;
        cin >> spam;
        cin >> invoke;
        char last_char = NONE;
        string sequence;
        multiset<char> symbols_in_sequence;
        for (int i = 0; i < invoke.size(); ++i) {
            char cur = invoke[i];
            if (combination.count(pcc(last_char, cur))) {
                symbols_in_sequence.erase(symbols_in_sequence.find(last_char));
                sequence.pop_back();
                last_char = combination[pcc(last_char, cur)];
                sequence.push_back(last_char);
                symbols_in_sequence.insert(last_char);
                continue;
            }
            bool deleted = false;
            for (int j = 0; j < opposed[cur].size(); ++j) {
                if (symbols_in_sequence.find(opposed[cur][j]) != symbols_in_sequence.end()) {
                    sequence.clear();
                    last_char = NONE;
                    symbols_in_sequence.clear();
                    deleted = true;
                    break;
                }
            }
            if (deleted) {
                continue;
            }
            last_char = cur;
            sequence.push_back(last_char);
            symbols_in_sequence.insert(last_char);
        }
        string result = "[";
        for (int i = 0; i < sequence.size(); ++i) {
            result.push_back(sequence[i]);
            if (i + 1 != sequence.size()) {
                result += ", ";
            }
        }
        result.push_back(']');
        printf("Case #%d: %s\n", test, result.c_str());
    }
	return 0;
}
