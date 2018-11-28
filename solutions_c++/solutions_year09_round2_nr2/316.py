#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char** argv)
{


	int ncases;
	cin >> ncases;
	
	for (int i = 0; i < ncases; i++)
	{
		string num;
		cin >> num;
		//cerr << "num " << num << endl;
		
		int count[10];
		
		memset(count, 0, sizeof(count));
		
		for (int j = 0; j < num.length(); j++)
		{
			count[num[j] - '0']++;
		}
		
		int test[10];
		memcpy(test, count, sizeof(test));
		int last = -1;
		
		for (int j = 0; j < num.length(); j++)
		{
			int dig = num[j] - '0';
			
			for (int k = dig+1; k <= 9; k++)
			{
				if (test[k] > 0)
				{
					last = j;
					break;
				}
			}
			
			test[dig]--;
		}
		
		//cerr << "last " << last << endl;
		
		string output;
		
		if (last == -1)
		{
			count[0]++;
			
			for (int j = 1; j <= 9; j++)
			{
				if (count[j] > 0)
				{
					count[j]--;
					output += (char)j + '0';
					break;
				}
			}
			
		}
		else
		{
			
			for (int j = 0; j < last; j++)
			{	
				output += num[j];
				count[num[j] - '0']--;
			}
		
			int dom = num[last] - '0';
		
			for (int j = dom+1; j <= 9; j++)
			{
				if (count[j] > 0)
				{
					count[j]--;
					output += (char)j + '0';
					break;
				}
			}
		}
		
		for (int j = 0; j <= 9; j++)
		{
			for (int k = 0; k < count[j]; k++)
			{
				output += (char)j + '0';
			}
		}
				
		cout << "Case #" << i + 1 << ": " << output << endl;
		
	}

}