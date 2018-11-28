#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int hash[27][5] = {0};
	const char des[20] = "welcome to code jam";

	ifstream fin("C-small-attempt0.in");
	ofstream fout("c.out");

	int n;
	int sum;
	int k;
	int k2;
	int length;
	int map[20][505];
	int num[20][505];
	char text[505];
	char tmp;
	char sumchar[5];
	char out[5];
	// initialize hash
	for (int i=0; i<26; i++)
		for (int j=0; j<19; j++)
			if ('a' + i == des[j])
			{
				hash[i][0]++;
				hash[i][ hash[i][0] ] = j;
			};
	hash[26][0] = 3;
	hash[26][1] = 7;
	hash[26][2] = 10;
	hash[26][3] = 15;
	// main begin
	fin >> n;
	fin.get();
	for (int z=0; z<n; z++)
	{
		// init map for text
		fin.getline(text,500);	
		memset(map, 0, sizeof(map));
		length = strlen(text);
		if (length == 0)
		{
			cout << "Case #" << z+1 << ": 0" << endl;
			continue;
		}
		for (int i=0; i<length; i++)
		{
			tmp = text[i];
			if (tmp == ' ')
			{
				k = hash[26][0];
				tmp = 'z' + 1;
			}
			else
				k = hash[tmp - 'a'][0];

			for (int j=1; j<=k; j++)
			{
				k2 = ++map[ hash[tmp - 'a'][j] ][0];
				map[ hash[tmp - 'a'][j] ][k2] = i;
			}
		}

		// cal the num
		memset(num, 0, sizeof(num));
		for (i=1; i<=map[0][0]; i++)
			num[0][i] = 1;

		for (i=1; i<19; i++)
		{
			k = map[i][0];
			for (int j=1; j<=k; j++)
			{
				k2 = map[i-1][0];
				for (int g=1; g<=k2; g++)
					if (map[i][j] > map[i-1][g])
						num[i][j] += num[i-1][g];
			}
		}
		// out
		k = map[18][0];
		sum = 0;
		for (i=1; i<=k; i++)
			sum += num[18][i];
		
		if (sum > 9999)
		{
			sum %= 10000;
			itoa(sum, out, 10);
		}
		else
		{
			itoa(sum, sumchar, 10);
			strcpy(out, "");
			for (int i=0; i<4-strlen(sumchar); i++)
				strcat(out, "0");
			strcat(out, sumchar);
		}			
		fout << "Case #" << z+1 << ": " << out << endl;
	}
	fin.close();
	fout.close();
	return 0;
}