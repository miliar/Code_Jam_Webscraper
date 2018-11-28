#include <iostream>
#include <string.h>
#include <string>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
int num[1000];
int main(){
	int t,n,l,h;
	freopen("C-small-attempt2.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&t);
	int i,j,k;
	bool flag;
	for (i = 1;i <= t;i++){
		flag = true;
		scanf("%d%d%d",&n,&l,&h);
		for (j = 0;j < n;j++){
			scanf("%d",&num[j]);
		}
		for (j = l;j <= h;j++){
			flag = true;
			for (k = 0;k < n;k++){
				if ((num[k]%j == 0) || (j%num[k] == 0))
					continue;
				else{
					flag = false;
					break;
				}
			}
			if (flag)
				break;
		}
		printf("Case #%d: ",i);
		if (flag){
			printf("%d\n",j);
		}
		else
			printf("NO\n");
	}
	return 0;
}