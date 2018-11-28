#include <iostream>
#include <set>
#include <iomanip>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <fstream>
using namespace std;

int main() {
  ifstream cin("A-large (4).in");
  ofstream cout("out.txt");
  int T;
  cin >> T;
  for(int tt = 1; tt <= T; tt++) {
    int X, S, R, t, N;
    cin >> X >> S >> R >> t >> N;
    vector<int> B(N), E(N), w(N);
    for(int i = 0; i < N; i++)
        cin >> B[i] >> E[i] >> w[i];
    vector<pair<int, int> > wt(N);
    int length = 0;
    for(int i = 0; i < N; i++) {
        wt[i] = make_pair(w[i], E[i]-B[i]);
        length += (E[i]-B[i]);
    }
    sort(wt.rbegin(), wt.rend());
    wt.push_back(make_pair(0, X-length));
    double time = 0;
    int i = 0;
    for(i = N; i >= 0; i--) {
        double needTime = (wt[i].second * 1.)/(wt[i].first+R);
        if(time > t) {
            time += (wt[i].second * 1.)/(wt[i].first+S);
            continue;
        }
        if(time + needTime > t) {
            time = t + (wt[i].second - (t - time)*(wt[i].first+R)) / (wt[i].first + S);
        } else
            time += needTime;
    }
    cout << "Case #" << tt << ":";
    cout << " ";
    cout.precision(15);
    cout << time;
    cout << endl;
  }
}
