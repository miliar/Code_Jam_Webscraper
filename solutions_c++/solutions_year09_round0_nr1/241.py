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

int L, D;
char Dic[6000][20];
char word[1000];
int Pos[6000];

void input()
{
	scanf(" %s", word);
}

void process()
{
	int i, j, move = 0;
	fr (i, D) Pos[i] = 1;

	fr (i, L) {
		set<char> list;
		if (word[move] == '(') {
			move++;
			while (word[move] != ')') {
				list.insert(word[move++]);
			}
		} else {
			list.insert(word[move]);
		}

		move++;

		fr (j, D) {
			if (list.find(Dic[j][i]) == list.end()) Pos[j] = 0;	
		}
	}

	int res = 0;
	fr (i, D) if (Pos[i] == 1) res++;

	printf("%d\n", res);
}

int main()
{
	int t, T;
	scanf("%d%d%d", &L, &D, &T);
	fr (t, D) scanf(" %s", Dic[t]);

	fr(t, T)
	{
		input();
		printf("Case #%d: ", t+1);
		process();
	}
	return 0;
}

