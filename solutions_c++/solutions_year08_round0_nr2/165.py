#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

class max_matcher
{
    public:
        static const int MaxV = 1024;

        int V, VLeft;
        vector<int> next[MaxV];
		int match_size, match[MaxV];
		
    private:
        int final, prev[MaxV];

        /* Find augumenting path */
        bool findpath(int v)
        {
            FOREACH(pv, next[v]) {
                if (prev[*pv] != -1)
                    continue;

                prev[*pv] = v;
                if (match[*pv] == -1) {
                    final = *pv;
                    return true;
                }

                int u = match[*pv];
                if (prev[u] != -1)
                    continue;
                prev[u] = *pv;
                if (findpath(u))
                    return true;
            }
            return false;
        }

        /* Augument the path */
        inline void augument()
        {
            int u = prev[final], v = final;
            while (1) {
                match[u] = v;
                match[v] = u;
                if (prev[u] == u)
                    break;
                v = prev[u];
                u = prev[v];
            }
            match_size++;
        }

    public:
        max_matcher() : V(0), VLeft(0) { clear_match(); }
        max_matcher(int V, int VLeft) : V(V), VLeft(VLeft) { clear_match(); }

        void clear_match()
        {
            match_size = 0;
            for (int i = 0; i < V; i++)
                match[i] = -1;
        }

        size_t max_match()
        {
            while (1) {
                size_t cur_size = match_size;
                for (int i = 0; i < V; i++)
                    prev[i] = -1;

                for (int i = 0; i < VLeft; i++)
                    if ((match[i] == -1) && (prev[i] == -1)) {
                        prev[i] = i;
                        if (findpath(i))
                            augument();
                    }

                if (cur_size == match_size)
                    break;
            }
            return match_size;
        }
};

pair<int, int> readScheduleItem()
{
	int hh1, mm1, hh2, mm2;
	scanf("%02d:%02d %02d:%02d\n", &hh1, &mm1, &hh2, &mm2);
	return make_pair(hh1*60 + mm1, hh2*60 + mm2);
}

void solve(int iTest)
{
	// Read data
	int T, NA, NB, N;
	scanf("%d %d %d\n", &T, &NA, &NB);
	N = NA+NB;

	vector< pair<int, int> > schedule(N);
	for (int i = 0; i < N; i++)
	    schedule[i] = readScheduleItem();
	
	// Build NxN bipartite graph
	max_matcher matcher(N*2, N);
	for (int i = 0; i < N; i++)
	for (int j = 0; j < N; j++) {
		if ((i < NA) == (j < NA))
		    continue;
		if (schedule[i].first >= schedule[j].second + T)
		    matcher.next[i].push_back(j+N);
	}
	
	// How many trains needed?
	matcher.max_match();
//	printf("%d\n", matcher.match_size);
	int need[2] = {0, 0};
	for (int i = 0; i < N; i++)
	    if (matcher.match[i] == -1)
	        need[i < NA ? 0 : 1]++;
	
	// Print answer.
	printf("Case #%d: %d %d\n", iTest, need[0], need[1]);
}

int main()
{
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);

	int nTest;
	scanf("%d", &nTest);
	for (int iTest = 0; iTest < nTest; iTest++)
	    solve(iTest+1);
	return 0;
}
