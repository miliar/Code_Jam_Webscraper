#include <cstdio>
#include <cstring>
#include <cstdlib>

const int MAXN = 500 ;
 
char words[MAXN + 10];
const char * p = "welcome to code jam";

int num[MAXN + 10][MAXN + 10];
bool mark[MAXN + 10][MAXN + 10];

int 
Search(int a, int b)
{	
	if(a > b)
		return 0;
		
	if(a == -1)
		return 1;
		
	if(mark[a][b])
		return num[a][b];

	int res = 0;
	for(int i = b; i >= 0; i--)
		if(words[i] == p[a])
			res += Search(a - 1, i - 1);
			
	num[a][b] = res;
	mark[a][b] = true;
	
	return res;
}

int main()
{
	int n, caseNum = 0;
	
	freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
	scanf("%d", &n);
	getchar();
	
	for(int i = 0; i < n; i++)
	{
		scanf("%[^\n]", words);
		getchar();
		
		memset(num, 0, sizeof(num));
		memset(mark, false, sizeof(mark));
		
		int res = Search(strlen(p) - 1, strlen(words) - 1);
		printf("Case #%d: %0.4d\n", ++caseNum, res);
	}

	return 0;
}
