#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <math.h>

using namespace std;


int main()
{
	int line;
	cin >> line;
	
	int K, N;

	for (int i=0; i<line; i++){
		cin>>N>>K;
		
		if ((K+1)%((int)pow(2, N)))
			printf("Case #%d: OFF\n", i + 1);
		else
			printf("Case #%d: ON\n", i + 1);
	}
	
	return 0;
}