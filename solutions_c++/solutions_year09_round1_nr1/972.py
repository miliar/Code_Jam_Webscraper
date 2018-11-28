#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

bool ishappy(int a, int base)
{
	vector<int> cycle;
	
	
	while (1)
	{
		
	int sum = 0;
	while (a)
	{
		int rem = a % base;
		sum += rem * rem;
		a = a / base;
	}
	
	if (sum == 1)
	{
		return true;
	}
	else
	{
		if (find(cycle.begin(), cycle.end(), sum) != cycle.end())
		{
			return false;
		}
		else
		{
			cycle.push_back(sum);
			a = sum;
		}
	}
		
	}
	
	
}

int main(int argc, char** argv)
{
	char temp[100];
	cin.getline(temp, 100);
	
	int ncases;
	sscanf(temp, "%d", &ncases);

	for (int i = 0; i < ncases; i++)
	{
		vector<int> bases;
		
		cin.getline(temp, 100);
		
		istringstream iss(temp, istringstream::in);
		
		while (!iss.eof())
		{
			int x;
			iss >> x;
			bases.push_back(x);
		}
		
		int j;
		for (j = 2; ; j++)
		{
			bool stillhappy = true;
			for (int k = 0; k < bases.size(); k++)
			{
				if (!ishappy(j, bases[k]))
				{
					stillhappy = false;
					break;
				}
			
			}
			
			if (stillhappy)
			{
				break;
			}

		}
		
		cout << "Case #" << i + 1 << ": " << j << endl;
		
	}


}