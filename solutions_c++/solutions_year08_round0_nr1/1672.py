#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using std::vector;
using std::string;
using std::cin;
using std::cout;

int analyze_queries(const vector<string> & vS, const vector<string>::const_iterator & beginQ, const vector<string>::const_iterator & endQ)
{
	int nSwitches = 0;
	int record_distance = 0;
	for (vector<string>::const_iterator is = vS.begin(); is != vS.end(); ++is)
	{
		vector<string>::const_iterator q = std::find(beginQ, endQ, *is);
		if (q == endQ)
			return 0;
		int distance = q - beginQ;
		if (distance > record_distance)
			record_distance = distance;
	}
	nSwitches = 1 + analyze_queries(vS, beginQ + record_distance, endQ);
	return nSwitches;
}

int main()
{
	int nCases = 0;

	cin >> nCases;

	for (int ic = 0; ic < nCases; ++ ic)
	{
		int nS = 0;
		cin >> nS; cin.ignore(1);

		vector<string> vS;
		vS.reserve(nS);
		for (int is = 0; is < nS; ++is)
		{
			char buff[128] = {0};
			cin.getline(buff, 100);
			vS.push_back(buff);
		}

		int nQ = 0;
		cin >> nQ; cin.ignore(1);
		vector<string> vQ;
		vQ.reserve(nQ);
		for (int iq = 0; iq < nQ; ++iq)
		{
			char buff[101] = {0};
			cin.getline(buff, 100);
			vQ.push_back(buff);
		}

		int nY = analyze_queries(vS, vQ.begin(), vQ.end());

		cout << "Case #" << (ic+1) << ": " << nY << std::endl;
	}

	return 0;
}