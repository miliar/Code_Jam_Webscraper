#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

void solve();
void runCase();

void runCase()
{
	int n;
	
	int sum = 0,esum = 0,minc = -1;
	scanf("%d",&n);
	for(int i = 0; i < n; i++) {
		int c;
		scanf("%d",&c);
		sum += c;
		esum ^= c;
		if(minc == -1 || minc > c) {
			minc = c;
		}
	}
	
	if(esum == 0) {
		printf("%d\n",sum-minc);
	}
	else {
		printf("NO\n");
	}
}

void solve()
{
	int n;
	scanf("%d",&n);
	getchar();
	
	for(int i = 0; i < n; i++) {
		printf("Case #%d: ",i+1);
		runCase();
	}
}

int main()
{
	solve();
	return 0;
}
