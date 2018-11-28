#include <iostream>
#include <string>

using namespace std;

bool check(int n, int m)
{
	char sn[8];
	char sm0[8];
	char sm1[8];

	itoa(n,sn,10);
	itoa(m,sm0,10);
	sm1[strlen(sm0)] = 0;

	int k;

	for(int i = 0; i < strlen(sn)-1; ++i)
	{
		if(i % 2 == 0)
		{
			for(int j = 0; j < strlen(sm0); ++j)
			{
				k = (j+1) % strlen(sm0);
				sm1[k] = sm0[j];
			}
			if(strcmp(sn,sm1)==0)
			{
				return true;
			}
		}
		else
		{
			for(int j = 0; j < strlen(sm0); ++j)
			{
				k = (j+1) % strlen(sm0);
				sm0[k] = sm1[j];
			}
			if(strcmp(sn,sm0)==0)
			{
				return true;
			}
		}
	}
	return false;
}

int main()
{
	int nr_cases = 0;
	char line[101];

	int A,B,n,m;

	cin >> nr_cases;
	cin.getline(line,101);	// skip past the endline

	for(int i = 0; i < nr_cases; ++i)
	{
		cin >> A >> B;
		int tally = 0;

		for(n = A; n < B; ++n)
		{
			for(m = n+1; m <= B; ++m)
			{
				if(m/n >= 10)
				{
					break;
				}
				if(check(n,m))
				{
					//cout << n << "\t" << m << endl;
					++tally;
				}
			}
		}

		
		cout << "Case #" << i+1 << ": " << tally << endl;
	}
	return 0;
}