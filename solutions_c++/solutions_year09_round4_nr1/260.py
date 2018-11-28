#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define fr(i, N) for(i = 0; i < (int)N; i++)
#define setContains(i,j) (((1<<j)&i) != 0)
#define MP make_pair
#define F first
#define S second
#define pb push_back
#define Eps 1e-11

typedef pair<int, int> pi;

int N;
int Map[50];

void input()
{
	int i, j;
	char a;
	scanf("%d", &N);

	fr (i, N) {
		int best = -1;
		
		fr (j, N) {
			scanf("%c", &a);

			if (a == '0') {
				continue;
			} else if (a == '1') {
				best = j;
			} else {
				j--;
			}
		}

		Map[i] = best;
	}
}

void process()
{
	int i, j, res = 0;

	fr (i, N) if (Map[i] > i) {
		for (j = i+1; j < N; j++) if (Map[j] <= i) break;

		for (; j > i; j--) {
			swap(Map[j], Map[j-1]);
			res++;
		}
	}

	printf("%d\n", res);
}

int main()
{
	int t, T;
	scanf("%d", &T);

	fr(t, T)
	{
		input();
		printf("Case #%d: ", t+1);
		process();
	}
	return 0;
}

