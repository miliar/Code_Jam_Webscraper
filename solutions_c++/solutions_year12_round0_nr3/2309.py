#include <iostream>
#include <fstream>
#include <cmath>
#include <set>

using namespace std;

int main()
{
	ofstream out("3.output");
	int T(0);
	cin >> T;
	for(int cases = 1; cases <= T; cases++)
	{
		int answer(0);
		int A, B;
		cin >> A >> B;
		int size = floor(log10(A))+1;
		for(int n=A; n<=B; n++)
		{
			set<int> currents;
			for(int j=size; j>0; j--)
			{
				int m = n/pow(10, j-1);
				m += (n%(int)pow(10, j-1))*pow(10, size-j+1);
				if(n < m && m <= B)
					currents.insert(m);
			}
			answer += currents.size();
		}
		//cout << answer << endl;
		out << "Case #" << cases << ": " << answer << endl;
	}
	return 0;
}
