#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

vector <int> v;
int T;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &T);
	scanf("\n");

	bool b;
	char c;

	for(int i = 0; i < T; i++)
	{
		v.clear();

		while( true )
		{
			if( scanf("%c", &c) != 1 )
				break;
			if( c < '0' || c > '9' )
				break;
			v.push_back( (int)(c - '0') );
		}

		b = next_permutation( v.begin(), v.end() );

		printf("Case #%d: ", i+1);

		if( !b )
		{
			if( v[0] == 0 )
			{
				for(vector<int>::iterator it = v.begin(); it != v.end(); it++)
				{
					if( *it != 0 )
					{
						printf("%d", *it);
						v.erase( it );
						break;
					}
				}

				printf("0%d", v[0]);

			}
			else
			{
				printf("%d", v[0]);
				printf("0");
			}
		}
		else
		{
			printf("%d", v[0]);
		}

		for(int i = 1; i < v.size(); i++)
		{
			printf("%d", v[i]);
		}
		
		printf("\n");
	}

}