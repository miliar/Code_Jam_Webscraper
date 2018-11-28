#include<iostream>

using namespace std;

int cas, cas_n;
#define N 1024
int n, sum, max_sum;
int p[N];
int x[N];

void search(int lev)
{
	if(lev >= n){
		int s1 = 0,s2 = 0;
		int r1 = 0,r2 = 0;
		for(int i=0;i<n; i++){
			if(x[i] == 0){
				s1 ^= p[i];
				r1 += p[i];
			}else{
				s2 ^= p[i];
				r2 += p[i];
			}
		}
		if(s1 == s2 && (r1 != max_sum) && (r2 != max_sum)){
			
			if(r1 > sum){
				sum = r1;
			}
			if(r2 > sum){
				sum = r2;
			}
		}
		return;
	}
	x[lev] = 1;
	search(lev+1);
	x[lev] = 0;
	search(lev+1);
}

int main(int argc, char *argv[])
{
	freopen("t.in", "r", stdin);
	freopen("t.out", "w", stdout);
	scanf("%d\n", &cas);





	for(int cas_n=1; cas_n<=cas; cas_n++)
	{
		scanf("%d\n", &n);
		sum = 0;
		max_sum = 0;
		for(int i=0;i<n;i++){
			scanf("%d", &p[i]);
			sum = sum ^ p[i];
			max_sum += p[i];
		}
		if (sum!= 0)
			printf("Case #%d: NO\n", cas_n);
		else{
			x[0] = 1;
			search(1);
			printf("Case #%d: %d\n", cas_n, sum);
		}
	}

	return 0;
}
