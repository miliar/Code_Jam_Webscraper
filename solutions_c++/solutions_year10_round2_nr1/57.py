#include <algorithm> 
#include <bitset> 
#include <cassert>
#include <cmath> 
#include <complex>
#include <cstdio> 
#include <cstdlib> 
#include <cstring>
#include <ctime> 
#include <deque> 
#include <functional> 
#include <iomanip> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <utility> 
#include <valarray>
#include <vector> 
using namespace std; 

#define ALL(x) (x).begin(), (x).end()
#define MP make_pair
#define SZ(x) ((int) (x).size())
#define max2(x,y) ((x) = max((x),(y)))
#define min2(x,y) ((x) = min((x),(y)))
typedef long long LL;

struct Directory
{
	map<string,int> children;
};

int dcnt;
Directory dirs[102000];

int alloc()
{
	dirs[dcnt].children.clear();
	return dcnt++;
}

vector<string> tokenize(char *buf)
{
	char *token = strtok(buf, "/");
	vector<string> tokens;
	do {
		tokens.push_back(token);
	} while ((token = strtok(NULL, "/")) != NULL);
	return tokens;
}

void create_dirs(const vector<string> path)
{
	int cur_dir = 0;
	for (int i = 0; i < SZ(path); ++i) {
		if (dirs[cur_dir].children.count(path[i]) == 0)
			dirs[cur_dir].children[path[i]] = alloc();
		cur_dir = dirs[cur_dir].children[path[i]];
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int TC = 1; TC <= T; ++TC) {
		int N, M;
		char buf[128];
		dcnt = 0;
		alloc();

		scanf("%d %d", &N, &M);
		for (int i = 0; i < N; ++i) {
			scanf("%s", buf);
			create_dirs(tokenize(buf));
		}

		int s = dcnt;
		for (int i = 0; i < M; ++i) {
			scanf("%s", buf);
			create_dirs(tokenize(buf));
		}

		printf("Case #%d: %d\n", TC, dcnt - s);
	}
	return 0;
}
