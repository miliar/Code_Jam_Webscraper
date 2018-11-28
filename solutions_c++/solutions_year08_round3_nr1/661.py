#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <numeric>
#include <algorithm>
#include <functional>

using namespace std;

int read(FILE *fp)
{
	int i, j, key_left, press;
	int p, k, l, t, sum;
	vector<int>::iterator it;

	fscanf(fp, "%d %d %d\n", &p, &k, &l);

	vector<int> occur;

	for( i = 0; i < l; i++ )
	{
		fscanf(fp, "%d", &t);

		occur.push_back(t);
	}

	sort(occur.begin(), occur.end(), greater<int>());

	key_left = 0;
	press = 0;
	
	for( i = 0; i < l; i++ )
	{
		if( key_left == 0 )
		{
			key_left = k;
			press++;

			if( p < press )
				return -1;
		}

		occur[i] *= press;
		key_left--;
	}

	sum = 0;

	for( it = occur.begin(); it != occur.end(); it++ )
		sum += *it;

	return sum;
}


int main(int argc, char *argv[])
{
	FILE *fp;
	int i, max_trial, sum;

	if( argc < 2 )
	{
		printf("%s <filename>\n", argv[0]);

		return -1;
	}

	fp = fopen(argv[1], "r");

	if( fp == NULL )
	{
		printf("Unable to open file '%s'\n", argv[1]);

		return -2;
	}

	fscanf(fp, "%d\n", &max_trial);

	for( i = 0; i < max_trial; i++ )
	{
		sum = read(fp);

		if( sum < 0 )
			printf("Case #%d: Impossible\n", i + 1);
		else
			printf("Case #%d: %d\n", i + 1, sum);
	}

	fclose(fp);

	return 0;
}
