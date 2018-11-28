#include <map>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <iostream>
using namespace std;

#define FOR(i,n) for(int i=0;i<n;i++)

typedef unsigned long long ull;

int main(){
	int tests,n,k,temp;
	scanf("%d",&tests);
	FOR(t,tests)
	{
		scanf("%d%d",&n,&k);
		temp=1<<n;
		k%=temp;
		if(k==temp-1)printf("Case #%d: ON\n",t+1);
		else printf("Case #%d: OFF\n",t+1);
	}
	
}
