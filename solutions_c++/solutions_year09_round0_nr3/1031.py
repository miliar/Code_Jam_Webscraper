#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

static const int MAX_LEN = 510;
static const int MAX_NUM = 10000;

int main()
{
	const char search[] = "welcome to code jam";
	const size_t s_len = sizeof(search) / sizeof(search[0]);
	size_t count;
	cin >> count;
	string t;

	getline(cin, t);

	for(size_t s = 1; s <= count; s++)
	{
		string test;
		getline(cin, test);

		size_t place[MAX_LEN];
		size_t current[MAX_LEN];
		for(size_t i = 0; i < test.size(); i++)
		{
			if(test[i] == search[0])
			{
				current[i] = 1;
				place[i] = 0;
			}
			else
			{
				current[i] = 0;
				place[i] = -1;
			}
		}

		for(size_t i = 1; i < s_len; i++)
		{
			size_t carry = 0;
			for(size_t j = 0; j < test.size(); j++)
			{
				//cerr << search[i] << "," << test[j] << ": " << current[j] << "," << carry << endl;
				//if(place[j] >= i - 1)
				{
					if(test[j] == search[i])
					{
						current[j] = carry;
						place[j] = i;
					}

					if(test[j] == search[i-1])
					{
						carry = (carry + current[j]) % MAX_NUM;
					}
				}
			}

			if(i == s_len - 1)
			{
				printf("Case #%d: %04d\n", s, carry);
			}
		}
	}

	return 0;
}
