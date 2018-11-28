#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <conio.h>

using namespace std;


int main()
{
	ifstream input("A-small-attempt0.in");
	ofstream output("A-small-attempt0.out");
	long long T, N, K, count=0, val=0;
	input >> T;
	for (int a=0; a < T; a++)
	{
		input >> N;
		input >> K;
		val = (long long) pow((double) 2, (double) N);
		if (K > val)
			count = K % val;
		else count = K;

		vector<bool> values;
    	for (long long i=0; i < N; i++)
	    {
			values.push_back(false);
		}
		
		for (long long i=1; i <= count; i++)
		{
			long long j=0;
			while (values[j] == true)
			{
				values[j] = false; j++;
			}
			values[j] = true;
		}

        bool state = true;
        for (long long i=0; i < values.size(); i++)
        {
            if (values[i] == false)
            { state = false; break;}
        }
		output << "Case #" << a+1<< ": ";
//		cout << "Case #" << a+1<< endl;
/*		for (long long i=0; i< values.size(); i++)
		{
			if (values[i] == true)
				cout << "1 ";
			else cout << "0 ";
		}
		cout << endl;*/
		if (state == true)
        output << "ON" << endl;
        else output << "OFF" << endl; 
	}
	system("PAUSE");
	return 0;
}
