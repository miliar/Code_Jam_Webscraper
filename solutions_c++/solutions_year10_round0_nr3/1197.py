#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <iostream>
using namespace std;

int main()
{
	int T;
// 	freopen("C.in","r",stdin);
// 	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for (int iCase=1; iCase<=T; ++iCase)
	{
		int N,K,R;
		int i,j,k;
		int cycle = 0;
		scanf("%d%d%d",&R,&K,&N);
		vector<int> g;
		int gi;
		for (k=0; k<N; ++k)
		{
			cin>>gi;
			g.push_back(gi);
		}
		__int64 sum = 0;
		__int64 result;
		for (i=0; i<N; ++i)
		{
			sum += g[i];
			if (sum > K)
				break;
		}
		if (i==N){
			result = R*sum;
			goto end;
		}
		int next[1000];
		__int64 p_sum[1000];
		int start;
		memset(next,-1,sizeof(next));
		i = 0;
		int nloops = 0;
		while (1){
			if (next[i] != -1){
				start = i;
				break;
			}
			++nloops;
			sum = 0;
			for (j=i; j<N; j++)
			{
				sum += g[j];
				if (sum>K) break;
			}
			if (j==N)
			{
				for (j=0; j<N; ++j){
					sum += g[j];
					if (sum > K)
						break;
				}
			}
			p_sum[i] = sum - g[j];

			next[i] = j;
			i = j;
		}
		result = 0;
		i = 0;
		//A1
		for (j=0; j<R; ++j){
			if (i==start) break;
			result += p_sum[i];
			i = next[i];
		}
		//A2
		R -= j;
		if (R<=0) goto end;
		sum = 0;
		for (i=start;;){
			sum += p_sum[i];
			++cycle;
			i = next[i];
			if (i==start)break;
		}
		result += sum*(R/cycle);
		R %= cycle;
		//A3
		i = start;
		while(R--){
			result += p_sum[i];
			i = next[i];
		}
end:
		printf("Case #%d: %I64d\n",iCase,result);

	}	
}
