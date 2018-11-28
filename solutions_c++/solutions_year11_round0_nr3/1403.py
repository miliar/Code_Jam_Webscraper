#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#define PB push_back
using namespace std;

const int INF = 1000000100;

int numTests, minValue, sumValue, xorValue, candies, value;

int main(){
	scanf("%d",&numTests);
	for(int test=1; test<=numTests; test++){
		scanf("%d",&candies);
		minValue = INF;
		sumValue = 0;
		xorValue = 0;
		for(int i=1; i<=candies; i++){
			scanf("%d",&value);
			minValue = min(value, minValue);
			sumValue += value;
			xorValue ^= value;
		}
		if(xorValue != 0)
			printf("Case #%d: NO\n",test);
		else
			printf("Case #%d: %d\n",test,sumValue - minValue);
	}
}