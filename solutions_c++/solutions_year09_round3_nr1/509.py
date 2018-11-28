#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;

char as[257];
unsigned long long ret;

int main()
{
	int i, j, id, N;
	char buff[100], flag;

	freopen("A.IN","r",stdin);
	freopen("A.out","w",stdout);

	cin >> N;

	for ( i = 1; i <= N; ++i )
	{
		cin >> buff;
		memset(as,'-',sizeof(as));
		//cout << buff << endl;

		id = 1;
		flag = 0;
		for ( j = 0; j < strlen(buff); ++j )
		{
			if ( as[ buff[j] ] == '-' )
			{
				if ( id == 2 && !flag )
					as[ buff[j] ] = 0, flag = 1;
				else
					as[ buff[j] ] = id++;
			}

		//	cout << buff[j] << " " << (int)as[ buff[j] ] << endl;

		}

		ret = 0;
		//cout << id << endl;
		for ( j = 0; j < strlen(buff); ++j )
			ret = ret * id + as[ buff[ j ] ];

		cout << "Case #" << i << ": " << ret << endl;
	}

	return 0;
}