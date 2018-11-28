#include <iostream>
#include <memory>
using namespace std;

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T,N;
	int C;
	cin >> T;
	for(int i=0;i<T;i++)
	{
		cin >> N;
		int xo = 0;
		int sum = 0;
		int min = 10000000;
		for(int j=0;j<N;j++)
		{
			cin >> C;
			if(min > C) min = C;
			sum += C;
			xo = xo ^ C;
		}
		cout << "Case #" << i+1 << ": ";
		if(xo == 0)	cout << sum - min <<endl;
		else cout << "NO" <<endl;
	}	
	return 0;
}
