/* by Ashar Fuadi [fushar] */

#include <cstdio>
#include <cstring>

#include <vector>
#include <string>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0; i < (int)n; i++)
#define FOR(i, a, b) for (int i = (int)a; i <= (int)b; i++)
#define FOREACH(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)
#define RESET(c,v) memset(c, v, sizeof(c))

typedef long long ll;

#define pb push_back
#define mp make_pair

int T;
char S[105];
const char* key = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	scanf("%d\n", &T);
	REP(tc, T)
	{
		gets(S);
		printf("Case #%d: ", tc+1);
		int N = strlen(S);
		REP(i, N)
		{
			if (S[i] == ' ')
				printf(" ");
			else
				printf("%c", key[S[i]-'a']);
		}
		printf("\n");
	}
}
