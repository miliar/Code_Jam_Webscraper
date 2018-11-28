#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

void input()
{
	int T;
	cin >> T;
	for(int i=0; i<T; i++)
	{
		int N;
		cin >> N;
		
		int table[10]={0,};

		int t=N;
		while(t>0)
		{
			table[t%10]++;
			t/=10;
		}

		int res=0;
		for(int j=N+1; ;j++)
		{
			int table2[10]={0,};
			int temp=j;
			while(temp>0)
			{
				table2[temp%10]++;
				temp/=10;
			}

			bool s=true;
			for(int k=1;k<10;k++)
			{
				if(table[k] != table2[k])
					s=false;
			}
			if(s)
			{
				res=j;
				break;
			}
		}
		cout << "Case #" << (i+1) << ": " << res << endl;
	}
}

int main()
{
	input();
	return 0;
}
