#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

#define MOD 10009

using namespace std;

int letcount[32];
static char poly[256];
int K, dsize;
vector <string> dict;
int ret[64];

int evalpoly(char poly[256])
{
	int s = strlen(poly);
	int ret = 0;
	int tempret = 1;

	for (int i = 0; i <= s; i++) {
		if ('a' <= poly[i] && poly[i] <= 'z')
			tempret = (tempret * letcount[poly[i]-'a']) % MOD;
		else {
			ret = (ret+tempret) % MOD;
			tempret = 1;
		}
	}

	return ret;
}

void count_word(string s)
{
	for (int i = 0; i < s.length(); i++)
		letcount[s[i]-'a'] ++;
}
void uncount_word(string s)
{
	for (int i = 0; i < s.length(); i++)
		letcount[s[i]-'a'] --;
}

void go(int i, int nword)
{
	ret[nword] = (ret[nword]+evalpoly(poly))%MOD;

	if (nword >= K)
		return;

	for (int j = 0; j < dsize; j++) {
		count_word(dict[j]);

		go(j, nword+1);

		uncount_word(dict[j]);
	}
}

int main(int argc, char ** argv)
{
	int ntest;

	scanf("%d", &ntest);

	for (int t = 0; t < ntest; t++) {
		fprintf(stderr, "%d\n", t);

		memset(letcount, 0, sizeof(letcount));
		dict.clear();

		scanf(" %s %d %d", poly, &K, &dsize);

		for (int j = 0; j < dsize; j++) {
			char temp[128];
			
			scanf(" %s", temp);

			dict.push_back(string(temp));
		}

		memset(ret, 0, sizeof(ret));
		go(0, 0);
		
		printf("Case #%d:", t+1);
		for (int i = 1; i <= K; i++)
			printf(" %d", ret[i]);
		printf("\n");
	}

	return 0;
}
