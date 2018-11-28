#include <cstdio>
#include <cstring>
#include <cmath>


const int MAXWORDS = 5001;
const int MAXWORDSLEN = 16;

char words[MAXWORDS][MAXWORDSLEN];
char visited[MAXWORDS][MAXWORDSLEN];


int process(char * str, int L, int D)
{
	memset(visited, 0, sizeof(visited));

	int len = strlen(str);
	int i, j, k;
	int res, found;
	int par = 0;
	int ind = 0;

	for(i=0; i<len; i++)
	{
		if(str[i] == '(')
		{
			par = 1;
		}

		else if(str[i] == ')')
		{
			ind++;
			par = 0;
		}

		else
		{
			for(j=0; j<D; j++)
			{
				if(words[j][ind] == str[i])
				{
					visited[j][ind] = 1;
				}
			}

			if(par == 0)
			{
				ind++;
			}
		}
	}

	res = 0;

	for(i=0; i<D; i++)
	{
		found = 1;

		for(j=0; j<L; j++)
		{
			if(visited[i][j] == 0)
			{
				found = 0;
				break;
			}
		}

		if(found == 1)
		{
			res++;
		}
	}

	return res;
}



int main(void)
{	
	//freopen("c:\\IO\\A-large.in", "rt", stdin);
	//freopen("c:\\IO\\A-large.out", "wt", stdout);
	
	int i;
	int L, D, N;
	char str[5000];

	scanf( " %d %d %d " ,&L, &D, &N);

	for(i=0; i<D; i++)
	{
		scanf(" %s" ,words[i]);
	}

	for(i=0; i<N; i++)
	{
		scanf(" %s" ,str);

		printf("Case #%d: %d\n" ,i+1 ,process(str, L, D));

	}


	return 0;
}


