#include "iostream"
#include "fstream"

using namespace std;

void main()
{
	ifstream infile("A-large.in");
	ofstream outfile("A-large.out");

	int T;
	infile >> T;
	for(int i=1; i<=T; i++)
	{
		int N;
		infile >> N;
		int *a = new int[N];
		int *b = new int[N];
		for(int j=0; j<N; j++)
		{
			infile >> a[j] >> b[j];
		}

		int count = 0;
		for(int j=0; j<N; j++)
		{
			int left = a[j];
			int right = b[j];
			for(int k=j+1; k<N; k++)
			{
				if((a[k] < left && b[k] > right)
					|| (a[k] > left && b[k] < right))
				{
					count++;
				}
			}
		}

		outfile << "Case #" << i << ": " << count << endl;
		cout << "Case #" << i << ": " << count << endl;
	}

	infile.close();
	outfile.close();
}