#include<cstdio>

using namespace std;


int main()
{
//	freopen("b.txt","r",stdin);
//	freopen("b.out","w",stdout);
	int T;
	scanf("%d\n", &T);
	for(int i = 1;i <= T; i++)
	{
		int N, S, P;
		int count0 = 0;
		int count1 = 0;
		int count2 = 0;
		scanf("%d %d %d ", &N, &S, &P);
		int test1 = 3*P - 2;
		int test2 = 3*P - 4;
/*		if(P == 1)
		{
			test1 = 1;
			test2 = 0;
		}
		if(P == 0)
		{
			test1 = test2 = 0;
		}
*/
		if(P == 0){
			count0 = N;
		}
		for(int j = 0;j < N;j++)
		{
			int d;
			scanf("%d", &d);
			if(P == 1){
				if(d >= 1)count0++;
			}
			if(P >= 2){
				if(d >= test1) count0++;
				else if(d >= test2) 
				{
					count1++;
				}
				else count2++;
			}
		}
		int output = count0;
		if(count1 > S)output += S;
		else output += count1;
		printf("Case #%d: %d\n", i, output);
	}
	return 0;
}
