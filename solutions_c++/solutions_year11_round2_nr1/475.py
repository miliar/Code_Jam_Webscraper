#include <cstdio>

using namespace std;

const int MAXN = 100+5;
int n;
char g[MAXN][MAXN];

int wins[MAXN];
int games[MAXN];

double WP[MAXN];
double OWP[MAXN];
double OOWP[MAXN];

void solve(int caseNumber) {
	printf("Case #%d:\n", caseNumber);
	scanf("%d", &n);
	for(int i = 0; i < n; i++) scanf("%s", g[i]);

	for(int i = 0; i < n; i++) {
		games[i] = wins[i] = 0;
		for(int j = 0; j < n; j++) {
			if(g[i][j] == '.') continue;
			games[i]++;
			if(g[i][j] == '1') wins[i]++;
		}
	}


	for(int i = 0; i < n; i++) {
		WP[i] = double(wins[i])/games[i];

		double owp = 0;
		int numberOpponnents = 0;
		for(int j = 0; j < n; j++) {
			if(g[i][j] == '.') continue;
			numberOpponnents++;
			int owpGames = games[j];
			int owpWins = wins[j];
			if(g[j][i] != '.') owpGames--;
			if(g[j][i] == '1') owpWins--;

			owp += double(owpWins)/owpGames;
		}
		OWP[i] = owp/numberOpponnents;		
	}

	for(int i = 0; i < n; i++) {
		double sum = 0;
		int number = 0;
		for(int j = 0; j < n; j++) {
			if(g[i][j] == '.') continue;
			number++;
			sum += OWP[j];
		}
		OOWP[i] = sum/number;	

	}

	for(int i = 0; i < n; i++) {
		double RPI = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
		printf("%.10lf\n", RPI);
	}


}


int main() {

	//freopen("in.txt", "r", stdin);
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) solve(i);
}