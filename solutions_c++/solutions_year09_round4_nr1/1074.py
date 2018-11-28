#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	
	int R;
	in >> R;
	//cout << "R = " << R << endl;
	char s[100];
	int ones[100];	
	for (int Case = 1; Case <= R; Case++)
	{
		cout << "case = " << Case << endl;
		int N;
		in >> N;
		//cout << "R = " << R << endl;
		//cout << "case: " << Case << " N = " << N << endl;
		for (int i = 0;i < N;i++)
		{
			in >> s;
			//cout << "row: " << i << " " << s << endl;
			ones[i] = -1;
			for (int j = 0;j < N;j++)
			{
				if (s[j] == '1')
				{
					ones[i] = j;
					//cout << " " << j << endl;
				}
			}
		}
		//cout << "R = " << R << endl;
		int ctr = 0;
		for (int i = 0;i < N;i++)
		{
			int loc = 0;
			for (int j = i;j < N;j++)
			{
				if (ones[j] <= i)
				{
					//cout << i << " " << j << endl;
					loc = j;
					break;
				}
			}
			for (int j = loc;j > i;j--)
			{
				int temp = ones[j];
				ones[j] = ones[j-1];
				ones[j-1] = temp;
				ctr++;
			}
		}
		//cout << "R = " << R << endl;
		//cout << "Case#" << Case << ": " << ctr << endl;
		out << "Case #" << Case << ": " << ctr << endl;
	}
	cout << R << endl;

	return 0;
}