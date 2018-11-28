# include <fstream>
# include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	ifstream in("input.in");
	ofstream out("output.out");
	int totalCase;
	in >> totalCase;

	for(int caseNumber = 1; caseNumber <= totalCase; caseNumber++)
	{
		int n=0, pD, pG;
		bool answer = false;
		char buff[100];
		in >> buff;
		for(int i = 0; i < strlen(buff); i++)
		{
			n = n * 10;
			n += buff[i] - '0';
			if(n >= 100)
			{
				answer = true;
				break;
			}
		}

		in >> pD >> pG;

		if(answer == false)
		{
			for(int i = 1; i <= n; i++)
			{
				for(int j = 0; j <=i; j++)
				{
					int per = j * 100 / i;
					if( j * 100 % i != 0)
					{
						continue;
					}
					if(per == pD)
					{
						answer = true;
						break;
					}
				}
				if(answer == true)
				{
					break;
				}
			}
		}

		if(pG == 100 && pD != 100)
		{
			answer = false;
		}

		if(pG == 0 && pD != 0)
		{
			answer = false;
		}
		
		out << "Case #" << caseNumber << ": ";
		if(answer == true)
		{
			out << "Possible" << endl;
		}
		else if(answer == false)
		{
			out << "Broken" << endl;
		}
	}
	return 0;
}