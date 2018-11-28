#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>
using namespace std;

ifstream fin("B.in");
ofstream fout("B.out");

int readtime(void)
{
	string s;
	fin >> s;
	int h, m;
	h = atoi(s.c_str());
	m = atoi(s.c_str()+3);
	return h*60+m;
}

void add(vector<int> &v, int val, int in)
{
	for (vector<int>::iterator it = v.begin() + in; it != v.end(); it++)
	{
		*it += val;
	}
}

int main(void)
{
	int N;
	fin >> N;
	for (int tn = 1; tn <= N; tn++)
	{
		int T, NA, NB;
		fin >> T >> NA >> NB;
		vector<int> arA, arB;
		vector<pair<int, int> > trA, trB;
		int resA, resB;
		resA = resB = 0;
		arA.resize(24*60+60);
		arB.resize(24*60+60);
		for (int i = 0; i < NA; i++)
		{
			int t1, t2;
			t1 = readtime();
			t2 = readtime();
			trA.push_back(make_pair(t1, t2));
		}
		for (int i = 0; i < NB; i++)
		{
			int t1, t2;
			t1 = readtime();
			t2 = readtime();
			trB.push_back(make_pair(t1, t2));
		}
		sort(trA.begin(), trA.end());
		sort(trB.begin(), trB.end());
		trA.push_back(make_pair(1000000, 1000000));
		trB.push_back(make_pair(1000000, 1000000));
		vector<pair<int, int> >::iterator iA, iB;
		iA = trA.begin();
		iB = trB.begin();
		while ((iA->first != 1000000) || (iB->first != 1000000))
		{
			if (iA->first  >  iB->first)
			{
				if (arB[iB->first] == 0)
				{
					resB ++;
				}
				else
				{
					add(arB, -1, iB->first);
				}
				add(arA, 1, iB->second + T);
				iB ++;
			} else
			{
				if (arA[iA->first] == 0)
				{
					resA ++;
				}
				else
				{
					add(arA, -1, iA->first);
				}
				add(arB, 1, iA->second + T);
				iA ++;
			}
		}
		fout << "Case #" << tn << ": " << resA << " " << resB << endl;
	}
	return 0;
}