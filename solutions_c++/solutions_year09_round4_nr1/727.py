#include <iostream>
#include <vector>
using namespace std;

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int numt;
	cin >> numt;
	
	
	for(int it=0; it<numt; it++)
	{
		vector<int> values;
		int n = 0;
		// read
		cin >> n;

		char buf[1024];
		for(int i=0; i<n; i++)
		{
			cin >> buf;

			int zend = 0;
			for(int j=0; j<n; j++)
			{
				if( buf[j]=='0' )
				{
					++zend;
				}
				else
				{
					zend = 0;
				}
			}
			values.push_back(zend);
		}

		//cout << "[";
		//for(int i=0; i<values.size(); i++)
		//	cout << values[i]<< " ";
		//cout << "]";
		//cout << endl;

		int countSwaps=0;
		
		int toHaveHere = n;
		for(int pos = 0; pos<n; pos++)
		{
			toHaveHere--;

			int idToUse = -1;
			for(int i=pos; i<n; i++)
			{
				if( values[i]>=toHaveHere )
				{
					idToUse = i;
					break;
				}
			}
			// now move idToUse up
			for(int i=idToUse; i>pos; i--)
			{
				countSwaps++;
				swap(values[i], values[i-1]);
			}
		}

		cout << "Case #" << (it+1) << ": " << countSwaps << endl;
	}

	return 0;
}