#include <cstdio>
#include <cstring>
#include <cmath>
#include <climits>

int T, mcase = 1;

int main()
{
	//freopen("in.txt", "r", stdin);
	freopen("C-large.in", "r", stdin);
 	freopen("C-large.out", "w", stdout);

	int total, t;
	int count;
	int small, temp;

	scanf("%d", &T);
	while(mcase <= T){
		scanf("%d", &count);
		small = INT_MAX;
		total = t = 0;
		for(int i=0; i<count; i++){
			scanf("%d", &temp);
			if(small > temp)
				small = temp;
			total = total + temp;
			t = t ^ temp;
		}

		printf("Case #%d: ", mcase);
		if(t == 0)
			printf("%d\n", total - small);
		else
			printf("NO\n");
		
		mcase ++;
	}
}