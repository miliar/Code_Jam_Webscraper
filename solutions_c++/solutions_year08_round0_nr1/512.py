#include <map>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
void trim(string &s) {
     s = s.erase(s.find_last_not_of("\r\n") + 1);
     s = s.erase(0, s.find_first_not_of("\r\n"));
}
int solve(const vector<string> &q, int Q) {
    string temp;
    vector<int> solutions(q.size(), 0);
    int res = 0;
    while (Q) {
        getline(cin, temp); trim(temp);
	if (temp == "") continue;
	int ok = 0, wh = -1;
	for (int x = 0; x < q.size(); x++) {
	    if (q[x] == temp) solutions[wh = x]++;
	    if (solutions[x] == 0) ok = 1;
	}
	if (!ok) {
	    for (int x = 0; x < q.size(); x++) solutions[x] = 0;
	    solutions[wh] = 1;
	    res++;
	}
	Q--;
    }
    return res;
}
void proc(int i) {
    int S, Q;
    string temp;
    vector<string> queries;
    cin >> S;
    while (S) {
        getline(cin, temp); trim(temp);
	if (temp == "") continue;
	queries.push_back(temp);
	S--;
    }
    cin >> Q;
    cout << "Case #" << i << ": ";
    cout << solve(queries, Q) << endl;
}
int main(int argc, char **argv) {
    int N, i = 1;
    cin >> N;
    while (N--) proc(i++);
    return 0;
}

