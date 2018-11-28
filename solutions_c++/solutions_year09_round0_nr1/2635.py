#include <cstdio>
#include <cstring>
#include <cstdlib>

const int LEN = 15;
const int MAXN = 5000;

char word[MAXN + 10][LEN + 10];
char dst[MAXN];
bool mark[LEN + 10][26];

int main()
{
    int l, d, n;
    int caseNum = 0;
    
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    scanf("%d%d%d", &l, &d, &n);
    for(int i = 0; i < d; i++)
    	scanf("%s", word[i]);
    	
    for(int i = 0; i < n; i++)
    {
		scanf("%s", dst);
		
		memset(mark, false, sizeof(mark));
		
		int len = strlen(dst);
		int pos = -1;
		int num = 0;
		
		for(int j = 0; j < len; j++)
		{
			if(num == 0)
				pos++;
				
			if(dst[j] == '(')
				num++;
			else if(dst[j] == ')')
				num--;
			else
				mark[pos][dst[j] - 'a'] = true;
		}
		/*
		for(int j = 0; j < l; j++)
		{
			for(int k = 0; k < 26; k++)
				if(mark[j][k])
					printf("1");
				else
					printf("0");
			printf("\n");
		}
		*/
		
		int res = 0;
		for(int i = 0; i < d; i++)
		{
			int j;
			for(j = 0; j < l; j++)
				if(!mark[j][word[i][j] - 'a'])
					break;
			if(j == l)
				res++;
		}
		printf("Case #%d: %d\n", ++caseNum, res);
	}
	
	return 0;
}
