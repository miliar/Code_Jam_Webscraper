#include<iostream>
#include<sstream>
#include<fstream>
#include<math.h>
#include<iomanip>
#include<vector>
#include<map>

using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define LARGE 1000000
#define PI 3.14159265358979323846



int main(int argc, char *argv[])
{
	
	int nCase;
	cin >> nCase;

	for (int numCases = 0; numCases < nCase; numCases++)
	{
		int P, K, L;
		cin >> P >> K >> L;
		vector<long long> freq;
			

		for (int i = 0; i < L; i++)
		{
			long long  f;
			cin >> f;
			freq.push_back(f);
		}
//cout << P << K << L << endl;
		sort(freq.begin(),freq.end(),greater<long long>());

		long long  sum = 0;
		vector<long long>::iterator it;
		for(it=freq.begin(); it!=freq.end();++it)
			sum+= *it;
//cout << sum << endl;
		if (P * K > sum)
			cout << "Case #" << numCases+1 << ": Impossible" << endl;
		else {

			long long sum2=0;
			vector<long long>::iterator it = freq.begin();
			bool getout = false;
			for (int j = 0; j < P; j++)
			{
				for (int i = 0; i < K; i++)
				{
					sum2 += *it * (j+1);
					if(freq.size() >1)
						it = freq.erase(it);
					else{
						getout = true;
						break;
					}
				}
				if (getout) break;
			}
			cout << "Case #" << numCases+1 << ": " << sum2 << endl;
		}
	}
	return 0;
}

