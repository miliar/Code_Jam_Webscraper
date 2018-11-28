#include <cstdio>
#include <algorithm>
#include <iostream>

using namespace std;

int main()
{
	int runs;
	scanf("%d", &runs);
	//cout << runs << endl;
	for(int r=1; r<=runs; r++){
		int n;
		scanf("%d",&n);
		int s = 0;
		for(int i=0; i<n; i++){
			int a;
			scanf("%d", &a);
			if(a==i+1) s++;		
		}
		printf("Case #%d: %d.000000\n",r,n-s);
	}
return 0;}
