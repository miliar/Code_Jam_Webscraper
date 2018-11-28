# include <vector>
# include <algorithm>
# include <fstream>
# include <iostream>
using namespace std;

int main()
{
	ifstream cin("C-in.txt");
	ofstream cout("C-out.txt");

	int t;
	int case_num = 0;
	cin >> t;
	while(t - case_num++)
	{
		int n;
		cin >> n;
		vector<int> c(n);
		int xor = 0;
		int sum = 0;
		int least = 1000 * 1000 * 1000;
		for(int i = 0; i < n; ++i)
		{
			cin >> c[i];
			least = min(least, c[i]);
			sum += c[i];
			xor ^= c[i];
		}
		
		if(xor == 0)
			cout << "Case #" << case_num << ": " << sum - least << endl;
		else
			cout << "Case #" << case_num << ": NO" << endl;
	}
	return 0;
}
