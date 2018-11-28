#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>
#include <stack>
#include <cstring>

using namespace std;

typedef long long ll;

int dp[510][20];
int n;
char str[1010];
char tmp[30] = "welcome to code jam";

vector < int > v[300];
void init()
{

	int i , len;
	len = strlen(tmp);
	for (i = 0 ; i < len ; i ++)
		v[tmp[i]].push_back(i);

}

int main()
{



	init();
	//freopen("test.in" , "r" , stdin);
	//freopen("test.out" , "w" , stdout);
	while (scanf("%d" ,  &n) == 1){

		getchar();
		for (int i = 0 ; i < n ; i ++){

			gets(str);

			int len = strlen(str);
			memset(dp , 0 , sizeof(dp));
			dp[0][0] = 1;
			for (int j = 1 ; j <= len ; j ++){

				int sz = v[str[j - 1]].size();
				for (int k = 0 ; k < j ; k ++){

					for (int s = 0 ; s < sz ; s ++){
						int tp = v[str[j - 1]][s];
						dp[j][ tp + 1 ] += dp[k][ tp ];
						dp[j][ tp + 1  ] %= 10000;
					}

				}

			}
			
			int ans = 0;
			for (int j = 1 ; j <= len ; j ++){
				ans += dp[j][19];
				ans %= 10000;
			}

			printf("Case #%d: %04d\n" , i + 1 , ans);


		}
		
	}
	return 0;
}


/*
3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc
*/