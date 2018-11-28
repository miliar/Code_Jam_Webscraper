#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

const int MAX = 30;


char val[MAX];



int main()
{
	freopen("f://B-large.in", "r", stdin);
	freopen("f://B-large.in.out", "w", stdout);
	int cnt = 0, T;
	scanf("%d", &T);
	while(T--){
		int i, j;
		cnt++;
		val[0] = '0';
		scanf("%s", val + 1);
		int len = strlen(val);
		//next_permutation(
		next_permutation(val, val + len);
		int flag = 0;
		printf("Case #%d: ",  cnt);
		for(i = 0; i < len; i++){
			if(val[i] != '0')  flag = 1;
			if(flag)  printf("%c", val[i]);
		}
		printf("\n");
	}
}