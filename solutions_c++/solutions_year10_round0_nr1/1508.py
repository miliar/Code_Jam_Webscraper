#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int T, N, K, nCase=1;

int main()
{
	cin>>T;
	while(T--)
	{
		cin>>N>>K;
		cout<<"Case #"<<nCase++<<": ";
		if( (K&((1<<N)-1))==((1<<N)-1) )
			cout<<"ON\n";
		else
		    cout<<"OFF\n";
	}
    return 0;
}


