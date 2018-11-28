#include <iostream>
#include <algorithm>

using namespace std;

int main(void)
{
	int t;
	cin >> t;
	for(int num=1;num<=t;num++) {
		double ans = 0;
		int n;
		int array[1001];
		cin >> n;
		for(int i=1;i<=n;i++) {
			cin >> array[i];
		}
		
		int sum = 0;
		for(int i=1;i<=n;i++) {
			if(array[i]==i) sum++;
		}
		ans = n-sum;
		
		printf("Case #%d: %.6f\n", num, ans);
	}
}
