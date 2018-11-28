#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int T;
	int n, k;
	cin >> T;
	for(int i=0; i<T; i++)
	{
		cin >> n >> k;
		bool on = true;
		for(int j=0; j<n; j++)
			if ((k&(1 << j)) == 0)
				on = false;
		printf("Case #%d: ", i+1);
		if (on)
			printf("ON\n");
		else
			printf("OFF\n");
	}
}

