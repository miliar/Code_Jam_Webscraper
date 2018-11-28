#include <cstdio>
#include <iostream>
using namespace std;

int N,K;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,T;
	cin >> T;
	for (i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		cin >> N >> K;
		if ((K & ((1<<N)-1)) == ((1<<N)-1)) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}
