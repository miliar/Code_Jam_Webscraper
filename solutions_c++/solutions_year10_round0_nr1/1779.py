#include <iostream>

using namespace std;

int main()
{
	int N,K,T;
	
	cin>>T;
	for(int x=1; x<=T; x++){
		cin>>N>>K;
		printf("Case #%d: %s\n",x,( (K&((1<<N)-1))==((1<<N)-1)? "ON" : "OFF"));
	}
	return 0;
}
