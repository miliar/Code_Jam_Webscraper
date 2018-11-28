#include <iostream>
using namespace std;

int main()
{
	int n;
	cin >> n;
	for(int i=1;i<=n;i++)
	{
		cout << "Case #" << i << ": ";
		long long N;
		int PD,PG;
		cin >> N >> PD >> PG;
		if(PD==PG&&PG==100)
		{
			cout << "Possible" << endl;
			goto endloop;
		}
		if(PD==0&&PG!=100)
		{
			cout << "Possible" << endl;
			goto endloop;
		}
		if(PD<100&&PG==100)
		{
			cout << "Broken" << endl;
			goto endloop;
		}
		if(PD>0&&PG==0)
		{
			cout << "Broken" << endl;
			goto endloop;
		}
		for(int j=1;j<=PD&&j<=N;j++)
		{
			if(j*100%PD==0&&j*100/PD<=N)
			{
				cout << "Possible" << endl;
				goto endloop;
			}
		}
		cout << "Broken" << endl;
	endloop:;
	}
}
