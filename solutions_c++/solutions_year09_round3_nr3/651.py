#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
#include <string>
#include <math.h>

using namespace std;

long solve(long P, vector<long> &Qs, long begin, long end)
{
	if (begin > P || end < 1) return 0;
	long result = end - begin;
	bool finded = false;
	long minVal = 0xFFFF;
	for (unsigned int i = 0; i < Qs.size(); i++)
	{
		long sum = 0;
		if (Qs[i] >= begin && Qs[i] <= end)
		{
			finded = true;
			sum += solve(P, Qs, begin, Qs[i] - 1);
			sum += solve(P, Qs, Qs[i] + 1, end);
			if (sum < minVal) minVal = sum;
		}
	}
	if (!finded) return 0;
	else return result + minVal;
}

int main(int argc, char **argv)
{
	cout << "Round 1C. Problem C" << endl;
	char strInpFileName[1024];
	cout << "Input file name: ";
	cin >> strInpFileName;
	ifstream inpf(strInpFileName);
	if (!inpf) { cout << "Bad input file name" << endl; return 0; }
	ofstream outf("output.out");
	if (!outf) { cout << "Cannot open \"output.out\"" << endl; return 0; }

	int casesCount;
	inpf >> casesCount;

	for (int cc = 1; cc <= casesCount; cc++)
	{
		cout << "Case " << cc << " of " << casesCount << "...";
		long P, Q;
		inpf >> P >> Q;
		vector<long> Qs;
		long a;
		for (int i = 0; i < Q; i++)
		{
			inpf >> a;
			Qs.insert(Qs.end(), a);
		}
		sort(Qs.begin(), Qs.end());
		
		outf << "Case #" << cc << ": " << solve(P, Qs, 1, P) << endl;
		cout << "finished" << endl;
	}

	inpf.close();
	outf.close();
	return 0;
}