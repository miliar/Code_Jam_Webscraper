#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream in("C-small.in");
	ofstream out("C-small.out");

	int T;
	in >> T;
	for(int c=0;c<T;c++)
	{
		int r,k,n;
		in >> r >> k >> n;

		int* gr = new int[n];
		for(int i=0;i<n;i++)
			in >> gr[i];
		
		int sum = 0;
		int index = 0;
		for(int i=0;i<r;i++)
		{
			int sit = 0;
			int tempSit = 0;
			bool circled = false;
			int start = index;
			while( k >= tempSit && !circled)
			{
				sit += gr[index];
				index++;
				index = index%n;
				if( index == start )
					circled = true;
				tempSit = sit + gr[index];
				
			}
			sum += sit;
		}
		out << "Case #" << c+1 << ": " << sum << endl;
	}

	return 0;
}