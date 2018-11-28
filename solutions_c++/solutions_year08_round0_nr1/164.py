#include <cstdio>
#include <string>
#include <vector>

using namespace std;

void solve(int iTest)
{
	// Read search engine names and put their name in vector engine.
	int S;
	scanf("%d\n", &S);
	vector<string> engine(S);
	for (int i = 0; i < S; i++) {
		static char line[1024];
		gets(line);
		engine[i] = line;
	}

	// Read each query and process it.
	vector<int> best(S, 0);
	int Q;
	scanf("%d\n", &Q);
	for (int i = 0; i < Q; i++) {
		static char query[1024];
		gets(query);

		int index = find(engine.begin(), engine.end(), string(query)) - engine.begin();
		if (index == S)
		    continue; // Query is not name of any engine -- skip it
		for (int j = 0; j < S; j++)
		    best[j] = min(best[j], best[index]+1);
		best[index] = 1000000000;
	}
	
	// Print answer.
	printf("Case #%d: %d\n", iTest, *min_element(best.begin(), best.end()));
}

int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int nTest;
	scanf("%d", &nTest);
	for (int iTest = 0; iTest < nTest; iTest++)
	    solve(iTest+1);
	return 0;
}
