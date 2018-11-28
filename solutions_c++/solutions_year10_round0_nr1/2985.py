#include<iostream>
#include<vector>
using namespace std;

#include<math.h>
#include<stdio.h>

struct snapper {
	bool state;
	bool power;
};

int main()
{
	int num_cases;
	cin >> num_cases;

	for(int t = 0; t < num_cases; t++)
	{
		int n, k;
		cin >> n >> k;

		int num_turns = pow(2, n);

		if(k < num_turns-1)
			printf("Case #%d: OFF\n", t+1);
		else {
			k %= num_turns;

			if(k == num_turns-1)
				printf("Case #%d: ON\n", t+1);
			else printf("Case #%d: OFF\n", t+1);
		}
	}
}
