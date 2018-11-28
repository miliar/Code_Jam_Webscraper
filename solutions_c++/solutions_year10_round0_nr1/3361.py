/*
 * main.cpp
 *
 *  Created on: 8/Mai/2010
 *      Author: Bisc8
 */

#include <iostream>
#include <vector>
#include <math.h>


using namespace std;

/*struct Snapper
{
	bool state; //false = OFF; true = ON
};*/

void print(vector<bool> snappers)
{
	for(unsigned int i = 0; i < snappers.size(); i++)
	{
		cout << snappers[i];
	}

	cout << endl;
}

bool light(vector<bool> snappers)
{
	bool result = true;

	for(unsigned int i=0; i < snappers.size(); i++)
		result = result && snappers[i];

	return result;
}
/*
bool problemA(unsigned int N,unsigned int K)
{
	vector<bool> snappers;

	for(unsigned int i = 0; i < N; i++)
	{
		bool b = false;
		snappers.push_back(b);
	}

	for(unsigned int k =0; k < K; k++)
	{
		//cout << "k" << endl;

		for(unsigned n =0; n < snappers.size(); n++)
		{
			//cout << "n" << endl;

			if(!snappers[n])
			{
				snappers[n] = true;

				for(int i = n; i != 0; i--)
					snappers[i-1] = false;

				break;
			}

			if((n == snappers.size() - 1) && n)
			{
				for(int i = n; i >= 0; i--)
					snappers[i] = false;
			}
		}
	}

	return light(snappers);
}*/


bool problemA(int N, int K)
{
	double exp = pow(2.0,N);
	double remainder = fmod(fabs(K - (exp - 1)),exp);

	if( remainder == 0)
		return true;
	else
		return false;
}

int main()
{
	int T,N,K;

	string filename = "A-large";
	freopen((filename+".in").c_str(), "r", stdin);
	freopen((filename+".out").c_str(), "w", stdout);

	cin >> T;

	for(int i = 0; i < T; i++)
	{
		cin >> N;
		cin >> K;

		cout << "Case #" << (i+1) << ": " << (problemA(N,K)? "ON" : "OFF") << endl;
	}

	return 0;
}
