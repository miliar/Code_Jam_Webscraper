#include <fstream>
#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	ifstream inp("C-large.in", ifstream::in);
	ofstream outp("outputlarge.txt", ofstream::out);

	/**** Declare variables ***/

	int T, N, temp, sum;
	int res_xor;
	int min;
	int *array;
	float x;

	/******* Start looping ******/
	inp>>T;
	for (int i = 1; i <= T; i++)
	{
		sum = 0;
		res_xor = 0;

		inp>>N;
		cout<<"Case #"<<i<<": "<<N<<endl;
		array = new int[N];

		inp>>temp;

		array[0] = temp;
		res_xor = res_xor ^ temp;
		sum += temp;
		min = temp;

		for (int j = 1; j < N; j++)
		{
			inp>>temp;
			array[j] = temp;
			sum += temp;
			res_xor = res_xor ^ temp;

			if (temp < min)
			{
				min = temp;
			}
		}
		
		delete array;
		cout<<res_xor<<" "<<sum<<" "<<min<<endl;
		outp<<"Case #"<<i<<": ";
		if (res_xor == 0)
		{
			outp<<(sum - min);
		}
		else
		{
			outp<<"NO";
		}
		outp<<endl;
	}

	/****** End ********/
	return 0;
}
