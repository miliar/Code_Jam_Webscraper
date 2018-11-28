#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	int Z;
	cin >> Z;
	for(int i = 0; i < Z; i++)
	{
		int N;
		cin >> N; 
		vector<int> scor;
		int res = 0;
		int S;
		cin >> S;
		int best;
		cin >> best;
		for(int j = 0; j < N; j++)
		{
			int val;
			cin >> val;
			scor.push_back(val);
		}
		sort(scor.begin(),scor.end());

		for(int j = 0; j < N; j++)
		{
			if(scor[j] >= best)
			{
				if(S > 0 && 3 * best - 4 <= scor[j])
				{
					S--;	
					res++;			
				}
	
				else if(3 * best - 2 <= scor[j])
				{
					res++;
				}
			}
		}
		cout <<"Case #" << i + 1 << ": " << res << endl;
					
		scor.clear();
	}
	return 0;
}
