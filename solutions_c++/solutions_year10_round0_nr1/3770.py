#include <iostream>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cases;
	cin>>cases;
	int t = 1;
	while (t<=cases)
	{
		cout<<"Case #"<<t<<": ";
		int N, K;
		cin>>N>>K;
		int x=1;
		for (int i=0; i<N; i++)
		{
			x = x<<1;
		}
		if ((K+1)%x==0)
		{
			cout<<"ON";
		}
		else
			cout<<"OFF";
		cout<<endl;
		t++;
	}
	fclose(stdin);
	fclose(stdout);
}