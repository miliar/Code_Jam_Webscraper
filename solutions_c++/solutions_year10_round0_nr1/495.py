#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	cin>>T;
	int i,n,k;
	for(i=1;i<=T;i++){
		cin>>n>>k;
		n = (1<<n) - 1;
		printf("Case #%d: %s\n",i,(k&n)==n?"ON":"OFF");
	}
	return 0;
}
