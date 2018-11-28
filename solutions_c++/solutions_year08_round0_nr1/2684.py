#include <fstream>
#include <string>
#include <iostream>
using namespace std;
void z(bool b[10])
{
	int it1;
	for(it1 = 0; it1 < 10; it1++)
	{
		b[it1] = 0;
	}
}
int main()
{
	bool b[10] = {0};
	string s;
	char c1[2];
	char c2[2];
	char c3[3];
	int i, j, k, c = 0, current;
	int an[20] = {0};
	string as[10];
	string aq[100];
	ifstream input("A-small.in");
	getline(input, s);
	for(i = 0; i < s.size(); i++)
	{
		c1[i] = s[i];
	}
	c1[i] = '\0';
	for(i = 0; i < atoi(c1); i++)
	{
		getline(input, s);
		for(j = 0; j < s.size(); j++)
		{
			c2[j] = s[j];
		}
		c2[j] = '\0';
		for(j = 0; j < atoi(c2); j++)
		{
			getline(input, as[j]);
		}
		getline(input, s);
		for(j = 0; j < s.size(); j++)
		{
			c3[j] = s[j];
		}
		c3[j] = '\0';
		for(j = 0; j < atoi(c3); j++)
		{
			getline(input, aq[j]);
		}
		for(j = 0; j < atoi(c3); j++)
		{
			for(k = 0; k < atoi(c2); k++)
			{
				if(aq[j] == as[k])
				{
					current = k;
					b[k] = 1;
					break;
				}
			}
			for(k = 0; k < atoi(c2); k++)
			{
				if(b[k] == 0)
				{
					break;
				}
				if(k == atoi(c2) - 1)
				{
					z(b);
					b[current] = 1;
					c++;
				}
			}
		}
		an[i] = c;
		z(b);
		c = 0;
	}
	input.close();
	ofstream output("A-small.out");
	for(i = 0; i < atoi(c1); i++)
	{
		output << "Case #" << i + 1 << ": " << an[i] << '\n';
	}
	output.close();
	return 0;
}