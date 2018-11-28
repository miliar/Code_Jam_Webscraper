#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int main()
{
	int len;
	cin>>len;
	for(int i=0;i<len;++i)
	{
		int N,K,ON;
		scanf("%d",&N);
		scanf("%d",&K);

		ON = K % (1<<N) == ((1<<N)-1);

		cout<<"Case #"<<i+1<<": "<<(ON?"ON":"OFF")<<endl;
	}

	return 0;
}
