#include <stdio.h>
#include <assert.h>

struct team {
    int m[100];
    int o[100];
    int w;
    int no;
    double owp;
    double oowp;
} g[100];

int trad (char c) {
    if (c == '.')
	return -1;
    else if (c == '1')
	return 1;
    else if (c == '0')
	return 0;
    assert(false);
    return -1;
}

int main (void) {
    int T;
    int scanned = scanf("%d", &T);
    for (int currentcase = 1; currentcase <= T; ++currentcase) {
	printf("Case #%d:\n", currentcase);
	int n;
	scanned = scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
	    getchar();
	    g[i].w = 0;
	    g[i].no = 0;
	    for (int j = 0; j < n; ++j) {
		int rel = trad(getchar());
		g[i].m[j] = rel;
		if (rel != -1) {
		    g[i].o[g[i].no] = j;
		    g[i].no++;
		    if (rel == 1) {
			g[i].w++;
		    }
		}
	    }
	}
	for (team *it = g; it < g + n; ++it) {
	    it->owp = 0;
	    for (int j = 0; j < it->no; ++j) {
		int opp = it->o[j];
		it->owp += ((double) g[opp].w + ((it->m[opp] == 0) ? (-1) : (0))) / ((double) g[opp].no - 1);
	    }
	    it->owp /= it->no;
	}
	for (team *it = g; it < g + n; ++it) {
	    double oowp = 0;
	    for (int j = 0; j < it->no; ++j) {
		oowp += g[it->o[j]].owp;
	    }
	    oowp /= it->no * 4;
	    oowp += ((double) it->w)/((double) it->no * 4) + it->owp / 2;
	    printf("%.8lf\n", oowp);
	}
    }
    return 0;
}
