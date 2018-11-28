#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
using namespace std;
int main()
{
	int total_inputs;
	cin >> total_inputs;
	//cout <<"no inputs:" << NoOfInputs << endl;
	int temp = 0;

	for( int i = 0; i < total_inputs; i++ )
	{
		//Input for case started
		int total_engines;
		cin >> total_engines;
		bool *flag;
		flag = new bool[total_engines];
		string *search_engines;
		search_engines = new string[total_engines];

		if( total_engines != 0 )
		{
			getline( cin , search_engines[0] , '\n' );
		}

		//cout << total_engines << endl;

		for( int j = 0; j < total_engines; j++ )
		{
			getline( cin, search_engines[j], '\n' );
			flag[j] = false;
			//cout << j << search_engines[j] << endl;
		}



		int list_index;
		cin >> list_index;
		string *engines;
		engines = new string[list_index];

		// cout << list_index << endl;

		if( list_index != 0 )
		{
			getline( cin , engines[0] , '\n' );
		}

		for( int j = 0; j < list_index; j++ )
		{
			getline( cin, engines[j], '\n' );
			// cout << j << engines[j] << endl;
		}
		//Input for case completed

		int switch_count = 0;
		int count = 0;
		int tempstore=0;
		for( int j = 0; j < list_index; j++ )
		{
			for( int k = 0; k < total_engines; k++ )
			{
				if( flag[k] != true )
				{
					if( engines[j] == search_engines[k] )
					{
						flag[k] = true;
						count++;
						tempstore = k;
					}

				}

				if( count == total_engines )
				{
					switch_count++;
					for( int k = 0; k < total_engines; k++ )
					{
						flag[k] = false;

					}
					flag[tempstore] = true;
					count = 1;
				}
			}
		}
		cout << "Case #" << (i + 1) << ": " << switch_count << endl;
	}
return 0;
}

