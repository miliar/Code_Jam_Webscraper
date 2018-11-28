#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int c = 1; c <= T; c++)
	{
		int N, S, p;
		cin >> N >> S >> p;
		vector<int> v(N);
		for (int j = 0; j < N; j++)
			cin >> v[j];
		sort(v.begin(),v.end(), greater<int>());
		int count = 0;
		if (p == 0)
		{
			cout << "Case #" << c << ": " << N << endl;	
			continue;
		}
		for (int i=0; i < v.size(); i++)
		{
			if (v[i] > 0 && (v[i]+2)/3 >= p)
				count++;
			else if (v[i] > 1 && S > 0 && (v[i]+4)/3 >= p)
			{
				count++;
				S--;
			}
			else
				break;
		}
		cout << "Case #" << c << ": " << count << endl;		
	}
	return 0;
}
	
