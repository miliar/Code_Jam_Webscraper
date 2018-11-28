#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>

using namespace std;
vector <string> Engines, Q;
vector <vector <bool> > V;
vector <vector <int> > M;

int LeastSwitches(int QInd, int CurEng)
{




	if (QInd >= Q.size())
		return 0;

	if (V[QInd][CurEng])
		return M[QInd][CurEng];

	V[QInd][CurEng] = true;

	if (Q[QInd] != Engines[CurEng])
	{
		return M[QInd][CurEng] = LeastSwitches(QInd +1 , CurEng);
	}
	else
	{
		int L = INT_MAX;
		for (int i=0; i < Engines.size(); ++i)
		{
			if (Engines[i] != Q[QInd])
			{
				L <?= LeastSwitches(QInd + 1, i);
			}
		}
		return M[QInd][CurEng] = 1 + L;
	}
}

int main()
{
	char c;
	ifstream cin("A.in1");
	ofstream cout("A.out");
	int nCases;
	string S;
	{
		getline(cin, S);
		stringstream ss(S);
		ss >> nCases;
	}

	//cin >> nCases;
	//cin >> c;

	for (int iCase = 1; iCase <= nCases; ++iCase)
	{
		Engines.clear();
		Q.clear();

		int nEngines, nQ;

		{
			getline(cin, S);
			stringstream ss(S);
			ss >> nEngines;
		}


		for (int i=0; i < nEngines; ++i)
		{
			getline(cin, S);
			//cout << S <<endl;
			Engines.push_back(S);
		}

		{
			getline(cin, S);
			stringstream ss(S);
			ss >> nQ;
		}

		//cin >> nQ;
		for (int i=0; i < nQ; ++i)
		{
			getline(cin, S);
			//cout << S <<endl;
			Q.push_back(S);
		}

		V.clear();
		M.clear();
		V.resize(nQ, vector< bool> (nEngines, false));
		M.resize(nQ, vector< int> (nEngines, 0));

		int L = INT_MAX;
		for (int i=0; i < nEngines; ++i)
		{
			L <?= LeastSwitches(0, i);
		}
		cout << "Case #"<< iCase <<": " << L<<endl;

	}
	return 0;
}
