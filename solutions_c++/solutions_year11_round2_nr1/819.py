#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

double wp[200];
double aowp[200][200];
double owp[200];
double oowp[200];

char schedule[200][200];

int main()
{
	int T;
	scanf("%d",&T);
	for (int test=1; test<=T; ++test)  {

		memset(wp, 0, sizeof(wp));
		memset(aowp, 0, sizeof(aowp));
		memset(owp, 0, sizeof(owp));
		memset(oowp, 0, sizeof(oowp));

		int N;
		scanf("%d",&N);
		for (int team=0; team<N; ++team) {
			scanf("%s",schedule[team]);
		}

		// calc wp
		for (int team=0; team<N; ++team) {
			int total = 0, win = 0;
			for (int opp=0; opp<N; ++opp) {
				if (schedule[team][opp] == '.') continue;
				total++;
				if (schedule[team][opp] == '1') win++;
			}
			wp[team] = (double)win / (double) total;
		}

		// calc aowp
		for (int team=0; team<N; ++team) {
			for (int skip=0; skip<N; ++skip) {
				if (schedule[team][skip] == '.') continue;
				int total = 0, win = 0;
				for (int opp=0; opp<N; ++opp) {
					if (schedule[team][opp] == '.') continue;
					if (opp == skip) continue;
					total++;
					if (schedule[team][opp] == '1') win++;
				}
				aowp[team][skip] = (double) win / (double) total;
			}
		}

		// calc owp
		for (int team=0; team<N; ++team) {
			double sum = 0.0;
			int total = 0;
			for (int opp=0; opp<N; ++opp) {
				if (schedule[team][opp] == '.') continue;
				total++;
				sum += aowp[opp][team];
			}
			owp[team] = sum / (double)total;
		}

		// calc oowp
		for (int team=0; team<N; ++team) {
			int total = 0;
			double sum = 0.0;
			for (int opp=0; opp<N; ++opp) {
				if (schedule[team][opp] == '.') continue;
				total++;
				sum += owp[opp];
			}
			oowp[team] = sum / (double) total;
		}
		printf("Case #%d:\n", test);
		for (int team=0; team<N; ++team) {
			double rpi = (0.25) * wp[team] + (0.5) * owp[team] + (0.25) * oowp[team];
			printf("%.8f\n",rpi);
		}
	}

	return 0;
}