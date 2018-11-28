#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int solve(int begin, int S, int Q, int queries[]) {
    int maxdist = 0, i, distances[S];
    for (i = 0; i < S; i++) distances[i] = Q;
    for (i = begin; i < Q; i++) if (distances[queries[i]] == Q) distances[queries[i]] = i;
    for (i = 0; i < S; i++) {
        if (distances[i] == Q) return 0;
        else if (distances[i] > maxdist) maxdist = distances[i];
    }
    return 1 + solve(maxdist, S, Q, queries);
}

int main () {
    int N, S, Q, j;
    string tmp;
    cin >> N;
    for (int i = 1; i <= N; i++) {
        cin >> S;
        cin.ignore();
        string engines[S];
        for (j = 0; j < S; j++) getline(cin, engines[j], '\n');
        cin >> Q;
        cin.ignore();
        string query;
        int queries[Q];
        for (j = 0; j < Q; j++) {
            getline(cin, query);
            for (int k = 0; k < S; k++) if (query == engines[k]) queries[j] = k;
        }
        cout << "Case #" << i << ": " << solve(0, S, Q, queries) << endl;
    }
}
