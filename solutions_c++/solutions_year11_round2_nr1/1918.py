#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define BOT 2

struct Instance {
    int n;
    vector<vector<bool > > played;
    vector<vector<int> > results;
    vector<int> num_of_opponents;
    Instance(int _n)
        : n(_n),
          num_of_opponents(vector<int>(n, 0)),
          results(vector<vector<int> >(n, vector<int>(n, 0))),
          played(vector<vector<bool> >(n, vector<bool>(n, false)))
    {}
};


void readInput(vector<Instance>* instances) {
    int numTests;
    cin >> numTests;

    for(int i = 0; i < numTests; ++i) {
        int numTeams;
        cin >> numTeams;

        Instance current(numTeams);

        for(int t = 0; t < numTeams; ++t) {
            string results;
            cin >> results;
            int num_opp = 0;
            for(int c = 0; c < results.length(); ++c) {
                switch(results[c]) {
                    case '.':
                        break;
                    case '1':
                        ++num_opp;
                        current.played[t][c] = true;
                        current.results[t][c] = 1;
                        //cout << "res[" << t << "][" << c << "] = " << current.results[t][c] << endl;
                        break;
                    case '0':
                        current.played[t][c] = true;
                        ++num_opp;
                        break;
                }
            }
            current.num_of_opponents[t] = num_opp;
        }
        instances->push_back(current);
    }
}

vector<double> solve(const Instance& instance) {
    const int n = instance.n;
    vector<vector<int> > exc_sums(instance.n, vector<int>(instance.n, 0));

    for(int i = 0; i < n; ++i) {
        int acc = 0;
        for(int j = 0; j < n; ++j) {
            exc_sums[i][j] = acc;
            acc += instance.results[i][j];
        }
        int acc1 = 0;
        for(int j = n - 1; j >= 0; --j) {
            exc_sums[i][j] += acc1;
            acc1 += instance.results[i][j];
        }
    }
    //for(int i = 0; i < n; ++i) for(int j = 0; j < n; ++j) cout << "e[" << i << "][" << j << "] = " << exc_sums[i][j] << endl;

    vector<double> wp(n, 0.0);
    for(int i = 0; i < n; ++i) {
        double sum = 0;
        for(int j = 0; j < n; ++j) {
            sum += instance.results[i][j];
        }
        if(instance.num_of_opponents[i]) {
            wp[i] = sum / instance.num_of_opponents[i];
            //cout << "wp[" << i << "]" << wp[i] << endl;
        }
    }

    vector<double> owp(n, 0.0);
    for(int i = 0; i < n; ++i){
        double sum = 0;
        for(int j = 0; j < n; ++j) {
            if(instance.played[i][j]) {
                sum += exc_sums[j][i] / float(instance.num_of_opponents[j] - 1);
            }
        }
        owp[i] = sum / instance.num_of_opponents[i];
        //cout << "owp[" << i << "]" << owp[i] << " " << sum << endl;
    }

    vector<double> oowp(n, 0.0);
    for(int i = 0; i < n; ++i) {
        double sum = 0;
        for(int j = 0; j < n; ++j) {
            if(instance.played[i][j]) {
                //cout << "P" << i << " " << j << endl;
                sum += owp[j];
            }
        }
        oowp[i] = sum / instance.num_of_opponents[i];
        //cout << "oowp " << i << " " << sum << " " << oowp[i] << " " << instance.num_of_opponents[i]  << endl;
    }

    vector<double> results(n, 0);
    for(int i = 0; i < n; ++i) {
        results[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
    }

    return results;
}

void outputAnswer(int n, const vector<double>& ans) {
    cout << "Case #" << n + 1 << ":" << endl;
    for(int i = 0; i < ans.size(); ++i) {
        cout << ans[i] << endl;
    }
}

int main() {
    vector<Instance> input;
    readInput(&input);
    for(int i = 0; i < input.size(); ++i) {
        outputAnswer(i, solve(input[i]));
    }
    return 0;
}
