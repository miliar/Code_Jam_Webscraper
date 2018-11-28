// acm.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <cassert>
#include <algorithm>
using namespace std;


long long len[1000010];
int _tmain(int argc, _TCHAR* argv[])
{
	freopen("t.in", "r", stdin);
	freopen("t.out", "w", stdout);

	int cas;
	scanf("%d", &cas);
	for(int cas_i=1;cas_i<=cas;cas_i++)
	{
		printf("Case #%d:", cas_i);
		
		long long  L,t,N,C;		
		scanf("%lld %lld %lld %lld", &L, &t, &N, &C);

		for(int i = 0;i<C;i++){
			scanf("%lld", &len[i]);
			len[i] *= 2;
		}
		for(int i=C; i<N; i++){
			len[i] = len[i - C];
		}


			long long til = 0;
			int idx;
			for( idx=0;idx<N;idx++){
				long long next_t = til + len[idx];
				if(t< next_t){
					til = t;
					len[idx] = next_t - t;
					break;
				}else{
					til += len[idx];
				}
			}
			sort(len + idx, len+N);
			for(int ii=1;ii<=L;ii++){
				len[N-ii] /= 2;
			}
			for(int i=idx;i<N;i++){
				til += len[i];
			}

		

		printf(" %lld\n", til);

	}
	return 0;
}

