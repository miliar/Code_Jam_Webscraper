#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	vector<int> freq;
	int test_cases;
	ofstream out("out.txt");
	ifstream in("A.in");
	in >> test_cases;
	for(int i = 1; i <= test_cases; i++)
	{
		int p, k, l;
		in >> p >> k >> l;
		for(int j = 0; j < l; j++)
		{
			int f;
			in >> f;
			freq.push_back(f);
		}
		if (p * k < l)
			out << "Case #" << i << ": Impossible" << endl;
		else
		{
			sort(freq.begin(), freq.end());
			int answer = 0;
			int ratio = 1;
			for(int j = 1; j <= l; j++)
			{
				//cout << freq[l - j] << "  " << ratio << endl;
				answer += ratio * freq[l - j];
				if(!(j % k))
					ratio++;
			}
			out << "Case #" << i << ": " << answer << endl;
		}
		freq.clear();
	}
	return 0;
}