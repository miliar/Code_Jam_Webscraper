#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;

int m[105];
int n;

bool game(int num){
	int i;
	for (i = 0;i < n;i++){
		if ((m[i] % num) && (num % m[i])){
			break;
		}
	}
	if (i == n)
		return true;
	return false;
}

int main(){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int test, t, i, l, r;
	scanf("%d\n",&test);
	for (t = 0;t < test;t++){
		if (t)
			printf("\n");
		printf("Case #%d: ",t + 1);
		scanf("%d%d%d",&n,&l,&r);
		for (i = 0;i < n;i++){
			scanf("%d",&m[i]);
		}
		for (i = l;i < r + 1;i++){
			if (game(i)){
				printf("%d",i);
				break;
			}
		}
		if (i == r + 1)
			printf("NO");
	}
	return 0;
}