#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	int t;
	cin >> t;
	int k;
	ofstream outf;
	outf.open("1.out",ios::out);
	for (k = 1; k <= t;k++)
	{
		int c, d, n;
		cin >> c;
		char comb[5];
		if (c == 1)
			cin >> comb;
		cin >> d;
		char opp[5];
		if (d == 1)
			cin >> opp;
		char str[20];
		int len;
		cin >> len;
		cin >> str;
		int i,j;
		char result[20];
		int p = 0;
		bool flag = false;
		bool done = false;
		for (i = 0;i < len;i++)
		{
			result[p++] = str[i];
			if (c == 1)
			{
				if (p > 1 &&(( result[p-1] == comb[0] && result[p-2] == comb[1])||(result[p-2] == comb[0] && result[p-1] == comb[1])))
				{
					result[p-2] = comb[2];
					p--;
					done = true;
				}
			}
			if (d == 1)
			{
				flag = false;
				for (j = 0;j < p;j++)
				{
					if (result[j] == opp[0])
					{
						flag = true;
						break;
					}
				}
				if (flag)
				{
					flag = false;
					for (j = 0;j < p;j++)
					{
						if (result[j] == opp[1])
						{
							flag = true;
							break;
						}
					}
					if (flag)
					{
						p = 0;
						done = true;
					}
				}
			}
		}
		result[p] ='\0';
		outf <<"Case #"<<k<<": [";
		for (i = 0;i < p-1;i++)
			outf <<result[i] <<", ";
		if (p > 0)
			outf << result[p-1];
		outf <<"]"<<endl;
	}
	return 0;
}
