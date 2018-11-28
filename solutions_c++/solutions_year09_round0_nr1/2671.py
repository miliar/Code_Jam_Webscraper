#include <iostream>
#include <algorithm>
using namespace std;

int token[20][2];
char dict[5010][20];
char word[500];

void parse(char word[500])
{
	int len = strlen(word);

	int i = 0, ti = 0, pn = 0;
	while (i < len)
	{
		if(word[i] == '(') {
			++ pn;
			token[ti][0] = i+1;

		}else if(word[i] == ')') {
			-- pn;
			token[ti++][1] = i-1;

		}else{
			if(pn == 0){
				token[ti][0] = i;
				token[ti++][1] = i;
			}
		}

		//
		++ i;
	}
}

int main()
{
	freopen("A-large.in.txt", "r", stdin);
	freopen("A-large.out.txt", "w", stdout);

	int L, D, N;
	int X, K, i, j, r;

	scanf("%d %d %d", &L, &D, &N);

	for(i=0; i<D; ++i)
	{
		scanf("%s", dict[i]);
	}
	
	X = 0;
	while( N-- )
	{
		scanf("%s", word);

		parse(word);

		K = 0;
		for(i=0; i<D; ++i) {
			for(j=0; j<L; ++j){
				for(r = token[j][0]; r<=token[j][1] && word[r]!=dict[i][j]; ++r);

				if(r>token[j][1]) break;
			}

			if(j>=L) ++ K;
		}

		//
		printf("Case #%d: %d\n", ++X, K);

	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
