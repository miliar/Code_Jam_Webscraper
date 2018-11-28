#include <iostream>

#define MAX 10

using namespace std;

int main()
{
	int T, nTestcase = 1;
	cin >> T;
	while(T--)
	{
		int r, k ,n;
		cin >> r >> k >> n;

		int gTable[MAX];
		for(int i=0; i<n; ++i)
			cin >> gTable[i];


		int money = 0, idx = 0, s = 0, sIdx = 0;

		bool flag = false;
		while(r)
		{
			s += gTable[idx];

			if(s>k)
			{
				s-=gTable[idx];

				money += s;
				
				r--;

				s = 0;

				sIdx = idx;
				flag = true;

				-- idx;
			}



			++idx;
			idx%=n;



			if(idx == sIdx && !flag)
			{
				money += s;
				r--;
				s = 0;
				sIdx = idx;
				flag = false;
			}

		}

		cout << "Case #" << nTestcase++ << ": " << money << endl;
		
	}
	return 0;
}