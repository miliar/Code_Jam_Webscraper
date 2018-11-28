#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int N,T,t=1,K;
	
	cin>>T;
	while(T--)
	{
		cin>>N>>K;
		
		int n = pow(2.0,N);
		if((K-n+1)%n==0)
			printf("Case #%d: ON\n",t++);
		else
			printf("Case #%d: OFF\n",t++);

	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
