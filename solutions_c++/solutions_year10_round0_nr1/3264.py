#include<iostream>
#include<math.h>

using namespace std;
int main()
{
	int T, N, K, i;
	cin>>T;
	bool ans[10000];
	for (i = 0; i < T; i++)
	{
		cin>>N>>K;
		double h = ((double)(K+1))/pow(2, N-1);
		if (h - (int)h == 0)
			if ((int)h%2 == 0)
				ans[i] = true;
			else
				ans[i] = false;
		else
			ans[i] = false;
	}
	for (int j = 0; j < i; j++)
	{
		cout<<"Case #"<<j+1<<": ";
		cout<<((ans[j]==true)?"ON":"OFF")<<endl;
	}
	//cout<<"hi"<<pow(2, 4);
}
