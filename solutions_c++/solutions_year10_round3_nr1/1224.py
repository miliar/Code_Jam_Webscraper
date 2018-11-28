#include <iostream>
using namespace std;

#define M 1200
int main()
{
 int T, N, point[M+1][2];

 scanf("%d", &T);

 for(int t = 1, cnt; t<= T; ++t)
 {
 	scanf("%d", &N);
	
	cnt = 0;	

	for(int i = 0; i < N; ++i) {
		scanf("%d %d",&point[i][0], &point[i][1]);	
		
		for(int j = 0; j < i; ++j)
		{
			if ((point[i][0] < point[j][0]) && (point[i][1] > point[j][1]))
				++cnt;
			if ((point[i][0] > point[j][0]) && (point[i][1] < point[j][1]))						++cnt;
		}
	}

	printf("Case #%d: %d\n", t, cnt);		
 }
return 0;
}
