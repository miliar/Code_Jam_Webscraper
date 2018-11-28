#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for( int a = 0; a < t; a++ )
	{
		string line;
		cin >> line;
		//cout << line << endl;
		int *array;
		int no = line.size();
		array = new int[no];
	
		for( int i = 0; i < no; i++ )
		{
			array[i] = line.c_str()[i] - '0';
		}
		bool answer = next_permutation(array, array+no);
	

		cout << "Case #" << a+1 << ": ";
		if( answer == false )
		{
			int count;
			for( count = 0; array[count] == 0 ; count++ );
			cout << array[count] << "0";
			for( int i = 0; i < count; i++ )
			{
				cout << "0";
			}
			for( int i = count + 1; i < no; i++ )
			{
				cout << array[i];
			}
		}
		else
		{
			for( int i = 0; i < no; i++ )
			{
				cout << array[i];
			}
		}

		cout << endl;
	}
	return 1;
}

