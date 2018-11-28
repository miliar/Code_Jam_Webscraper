#include <iostream>

using namespace std;

int main ()
{
	int T, N, L, H;
	cin >> T;
	for (int i=0;i<T;++i)
	{
		cin >> N >> L >> H;
		int nums[N];
		for (int k=0;k<N;++k)
			cin >> nums[k];
			
			
		bool notFound=false;
		bool endCase=false;
		cout << "Case #" << i+1 << ": ";
		for (int j=L;j<=H;++j)
		{
			notFound=false;
			for (int k=0;k<N&& notFound==false;++k)
			{
				if (nums[k]%j!=0 && j%nums[k]!=0)
				{
					notFound=true;
				}
			}
			if (notFound == false)
			{
				cout << j << endl;
				endCase = true;
				break;
			}
		}
		if (endCase == false)
			cout << "NO" << endl;
	}
}
