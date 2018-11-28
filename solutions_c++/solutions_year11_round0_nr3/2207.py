#include <stdio.h>
#include <algorithm>

using namespace std;


int C[1010];

int main()
{
	int T;
	scanf("%d ",&T);
	for (int caseID = 1; caseID <= T; ++caseID)
	{
		int N; 
		scanf("%d ",&N);
		int sum_all = 0;
		for (int i = 0; i < N; ++i){
			scanf("%d ",&C[i]);
			sum_all ^= C[i];
		}

		if (sum_all != 0){
			printf("Case #%d: NO\n", caseID);
			continue;
		}
		int ans = 0;
		sort(C, C + N);
		for (int i = 1; i < N; ++i)
			ans += C[i];
		printf("Case #%d: %d\n", caseID, ans);
	}


	return 0;
}
