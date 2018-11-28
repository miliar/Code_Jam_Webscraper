#include <iostream>

using namespace std; 

int main() {
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);

	int T,C = 1;
	scanf("%d", &T);
	for(int i = 0; i< T; ++i)
	{
		int n,k;
		cin >> n >> k;
		k = k % (1<<n);
		n = (1<<n) - 1;
		printf("Case #%d: ", C++);
		if(n == k) printf("ON\n");
		else printf("OFF\n");
	}

	return 0;
}