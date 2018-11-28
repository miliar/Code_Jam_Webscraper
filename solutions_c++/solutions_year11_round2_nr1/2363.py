#include "stdio.h"
#include "Fraction.h"
#define dprint if(false) printf

class Team;

extern Team teams[];
int grid[100][100];
int n;

class Team {
	public:

	Fraction rpi, wp, owp, oowp;
	int id;
	int wins;
	int loses;

	Team() {
		id = 0;
		wins = loses = 0;
	}

	Team(int i) {
		wins = loses = 0;
		id = i;
	}

	void calculate_wp() {
		wins = loses = 0;
		for(int i=0; i<n; i++) {
			int result = grid[id][i];
			if(result == 1) {
				wins++;
			} else if(result == 0) {
				loses++;
			}
		}
		dprint("wp = %d/%d\n", wins, wins+loses);
		wp = Fraction(wins, wins+loses);
	}

	Fraction get_wp(int exclude_id) {
		if(grid[id][exclude_id] == 1) {
			return Fraction(wins-1, wins+loses-1);
		} else if(grid[id][exclude_id] == 0) {
			return Fraction(wins, wins+loses-1);
		} else {
			return wp;
		}
	}

	void calculate_owp() {
		Fraction sum;
		int antal = 0;
		for(int i=0; i<n; i++) {
			if((grid[id][i] == 0) || (grid[id][i] == 1)) {
				sum = sum + teams[i].get_wp(id);
				antal++;
			}
		}
		dprint("owp = (%s)/%d\n", sum.get_string().c_str(), antal);
		owp = sum / Fraction(antal);
	}

	Fraction get_owp() {
		return owp;
	}

	void calculate_oowp() {
		Fraction sum;
		int antal = 0;
		for(int i=0; i<n; i++) {
			if((grid[id][i] == 0) || (grid[id][i] == 1)) {
				sum = sum + teams[i].get_owp();
				antal++;
			}
		}
		dprint("oowp = (%s)/%d\n", sum.get_string().c_str(), antal);
		oowp = sum / Fraction(antal);
	}

	Fraction get_rpi() {
		rpi = Fraction(1, 4) * wp;
		rpi = rpi + Fraction(1, 2) * owp;
		rpi = rpi + Fraction(1, 4) * oowp;
		return rpi;
	}
};

Team teams[100];

int main() {
	freopen("rpi.in", "r", stdin);
	freopen("rpi.out", "w", stdout);
	int T;
	scanf("%d", &T);

	for(int i=0; i<T; i++) {
		scanf("%d", &n);
		for(int j=0; j<n; j++) {
			for(int k=0; k<n; k++) {
				char ch;
				do {
				scanf("%c", &ch);
				} while(ch == '\n');
				if(ch == '1') {
					grid[j][k] = 1;
				} else if(ch == '0') {
					grid[j][k] = 0;
				} else {
					grid[j][k] = -1;
				}
			}
		}

		for(int j=0; j<n; j++) {
			teams[j].id = j;
			teams[j].calculate_wp();
		}

		for(int j=0; j<n; j++) {
			teams[j].calculate_owp();
		}

		for(int j=0; j<n; j++) {
			teams[j].calculate_oowp();
		}

		printf("Case #%d:\n", i+1);
		for(int j=0; j<n; j++) {
			printf("%.12Lf\n", teams[j].get_rpi().get_double());
		}
	}
}
