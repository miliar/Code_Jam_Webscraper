#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <numeric>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <iomanip>
using namespace std;
const double EPS = 1.0e-9;
enum CONDITION { MELTED, UNMELTED, NONE };

bool bt(vector<vector<pair<int,int> > >& requests, int id, vector<int>& batch)
{
    if (id == requests.size()) return true;
    vector<pair<int,int> > customer = requests[id];
    int sz = customer.size();
    for (int i = sz-1; i >= 0; i--) {
        int cond = batch[customer[i].first];
        if (cond == NONE || cond == customer[i].second) {
            batch[customer[i].first] = customer[i].second;
            if (bt(requests, id+1, batch)) 
                return true;
            batch[customer[i].first] = cond;
        }
    }
    return false;
}

int main(void)
{
    int C, N, M, T, X, Y;
    cin >> C;

    for (int caseId = 1; caseId <= C; caseId++) {
        cin >> N >> M;
        vector<int> batch(N+1);
        for (int i = 0; i < N+1; i++)
            batch[i] = NONE;
        bool isImpossible = false;
        vector<vector<pair<int,int> > > requests;
        for (int i = 0; i < M; i++) {
            cin >> T;
            if (T == 1) {
                cin >> X >> Y;
                if (Y == 0 && batch[X] == MELTED || 
                        Y == 1 && batch[X] == UNMELTED) 
                    isImpossible = true;
                else 
                    batch[X] = (Y == 0) ? UNMELTED : MELTED;
                continue;
            }
            vector< pair<int,int> > customer;
            for (int j = 0; j < T; j++) {
                cin >> X >> Y;
                if (Y == 1) {
                    if (customer.empty()) 
                        customer.push_back(pair<int,int>(X,MELTED));
                    else {
                        pair<int,int> tmpPair = customer[0];
                        customer[0] = pair<int,int>(X,MELTED);
                        customer.push_back(tmpPair);
                    }
                } else 
                    customer.push_back(pair<int,int>(X,UNMELTED));
            }
            requests.push_back(customer);
        }
        cout << "Case #" << caseId << ":";
        if (isImpossible || !bt(requests, 0, batch)) {
            cout << " IMPOSSIBLE" << endl;
        } else {
            for (int i = 1; i <= N; i++) {
                if (batch[i] == MELTED)
                    cout << " " << 1;
                else
                    cout << " " << 0;
            }
            cout << endl;
        }
    }

    return 0;
}

