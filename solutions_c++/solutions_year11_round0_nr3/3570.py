#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int T,N, m=0;
	long in[1000];
	cin >> T;
	long x=0, s=0;
	while(T--)
	{
		x=0,s=0;
		m++;
		cin >> N;
		for(int i=0; i<N; i++)
		{
			cin >> in[i];
			x = x^in[i];
			s = s + in[i];
		}
		if(x)
		{
			cout << "Case #" << m << ": NO\n";
			continue;
		}
		else
		{
			sort(in, in+N);
			cout << "Case #" << m << ": " << s - in[0] << endl;
		}
	}
	return 0;
} 
