#include <iostream>
using namespace std;

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for(int i=0;i<T;i++)
	{
		int N;
		int a[1010];
		int b[1010];
		double res = 0;
		cin >> N;
		for(int j=1;j<=N;j++)
		{
			cin >> a[j];
			b[j] = a[j];
		}
		sort(b+1,b+N+1);
		bool rplace[1010] = {0};
		for(int j=1;j<=N;j++)
			if(a[j] == b[j])
				rplace[j] = true;
		for(int j=1;j<=N;j++)
		{
			if(rplace[j] == false)
			{
				int count = 1;
				int p = j;
				rplace[j] = true;
				while(a[p] != j)
				{
					p = a[p];
					rplace[p] = true;
					count ++;
				}
				res += count;
			}
		}
		cout << "Case #" << i+1 << ": " << res << ".000000" << endl;
	}
	return 0;
}
