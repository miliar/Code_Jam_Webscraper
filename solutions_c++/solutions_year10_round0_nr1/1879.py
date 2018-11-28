// bnbn.cpp : Defines the entry point for the console application.
//

#include <iostream>

using namespace std;
void v(int j, int m){
	if (m == 1)
		cout<<"Case #"<<j<<": ON"<<endl;
	else
		cout<<"Case #"<<j<<": OFF"<<endl;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	__int64 k, n, t, i, b, step;
	cin>>t;
	for (i = 1; i <= t; i++)
	{
		cin>>n>>k;
		step = 1;
		for (b = 1; b<=n;  b++)
		{
			step = step*2;
		}
		if ((k%step)==(step-1))
			v(i,1);
		else
			v(i,0);
			
	}

	return 0;
}

