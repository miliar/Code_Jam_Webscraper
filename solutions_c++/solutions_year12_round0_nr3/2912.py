#include<cstdio>
#include<cstring>

int multi;

bool flag[2000001];

int ret = 0;

int A, B;

void make(int x){
	if(flag[x]) return;

	int a = 0;
	while(!flag[x]){
		if(x >= A && x <= B){
			a++;
		}
		int y = x % 10;
		flag[x] = true;
		x = y * multi + x / 10;
	}
	ret += a * (a - 1) / 2;
}

int main(){
//	freopen("in.txt" , "r" , stdin);
//	freopen("out.txt" , "w" , stdout);
	int t;
	scanf("%d" , &t);
	for(int ii = 1;ii <= t;ii++){
		scanf("%d%d" , &A, &B);
		if(A < 10) multi = 1;
		else if(A < 100) multi = 10;
		else if(A < 1000) multi = 100;
		else if(A < 10000) multi = 1000;
		else if(A < 100000) multi = 10000;
		else if(A < 1000000) multi = 100000;
		memset(flag, false, sizeof(flag));
		ret = 0;
		for(int i = A;i <= B;i++){
			make(i);
		}
		printf("Case #%d: %d\n" , ii, ret);
	}
	return 0;
}