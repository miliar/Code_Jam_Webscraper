#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;

const int INF = 1000000;
const int UNDEF = -1;

int main() {
    int N, S, Q;

    cin >> N;
    for(int n = 1; n <= N; n++) {
        vector<string> servers, queries;
        vector< vector<int> > cost;
        vector<int> minCost;

        cin >> S;
        servers.resize(S);
        cin.ignore(10, '\n');
        for(int i = 0; i < S; i++) {
            getline(cin, servers[i]);
        }

        cin >> Q;
        queries.resize(Q);
        cin.ignore(10, '\n');
        for(int i = 0; i < Q; i++) {
            getline(cin, queries[i]);
        }

        cost.resize(Q, vector<int>(S, UNDEF));
        minCost.resize(Q, INF);

        for(int i = 0; i < Q; i++) {
            for(int j = 0; j < S; j++) {
                if(queries[i] == servers[j]) {
                    cost[i][j] = INF;
                } else if(i == 0) {
                    cost[i][j] = 0;
                } else if(i == 1) {
                    cost[i][j] = (cost[i - 1][j] == INF ? 1 : 0);
                } else if(cost[i - 1][j] == INF) {
                    cost[i][j] = minCost[i - 1] + 1;
                } else {
                    cost[i][j] = cost[i - 1][j];
                }
                cost[i][j] = min(cost[i][j], INF);
                minCost[i] = min(min(minCost[i], cost[i][j]), INF);

//                if(cost[i][j] == INF) cerr << "_ ";
//                else cerr << cost[i][j] << " ";
            }
//            cerr << "| " << minCost[i] << endl;
        }
//        cerr << endl;
    
        cout << "Case #" << n << ": " << (cost.empty() ? 0 : *min_element(cost.back().begin(), cost.back().end())) << endl;
    }
    return 0;
}
