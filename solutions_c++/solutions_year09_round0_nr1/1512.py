#include <iostream>

using namespace std;

int main()
{
	int L, D, N;
	cin >> L >> D >> N;

	char words[D][L];
	for(int i = 0; i < D; i++)
		cin >> words[i];

	char test[(L + 2) * D];
	bool possible[D];
	for(int i = 0; i < N; i++)
	{
		cin >> test;
		for(int j = 0;j < D;j++)
			possible[j] = true;
		for(int j = 0, k = 0, l = 0;j < L;j++, k++, l++)
			if(test[k] == '(')
			{
				while(test[l] != ')')
					l++;
				for(int m = 0; m < D; m++)
				{
					bool verify = false;
					if(possible[m])
						for(int n = k + 1; n < l; n++)
							if(test[n] == words[m][j])
							{
								verify = true;
								break;
							}
					if(!verify)
						possible[m] = false;
				}
				k = l;
			}
			else
			{
				for(int m = 0; m < D; m++)
					if(possible[m] && test[k] != words[m][j])
						possible[m] = false;
			}

		int count = 0;
		for(int j = 0;j < D;j++)
			if(possible[j])
				count++;

		cout << "Case #" << i + 1 << ": " << count << endl;
	}
	return 0;
}
