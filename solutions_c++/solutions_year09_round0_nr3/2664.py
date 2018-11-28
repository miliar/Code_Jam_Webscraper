#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstring>
using namespace std;


int a[500][19];
int b[27][3];
int index[27];
int main()
{
	char c[] = "welcome to code jam";
	ifstream in("C-small-attempt3.in");
	ofstream out("out2.txt");
	for(int i=0; i<strlen(c); i++)
	{
		if(c[i] != ' ')
		{
			b[c[i]-'a'][index[c[i]-'a']] = i;
			index[c[i]-'a'] ++;
		}
		else
		{
			b[26][index[26]] = i;
			index[26] ++;
		}
	}

	string s;
	getline(in, s);
	int N;
	istringstream is(s);
	is >> N;
	int count = 0;
	while(N--)
	{
		count ++;
		char cc[500] = {0};
		string s;
		getline(in, s);
		memcpy(cc, s.c_str(), s.size());
		memset(a, 0, sizeof(a));

		int start, i;
		for(i=0; i<strlen(cc); i++)
		{
			if(cc[i] == 'w')
			{
				start = i;
				break;
			}
		}
		if(i == strlen(cc))
		{
			out << "Case #" << count << ": " << "0000" << endl;
			continue;
		}
		a[start][0] = 1;
		for(int i=start+1; i<strlen(cc); i++)
		{
			memcpy(a[i], a[i-1], sizeof(a[0]));
			if(cc[i] == 'w')
			{
				a[i][0] = a[i-1][0] + 1;
			}
			else if(cc[i] != ' ')
			{
				for(int j=0; j<index[cc[i]-'a']; j++)
				{
					a[i][b[cc[i]-'a'][j]] += a[i-1][b[cc[i]-'a'][j]-1];
				}
			}
			else
			{
				for(int j=0; j<index[26]; j++)
				{
					a[i][b[26][j]] += a[i-1][b[26][j]-1];
				}
			}
		}
		int result = a[strlen(cc)-1][18]%10000;
		
		out << "Case #" << count << ": " << setw(4) << setfill('0') << result << endl;
	}
	

	return 0;
}
