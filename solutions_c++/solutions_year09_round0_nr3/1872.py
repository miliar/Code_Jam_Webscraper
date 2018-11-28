#include <iostream>
using namespace std;
//welcome to code jam

#define Max(a , b) (a > b ? a : b)

char word[100] = {"welcome to code jam"};
char s[1010];
int ans[2][1010];

void Print(int x)
{
	int len , temp = x;
	len = 0;
	while(temp){
		
		len++;
		temp /= 10;
	}

	for (int i=3 ; i>=len ; i--)
		printf("0");
	if (x != 0)
		printf("%d" , x);
}

int main()
{
	freopen("C-large.in" , "r" , stdin);
	freopen("C-large.out" , "w" , stdout);
	int T;
	int len , wordLen;
	int p , u , cas = 0;
	scanf("%d" , &T);
	getchar();
	while (T--){

		cas++;
		gets(s);
		len = strlen(s);

		memset(ans , 0 , sizeof(ans));

		for (int i=0 ; i<len ; i++){

			ans[0][i] = 1;
		}

		p = 0;
		u = 1;
		
		wordLen = strlen(word);
		for (int i=0 ; i<wordLen ; i++){

			if (word[i] == ' '){

				i += 0;
			}
			for (int j=i ; j<len ; j++){

				if (j == 0){

					if (s[j] == word[i])
						ans[u][j] = 1;
					else
						ans[u][j] = 0;
				}
				else{

					if (s[j] == word[i])
						ans[u][j] = ans[u][j - 1] + ans[p][j - 1];
					else
						ans[u][j] = ans[u][j - 1];
				}
				if (ans[u][j] >= 10000)
					ans[u][j] %= 10000;
			}
			p = 1 - p;
			u = 1 - u;

			for (int j=0 ; j<len ; j++)
				ans[u][j] = 0;
		}

		printf("Case #%d: " , cas);
		Print(ans[p][len - 1]);
		printf("\n");
	}
	return 0;
}