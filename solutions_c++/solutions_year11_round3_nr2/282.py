#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

long long L, N, C;
long long t;
long long a[1100];
long long d[1100000];
long long Booster[1100000];
long long traveT[1100000];
long long Array[1100000], nCount;

void Read()
{
	memset(a, 0 ,sizeof(a));
	memset(d, 0 ,sizeof(d));
	memset(Booster, 0 ,sizeof(Booster));
	memset(traveT, 0 ,sizeof(traveT));
	scanf("%lld %lld %lld %lld", &L, &t, &N, &C);
	for(int i = 0; i < C; i++)
		scanf("%d", &a[i]);
	for(int i = 0, j = 0; i < N; i++){
		d[i] = a[j];
		j = (j+1) % C;
	}
}

long long GetResult(int b0, int b1)
{
	long long nTime = 0;
	for(int i = 0; i < N; i++){
		if(i == b0 || i == b1){
			if(nTime >= t)
				nTime += d[i];
			else if(nTime+d[i] <= t)
				nTime += d[i]*2;
			else{//?
				long long dTime = t - nTime;
				if(dTime%2) printf("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n");
				nTime = t+(d[i]-dTime/2);
			}
		}else{
			nTime += d[i]*2;
		}
	}
	return nTime;
}

void Solve2()
{
	long long nResult = 10000000000;
	for(int i = 0; i < N; i++)
		for(int j = i+1; j < N; j++){
			int nTemp = GetResult(i, j);
			if(nResult > nTemp)
				nResult = nTemp;
		}
	printf("%lld\n", nResult);
}

void Solve1()
{
	long long nResult = 10000000000;
	for(int i = 0; i < N; i++){
		int nTemp = GetResult(i, -1);
		if(nResult > nTemp)
			nResult = nTemp;
	}
	printf("%lld\n", nResult);
}

void Solve0()
{
	long long nResult = 10000000000;
	nResult = GetResult(-1, -1);
	printf("%lld\n", nResult);
}

void Solve()
{
	long long nResult = 0;
	nCount = 0;
	long long nCurTime = 0;
	for(int i = 0; i < N; i++){
		if(nCurTime+d[i]*2> t){
			if(nCurTime > t)
				Array[nCount++]	= d[i];
			else{
				if((t-nCurTime)%2) printf("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
				nResult += t-nCurTime;
				Array[nCount++]	= d[i]-(t-nCurTime)/2;
			}
		}else{
			nResult += d[i]*2;
		}
		nCurTime += d[i]*2;
	}
	sort(Array, Array+nCount);
	for(int i = 0; i < nCount; i++){
		if(i < L)
			nResult += Array[nCount-1-i];
		else
			nResult += 2*Array[nCount-1-i];
	}
	printf("%lld\n", nResult);
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		Read();
		printf("Case #%d: ", i);
		Solve();
	}
}
