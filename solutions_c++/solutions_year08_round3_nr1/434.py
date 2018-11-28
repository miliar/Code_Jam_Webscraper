
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <iostream>
#include <algorithm>
#include <conio.h>
using namespace std;

vector<long> letters;
long long P, K, L;

void main()
{
	ifstream inf("A-large.in");		//large
	ofstream outf("A-large.out");

	long long N;
	inf >> N;
	for (long long time=0; time <N; time++)
	{
		letters.clear();
		inf >> P >> K >> L;
		for (long long i=0; i<L; i++)
		{
			long long t;
			inf >> t;
			letters.push_back(t);
		}
		sort(letters.begin(), letters.end());
		reverse(letters.begin(), letters.end());
	//	cout << letters[0] << endl;
		long long re = 0;
		long long wei = 1;
		long long index = 0;
		for (long long i=0; i<letters.size(); i++)
		{
			if (wei > P)
			{
				re = -1;
				break;
			}			
			re += letters[i] * wei;
			index++;
		//	cout << index << letters.end()-letters.begin() << endl;
			if (index == K)
			{
				index = 0;
				wei++;
			}
		}

		if (re == -1)
		{
			outf << "Case #" << time+1 << ": " << "Impossible" << endl;
		}
		else
		{
			outf << "Case #" << time+1 << ": " << re << endl;
		}

		cout << endl;
	}

	inf.close();
	outf.close();
	_getch();
}
