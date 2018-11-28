#include <fstream>
#include <algorithm>
using namespace std;

ifstream input("input.txt");
ofstream output("output.txt");

int main()
{
	int t, n;
	int arr[1000];
	int sarr[1000];
	input >> t;
	for (int i=0;i<t;++i)
	{
		input >> n;
		for (int j=0;j<n;++j)
		{
			int v;
			input >> v;
			sarr[j] = arr[j] = v;			
		}
		sort(sarr,sarr+n);
		int inplace = 0;
		for (int j=0;j<n;++j) if (arr[j]==sarr[j]) ++inplace;
		output << "Case #" << i+1 << ": " << n-inplace << endl;
	}
	return 0;
}