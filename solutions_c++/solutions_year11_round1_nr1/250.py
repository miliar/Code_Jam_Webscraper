#include<cstdio>
#include<iostream>
using namespace std;

void work(int x)
{
	long long n, pg, pd;
	printf("Case #%d: ",x);
	cin >> n >> pd >> pg;
	int wind;
	if(pd == 0)wind= 0;
	else {
		for(int i = 1; i<=100; i++){
			if(i*100%pd == 0){
				wind = i;
				break;
			}
		}
	}
	if(pd != 0 && wind*100/pd > n){
		printf("Broken\n");
		return;
	}
	if(pg == 100 && pd != 100){
		printf("Broken\n");
		return;
	}
	if(pg == 0 && pd != 0){
				printf("Broken\n");
		return;

	}
	printf("Possible\n");
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i = 1; i <= t; i++)work(i);
}
