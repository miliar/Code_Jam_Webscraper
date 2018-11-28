#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string.h>
using namespace std;

bool check(int A, int B) {
	if(A<B) swap(A, B);
	vector<int> dt;
	while(B) {
		dt.push_back(A/B);
		A%=B;
		swap(A, B);
	}
	bool win=true;
	for(int i=dt.size()-1;i>=0;i--)
		win=(!win || dt[i]>1);
	return win;
}

int solve() {
	int A1, A2, B1, B2;
	scanf("%d%d%d%d", &A1, &A2, &B1, &B2);
	int cnt=0;
	for(int i=A1;i<=A2;i++)
		for(int j=B1;j<=B2;j++)
			cnt+=check(i, j);
	return cnt;
}

int main() {
	check(1000000, 1000000);
	int t;
	scanf("%d", &t);
	for(int i=1;i<=t;i++)
		printf("Case #%d: %d\n", i, solve());
}