/* 
Google Codejam 2010
C. Theme Park

C++ Solution by:
 Marco Chiesi
 chiesi@gmail.com
*/

#include <string>
#include <sstream>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

/**
 * Class for a single instance of the problem
 */
class Instance {
    private:
        int solution;
        int R, k, N;
        int *g;
        vector<int> seq;
        vector<int> seq_revenue;

    public:
	void readInput(istream &in) {
        in >> R >> k >> N;
        g = new int[N];
		for (int i = 0; i < N ; i++) {
            in >> g[i];
        }
	}

	void solve() {
        int group = 0;
        int total_rides = 0;
        int rides = 0;
        long long total_revenue = 0;
        long long ride_revenue = 0;
        do {
            int ride_first_group = group;
            ride_revenue = 0;
            while (ride_revenue + g[group] <= k) {
                ride_revenue += g[group];
                group = (group + 1) % N;
                if (ride_first_group == group) {
                    break;
                }
            }
            seq.push_back(ride_first_group);
            seq_revenue.push_back(ride_revenue);
            rides ++;
        }
        while (find(seq.begin(),seq.end(), group) == seq.end() && rides < R);
        if (rides == R) {
            for (vector<int>::iterator i = seq.begin(); i < seq.end(); i++) {
                total_revenue += seq_revenue[i-seq.begin()];
            }
        }
        else {
            // Adding pre cycles
            int pre_cycle_rides = find(seq.begin(), seq.end(), group) - seq.begin();
            for (int i = 0; i < pre_cycle_rides; i++) {
                total_revenue += seq_revenue[i];
            }
            total_rides += pre_cycle_rides;
            // Adding cycles
            int cycle_rides = rides - pre_cycle_rides;
            int cycles = (R - pre_cycle_rides) / cycle_rides;
            long cycle_revenue = 0;
            for (vector<int>::iterator i = find(seq.begin(), seq.end(), group); i < seq.end(); i++) {
                cycle_revenue += seq_revenue[i-seq.begin()];
            }
            total_revenue += cycles * cycle_revenue;
            total_rides += cycles * cycle_rides;
            // Adding post cycles
            int remaining_rides = R - total_rides;
            vector<int>::iterator current = find(seq.begin(), seq.end(), group);
            for (int i = 0; i < remaining_rides; i++) {
                total_revenue += seq_revenue[current - seq.begin()];
                current ++;
                total_rides ++;
            }
        }
    	solution = total_revenue;
	}

	string getSolution() {
    	stringstream ss;
        ss << solution;
		return ss.str();
	}
};

/**
 * Class for a problem
 */
class Problem {
	private:
        Instance *instances;
	    int cases;
	
	public:
	void readInput(istream &in) {
		in >> cases;
		instances = new Instance[cases];
		for (int i = 0; i < cases; i++) {
			instances[i].readInput(in);
		}
	}
	
	void solve() {
		for (int i = 0; i < cases; i++) {
			instances[i].solve();
		}
	}
	
	void writeOutput(ostream &out) {
		for (int i = 0; i < cases; i++) {
			out << "Case #" << i+1 << ": " << instances[i].getSolution() << endl;
		}
	}
};

/**
 * Main function
 */
int main(int argc, char *argv[]) {
    istream *in;
    ostream *out;
    if (argc > 1) {
        in = new fstream(argv[1], fstream::in);
    }
    else {
        in = &cin;
    }
    if (argc > 2) {
        out = new fstream(argv[2], fstream::out);
    }
    else {
        out = &cout;
    }
    Problem *problem = new Problem();
    problem->readInput(*in);
    problem->solve();
    problem->writeOutput(*out);
    return 0;
}
