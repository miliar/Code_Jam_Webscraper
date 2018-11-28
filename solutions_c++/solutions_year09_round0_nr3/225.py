#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cfloat>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <string>

using namespace std;

char str[] = "welcome to code jam", linha[512];
int lenStr, lenLinha;

int memoization[32][512];

int resp(int ptStr, int ptLinha) {
	if (ptStr == lenStr)
		return 1;

	if (ptLinha == lenLinha)
		return 0;

	if (memoization[ptStr][ptLinha] != -1)
		return memoization[ptStr][ptLinha];

	int ret = 0;

	if (str[ptStr] == linha[ptLinha])
		ret += resp(ptStr+1, ptLinha+1);

	ret += resp(ptStr, ptLinha+1);

	return memoization[ptStr][ptLinha] = ret%10000;
}

int main(void){
	lenStr = strlen(str);
	int ds, tc = 1;
	scanf("%d ", &ds);
	while(ds--) {
		scanf(" %[^\n] ", linha);
		lenLinha = strlen(linha);
		for(int i = 0; i < lenLinha; ++i)
			for(int j = 0; j < lenStr; ++j)
				memoization[j][i] = -1;
		printf("Case #%d: %04d\n", tc++, resp(0, 0));
	}
	return 0;
}
