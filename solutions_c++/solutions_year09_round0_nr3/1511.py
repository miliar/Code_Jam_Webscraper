#include <iostream>
#include <string>

using namespace std;

int main(int argc, char** argv)
{
	char temp[600];
	int ncases;
	cin.getline(temp, 600);
	sscanf(temp, "%d", &ncases);
	
	const char* key = "welcome to code jam";
	
	for (int i = 0; i < ncases; i++)
	{
		cin.getline(temp, 600);
		string s = temp;
		
		int scores[19];
		memset(scores, 0, sizeof(scores));
		
		for (int j = 0; j < s.length(); j++)
		{
			
			for (int k = 0; k < 19; k++)
			{
				if (s[j] == key[k])
				{
					if (k == 0)
					{
						scores[0]++;
					}
					else
					{
						scores[k] += scores[k-1] % 10000;
					}
				}
			}
		}
		
		int a,b,c,d;
		a = (scores[18] / 1000) % 10;
		b = (scores[18] / 100 ) % 10;
		c = (scores[18] / 10  ) % 10;
		d = (scores[18]       ) % 10;
		
		cout << "Case #" << i + 1 << ": " << a << b << c << d << endl;
			
		
	}



}