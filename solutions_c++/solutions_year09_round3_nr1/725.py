#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::cerr;
using std::endl;

size_t toAsc(char c)
{
	if('a' <= c && c <= 'z')
		return c - 'a' + 10;
	return c - '0';
}

int main()
{
	size_t ct;
	cin >> ct;

	for(size_t ca = 1; ca <= ct; ca++)
	{
		std::string in;
		cin >> in;

		size_t total_used = 0;
		size_t digit[36];

		for(size_t i = 0; i < 36; i++)
		{
			digit[i] = -1;
		}

		for(size_t i = 0; i < in.size(); i++)
		{
			const size_t ch = toAsc(in[i]);

			if(digit[ch] == -1)
			{
				if(total_used == 0)
				{
					digit[ch] = 1;
				}
				else if(total_used == 1)
				{
					digit[ch] = 0;
				}
				else
				{
					digit[ch] = total_used;
				}
				++total_used;
			}
		}

		unsigned long time = 0;
		//cerr << total_used << endl;
		if(total_used == 1)
		{
			++total_used;
		}

		for(size_t i = 0; i < in.size(); i++)
		{
			time = time * total_used + digit[toAsc(in[i])];
		}

		cout << "Case #" << ca << ": " << time << endl;
	}

	return 0;
}