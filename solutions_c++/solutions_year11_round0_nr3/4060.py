#include <iostream>

using namespace std;

int main()
{
	int test, test_count;
	cin >> test_count;
	for (test=1;test<=test_count;test++)
	{
		int n;
		cin >> n;
		int x[15];
		for (int i=0;i<n;i++)
		{
			cin >> x[i];
		}

		int res = -1;
		for (int mask = 1;mask < (1<<n)-1;mask++)
		{
			int xor1=0, xor2=0;
			int sum1=0,sum2 = 0;
			for (int i=0;i<n;i++)
			{
				if (mask & (1<<i) ) {sum1+=x[i];xor1^=x[i];}
				else {sum2+=x[i];xor2^=x[i];}
			}

			if (xor1==xor2 && max(sum1,sum2)>res)
				res = max(sum1, sum2);
		}
		cout << "Case #" << test << ": ";
		if (res==-1) cout << "NO\n";
		else cout << res << endl;
	}

	return 0;
}