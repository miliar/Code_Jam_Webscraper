#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<list>
#include<queue>
#include<cctype>
#include<stack>
#include<map>
#include<set>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int n,k;
		cin>>n>>k;
		int pow=1<<n;
		k=k%pow;
		printf("Case #%d: ",i);
		if(k+1==pow)
			printf("%s\n","ON");
		else 
			printf("%s\n","OFF");
	}




	
	return 0;
}
