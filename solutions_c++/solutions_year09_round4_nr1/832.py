#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>

using namespace std;

int n;
char a[100][100];
int s[100];

int main()
{

	freopen("test.in" , "r" , stdin);
	freopen("test.out" , "w" , stdout);
	int t;
	int cas = 1;
	scanf("%d" , &t);
	while (t --){

		scanf("%d" , &n);
		int i , j;
		memset(s , 0 , sizeof(s));
		for (i = 0 ; i < n ; i ++){
			scanf("%s" , a[i]);
		}
		for (i = 0 ; i < n ; i ++){

			for (j = n - 1 ; j >= 0 ; j --){
				
				if ( a[i][j] == '1' ){
					s[i] = j;
					break;
				}

			}

		}

		int ret = 0;
		int tp = 0;
		int tmp;
		for(i = 0; i < n; i++) 
		{
			if(s[i] > i) 
			{
				for(j = i + 1; j < n; j++) {
					if(s[j] <= i) {
						tmp = j;
						break;
					}
				}
				for(j = tmp; j > i; j--) {
					swap(s[j], s[j - 1]);
					ret ++;
				}			
			}
		}

		printf("Case #%d: %d\n" , cas , ret);
		cas ++;

	}

}