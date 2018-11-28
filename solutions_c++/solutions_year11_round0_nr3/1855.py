#include <cstdio>
#include <vector>

using namespace std;

void solve(int tc){
	int n;
	scanf("%d", &n);
	vector<int> c;
	int sum = 0;
	int psum = 0;
	int min = 10000000;
	while(n--){
		int ci;
		scanf("%d", &ci);
		if(ci < min) min = ci;
		sum += ci;
		psum ^= ci;
	}
	printf("Case #%d: ", tc);
	if(psum){
		printf("NO\n");
	}else{
		printf("%d\n", sum - min);
	}
}

int main(){
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; i++){
		solve(i+1);
	}
	return 0;
}
