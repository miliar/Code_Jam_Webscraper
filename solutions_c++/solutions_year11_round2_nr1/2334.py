#include <iostream>
#include <vector>

using namespace std;

struct Game {
	int op;
	int win;
};

struct Team {
	double WP, OWP ,OOWP;
	vector<Game> ops;
};

int main() {
	int T,N;
	
	cin >> T;
	
	for (int i=0; i<T; i++) {
		cin >> N;
		
		Team teams[N];
		string inp;
		getline(cin, inp);
		for (int j=0; j<N; j++) {
			getline(cin, inp);

			int count = 0;
			for (int k=0; k<N; k++) {
				if (inp[k] == '1') count++;
				
				if (inp[k] != '.') {
					Game gm;
					gm.op = k;
	
					if (inp[k] == '1') gm.win = 0;
					else gm.win = 1;
					teams[j].ops.push_back(gm);
				
				}
			}
			teams[j].WP = ((double) count) / ( (double) teams[j].ops.size());
		}
		
		for (int j=0; j<N; j++) {
			vector<Game>::iterator it;
			
			double totWP=0;
			for (it = teams[j].ops.begin(); it < teams[j].ops.end(); it++) {
				double tmpWP = teams[(*it).op].WP * teams[(*it).op].ops.size() - (*it).win;
				
				totWP += (tmpWP / (double) (teams[(*it).op].ops.size() -1));
				
			}
			
			teams[j].OWP = totWP / teams[j].ops.size();
		}
		
		cout << "Case #" << (i+1) << ":\n";
		for (int j=0; j<N; j++) {
			vector<Game>::iterator it;
			
			double totOWP=0;
			for (it = teams[j].ops.begin(); it < teams[j].ops.end(); it++) {
				totOWP += teams[(*it).op].OWP;
			}
			
			teams[j].OOWP = totOWP / teams[j].ops.size();
			
			double RPI = (0.25 * teams[j].WP) + (0.50 *teams[j].OWP) + (0.25 * teams[j].OOWP);
			
			cout << RPI << "\n";			
		}
		
	}
}
