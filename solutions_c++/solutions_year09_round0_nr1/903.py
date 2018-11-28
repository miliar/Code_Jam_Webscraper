#include <cstdio>
#include <cstring>

const int MAX_D = 5000 + 5;
const int MAX_L = 15 + 5;
const int ALPHA = 30;

int L, D, N;
char words[MAX_D][MAX_L];
char cur[MAX_L * ALPHA];
bool in[MAX_L][ALPHA];
int main()
{
	scanf("%d %d %d\n", &L, &D, &N);
	for(int i = 0; i < D; i ++)
		gets(words[i]);
	for(int t = 0; t < N; t ++)
	{
		gets(cur);
		memset(in, 0, sizeof(in));
		int pos = 0, i = 0;
		while(pos < L)
		{
			if(cur[i] == '(')
			{
				i ++;
				while( cur[i] != ')' )
					in[pos][cur[i ++] - 'a'] = 1;
				i ++;
			}
			else
				in[pos][cur[i ++] - 'a'] = 1;
			pos ++;
		}
		int res = 0;
		for(int i = 0; i < D; i ++)
		{
			int j;
			for(j = 0; j < L; j ++)
				if( in[j][words[i][j] - 'a'] == 0 )
					break;
			if(j == L)	res ++;
		}
		printf("Case #%d: %d\n", t + 1, res);
	}
    return 0;
}
