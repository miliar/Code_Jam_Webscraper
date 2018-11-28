#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int N, N2=0;
	scanf("%d\n",&N);
	while (N--) {
		int P, K, L;
		scanf("%d %d %d\n",&P,&K,&L);
		int letters[L];
		vector<int> let;
		for (int i=0; i<L; i++) {
		       scanf("%d ",letters+i);
		       let.push_back(letters[i]);
		}
		sort(let.begin(),let.end(),greater<int>());

		long long int ans = 0;
		int ps = 1;
		int c = 0;
		for (int i=0; i<L; i++) {
			ans += let[i]*ps;
			c++;
			if (c==K) {
				ps++;
				c = 0;
			}
		}




		// print result
		printf("Case #%d: ",++N2);
		cout << ans << endl;
	}
	return 0;
}

