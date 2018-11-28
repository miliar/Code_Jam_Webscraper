/* Karolis Narkevicius */

#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

class Snapper
{
	private:
		vector<vector<long> > lookup;
		
	public:
		void init() {
			int N = 30;
			long K = 100000000;

			for (long j=0; j<=N; j++) {
				lookup.push_back(vector <long>());
			}

			bool *state = new bool[N+1];
			bool *power = new bool[N+1];

			//initialize
			state[0] = true;
			power[0] = true;
			for (int i=1; i<=N; i++) {
				state[i] = false;
				power[i] = false;
			}
			power[1] = true;

			for (long kk=1; kk<=K; kk++) {
				for (int nn=1; nn<=N; nn++) {
					if (power[nn]) {
						state[nn] = !state[nn];
					}
					power[nn] = state[nn-1]&&power[nn-1];
					if (state[nn]&&power[nn]) {
						lookup[nn].push_back(kk);
					}
				}
				if (kk%10000000==0) {
					//just for observing the progress..
					cout << kk << endl;
				}
			}
		}

		bool snap(int N, long K)
		{
			return binary_search(lookup[N].begin(), lookup[N].end(), K);
		}
};

bool snapSmall(int N, long K)
{
	bool *state = new bool[N+1];
	bool *power = new bool[N+1];

	//initialize
	state[0] = true;
	power[0] = true;
	for (int i=1; i<=N; i++) {
		state[i] = false;
		power[i] = false;
	}
	power[1] = true;

	for (long kk=0; kk<K; kk++) {
		for (int i=1; i<=N; i++) {
			if (power[i]) {
				state[i] = !state[i];
			}
			power[i] = state[i-1]&&power[i-1];
		}
	}

	return state[N]&&power[N];
}

void runSmall() {
	int CASES, N;
	long K;
	string a;
	ifstream infile;
	ofstream outfile;

	infile.open("A-small.in");
	outfile.open ("A-small.out");
	infile >> CASES;
	for (int i=1; i<=CASES; i++) {
		infile >> N;
		infile >> K;
		if (snapSmall(N, K)) {
			a = "ON";
		} else {
			a = "OFF";
		}
		outfile << "Case #" << i << ": " << a << endl;
	}
	infile.close();
	outfile.close();
}

void runLarge() {
	int CASES, N;
	long K;
	string a;
	ifstream infile;
	ofstream outfile;

	Snapper s;
	s.init();

	infile.open("A-large.in");
	outfile.open ("A-large.out");
	infile >> CASES;
	for (int i=1; i<=CASES; i++) {
		infile >> N;
		infile >> K;
		if (s.snap(N, K)) {
			a = "ON";
		} else {
			a = "OFF";
		}
		outfile << "Case #" << i << ": " << a << endl;
	}
	infile.close();
	outfile.close();
}

int main()
{
	runLarge();
	return 0;
}