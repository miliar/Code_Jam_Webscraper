#include <iostream>

using namespace std;

//rules:
//(n, m) with A =< n < m =< B
//largest dataset: 1 =< A =< B =< 2000000. (only 7 digits)

int main()
{	
	int tt = 0;
	int A = 0, B = 0, count = 0;
	const int MAX_DIGITS = 8;

	cin >> tt;
	for (int t = 1; t <= tt; ++t)
	{
		A = B = count = 0;
		cin >> A >> B;
		for (int n = A; n < B; ++n)
		{
			char str_n[MAX_DIGITS * 2] = {0};
			char *pstr_n8 = str_n + MAX_DIGITS;
			int m = 0;
			itoa(n, pstr_n8, 10);
			int len = strlen(pstr_n8);
			int len2 = len;
			int array_m[MAX_DIGITS] = {0};

			for (int x = 1; x < len; ++x)
			{
				str_n[8 - x] = pstr_n8[--len2]; //shift the digits to front
				pstr_n8[len2] = 0;
				m = atoi(str_n + (8 - x));

				if ((n < m) && (m <= B)) 
				{
					bool duplicate = false;
					//to avoid duplicacy, in case like: 1212,2121 - 1212,1212 - 1212,2121
					int y = MAX_DIGITS;
					for (int y = 0; y < MAX_DIGITS; ++y)
					{
						if (array_m[y] == m)
						{
							duplicate = true;
							break;
						}
					}					
					if (!duplicate)
						++count;
				}
				array_m[x-1] = m;
			}
		}
		cout << "Case #" << t << ": " << count << endl;
	} 
	return 0;
}