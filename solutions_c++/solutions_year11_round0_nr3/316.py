#include <cstdio>
using namespace std; 

const int maxn = 1003; 

int sum; 
int min; 

int T;
int N; 
int a[maxn]; 
int binsum; 
void input(){
	scanf("%ld", &N); 
	sum = 0;
	binsum = 0; 
	min = 2000000; 
	for (int i = 0; i < N; i++){
		scanf("%ld", &a[i]);
		sum += a[i]; 
		min = min < a[i]? min : a[i]; 
		binsum = (binsum ^ a[i]);
	}
}

void work(int cid){
	printf("Case #%ld: ", cid); 
	if (N <= 1 || binsum != 0) {
		printf("NO\n"); 
		return;
	}
	printf("%ld\n", sum - min); 
}

int main(){
	//freopen("E:\\Algorithms\\GoogleJam\\GoogleJam\\input\\C-large.in", "r", stdin); 
	//freopen("E:\\Algorithms\\GoogleJam\\GoogleJam\\input\\C-large.out", "w", stdout); 
	scanf("%ld", &T);
	for (int i = 0; i < T; i++) {
		input(); 
		work(i + 1); 
	}
	//fclose(stdout); 
}