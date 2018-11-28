#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#include <complex>


//#define DEBUG


using namespace std;



int main(int argc, char** argv)
{
	//freopen("test.in", "r", stdin );
	//freopen("test.out", "w", stdout );
	//freopen("A-small-attempt1.in", "r", stdin );
	//freopen("A-small-attempt1.out", "w", stdout );
	freopen("A-large.in", "r", stdin );
	freopen("A-large.out", "w", stdout );

	int T;
	string line;

	cin >> T;
	for( int iT=0; iT < T; iT++){
		int N;
		unsigned long long K;

		cin >> N >> K;
#ifdef DEBUG
		printf("iT:%d: N:%d K:%d\n", iT,N,K);
#endif//DEBUG
		
		unsigned long long completeBase = 1 << N;
		unsigned long long completeBase2 = completeBase - 1;
		unsigned long long multi = K / completeBase;
		unsigned long long remainder = K % completeBase;


#ifdef DEBUG
		printf("cb:%lld multi:%lld multi-2:%lld cb2:%lld remainder:%lld \n", completeBase, multi, multi %2, completeBase2, remainder);
#endif//DEBUG

		if( remainder ==  completeBase2 ){
			printf("Case #%d: ON\n", iT+1);
		}else{
			printf("Case #%d: OFF\n", iT+1);
		}

#ifdef DEBUG
		printf("\n\n");
#endif//DEBUG
	}


}