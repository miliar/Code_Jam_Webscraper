#include <cstdio>
#include <cstring>
#include <cmath>

bool status[11];
int N,K;

int main()
{
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	int t = 0;
	while(T--){
		scanf("%d%d",&N,&K);
		++t;
		int temp = 1<<N;
		if((K+1)%temp == 0)
			printf("Case #%d: ON\n",t);
		else
			printf("Case #%d: OFF\n",t);
	}
}