#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>

int T;
int A;
int B;
char b_[100];

int RecycleCount(int n)
{
	char n_[100];
	itoa(n,n_,10);
	int digit = strlen(n_);
	
	std::list<int> result;
	
	int ret = 0;
	for(int sp = 1; sp < digit; sp++)
	{
		bool flag = false;
		for(int i = 0; i < digit; i++)
		{
			int n_p = (i + sp) % digit;
			if(n_[n_p] < n_[i] )
			{
				break;
			}
			else if(n_[n_p] > n_[i])
			{
				flag = true;
				break;
			}
		}
		if(flag)
		{
			for(int i = 0; i < digit; i++)
			{
				int n_p = (i + sp) % digit;
				if(n_[n_p] > b_[i])
				{
					flag = false;
					break;
				}
				else if(n_[n_p] < b_[i])
				{
					break;
				}
			}
			if(flag)
			{
				char temp[100];
				temp[digit] = 0;
				for(int i = 0; i < digit; i++)
				{
					int n_p = (i + sp) % digit;
					temp[i] = n_[n_p];
				}
				int temp_ = atoi(temp);
				for(std::list<int>::iterator it = result.begin(); it != result.end(); it++)
				{
					if(temp_ == *it)
					{
						flag = false;
						break;
					}
				}
				if(flag)
				{
					ret++;
					result.push_back(temp_);
				}
			}
		}
	}
	return ret;
}
bool IsRecycle(int n, int m)
{
	char n_[100];
	char m_[100];
	itoa(n,n_,10);
	itoa(m,m_,10);

	int digit = strlen(n_);
	for(int sp = 0; sp < digit; sp++)
	{
		if(n_[sp] == '0')
			continue;
		if(n_[sp] < n_[0])
			continue;
		bool flag = true;
		for(int i = 0; i < digit; i++)
		{
			int n_p = (sp + i) % digit;
			if(n_[n_p] != m_[i])
			{
				flag = false;
				break;
			}
		}
		if(flag)
		{
			return true;
		}
	}
	return false;
}

int main()
{
	std::fstream input;
	std::fstream output;
	input.open( "input.txt", std::istream::in );
	output.open("output.txt", std::ostream::out);

	input >> T;
	for(int t = 0; t < T; t++)
	{
		input >> A >> B;

		itoa(B,b_,10);
		int out = 0;
		for(int n = A; n < B; n++)
		{
			out += RecycleCount(n);
		}

		std::cout << "Case #" << t+1 << ": " << out << std::endl;
		output << "Case #" << t+1 << ": " << out << std::endl;
	}
	getchar();
	return 1;
}