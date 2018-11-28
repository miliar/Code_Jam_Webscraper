#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
void main()
{
	freopen("A-large.in.txt","r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);

	for (int ctr = 1; ctr <= T; ctr++)
	{
		int N;
		scanf("%d", &N);
		int K;
		scanf("%d", &K);

		bool onoff = false;
		if(((K+1)%(int)pow(2.0, N)) == 0)
			onoff = true;

		if(onoff)
			cout<<"Case #"<<ctr<<": ON"<<endl;
		else
			cout<<"Case #"<<ctr<<": OFF"<<endl;
	}

}