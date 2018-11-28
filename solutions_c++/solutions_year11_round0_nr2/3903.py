#include <iostream>
#include <cmath>
#include <list>
#include <string>
#include <string>

using namespace std;

struct combination
{
	char elements[2];
	bool present[2];
	int positions[2];
	char result;
};

struct opposition
{
	char elements[2];
	int positions[2];
	bool present[2];
};

int main()
{
	int n;
	cin >> n;

	for( int i = 0; i < n; i++ )
	{
		int c;
		cin >> c;

		combination *combine = new combination[c];
		for( int j = 0; j < c; j++ )
		{
			cin >> combine[j].elements[0];
			cin >> combine[j].elements[1];
			cin >> combine[j].result;
		}

		int d;
		cin >> d;

		opposition *oppose = new opposition[d];
		for( int j = 0; j < d; j++ )
		{
			cin >> oppose[j].elements[0];
			cin >> oppose[j].elements[1];
		}

		int count;
		cin >> count;

		char *elements = new char[count];
		for( int j = 0; j < count; j++ )
		{
			cin >> elements[j];
		}

		bool operated = true;

		while(operated)
		{
			operated = false;

			for( int x = 0; x < c; x++ )
			{
				combine[x].present[0] = false;
				combine[x].present[1] = false;
				combine[x].positions[0] = -1;
				combine[x].positions[1] = -1;
			}
			for( int x = 0; x < d; x++ )
			{
				oppose[x].positions[0] = -1;
				oppose[x].positions[1] = -1;
				oppose[x].present[0] = false;
				oppose[x].present[1] = false;
			}	

			for( int j = 0; j < count; j++ )
			{
				for( int k = 0; k < c; k++ )
				{
					if( elements[j] == combine[k].elements[0] )
					{
						if(combine[k].present[1] && combine[k].positions[1] == (j - 1) && elements[j - 1] != ' ')
						{
							elements[j-1] = combine[k].result;
							elements[j] = ' ';
							combine[k].present[1] = false;
							combine[k].positions[1] = -1;
							operated = true;
						}
						else
						{
							combine[k].present[0] = true;
							combine[k].positions[0] = j;
						}
					}

					if( elements[j] == combine[k].elements[1] )
					{
						if(combine[k].present[0] && combine[k].positions[0] == (j - 1) && elements[j - 1] != ' ')
						{
							elements[j-1] = combine[k].result;
							elements[j] = ' ';
							combine[k].present[0] = false;
							combine[k].positions[0] = -1;
							operated = true;
						}
						else
						{
							combine[k].present[1] = true;
							combine[k].positions[1] = j;
						}
					}
				}

				for( int k = 0; k < d; k++ )
				{
					if( elements[j] == oppose[k].elements[0] )
					{
						if( oppose[k].present[1] && oppose[k].elements[1] == elements[oppose[k].positions[1]] )
						{
							for( int l = 0; l <= j; l++ )
							{
								elements[l] = ' ';
							}
							oppose[k].present[1] = false;
							oppose[k].positions[1] = -1;
						}
						else
						{
							oppose[k].present[0] = true;
							oppose[k].positions[0] = j;
						}
					}

					if( elements[j] == oppose[k].elements[1] )
					{
						if( oppose[k].present[0] && oppose[k].elements[0] == elements[oppose[k].positions[0]] )
						{
							for( int l = 0; l <= j; l++ )
							{
								elements[l] = ' ';
							}
							oppose[k].present[0] = false;
							oppose[k].positions[0] = -1;
						}
						else
						{
							oppose[k].present[1] = true;
							oppose[k].positions[1] = j;
						}
					}
				}
			}	
		}

//		for( int j = 0; j < count; j++ )
//		{
//			cout << elements[j] << " ";
//		}
//		cout << endl;

		cout << "Case #" << i + 1 << ": [";
		bool flag = false;
		for( int j = 0; j < count; j++ )
		{
			if( elements[j] != ' ')
			{
				if(flag)
				{
					cout << ", " << elements[j];
				}
				else
				{
					cout << elements[j];
					flag = true;
				}
			}
		}
		cout << "]" << endl;

		delete [] combine;
		delete [] oppose;

	}

	return 0;
}
