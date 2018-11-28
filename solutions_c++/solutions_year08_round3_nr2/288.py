#include<iostream>
#include<cstring>

using namespace std;

int main()
{
	int N;
	cin >> N;

	for(int n=1; n <= N; ++n)
	{
		char digits[41];
		cin >> digits;

		int D = int(strlen(digits));

		char str[80]={digits[0] - '0'};

		for(int i=1; i < D; ++i)
		{
			str[2 * i - 1] = '.';
			str[2 * i] = digits[i] - '0';
		}

		unsigned long long ugly = 0;

		int j;

		do
		{
			long long num = str[0];

			for(j = 1; j < 2 * D - 1 && str[j] == '.'; j+=2)
				num = num * 10 + str[j + 1];

			while(j < 2 * D - 1)
			{
				char op = str[j];

				long long tmp = str[++j];

				for(++j; j < 2 * D - 1 && str[j] == '.'; j+=2)
					tmp = tmp * 10 + str[j + 1];

				if( op == '+' )
					num += tmp;
				else
					num -= tmp;
			}

			if( num < 0 )
				num = -num;

			if( num % 2 == 0 ||  num % 3 == 0 ||  num % 5 == 0 ||  num % 7 == 0 )
				++ugly;

			for(j = 2 * D - 3; j > 0; j -= 2)
			{
				if(str[j] == '.')
				{
					str[j] = '+';
					break;
				}

				if(str[j] == '+')
				{
					str[j] = '-';
					break;
				}

				str[j] = '.';
			}
		}
		while(j > 0);

		cout << "Case #" << n << ": " << ugly << endl;
	}

	return 0;
}