#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <string>
#include <algorithm>
#include <iterator>
#include <functional>
#include <stdlib.h>

using namespace std;

#define repp(I, Start, End)		for(I = Start; I < End; ++I)
#define rep(I, End)				for( ; I < End; ++I)
#define irep(I, End)			for( ; I != End; ++I)
#define idef(Typ, No, Var)		Typ::const_iterator ite##No = Var.begin();	Typ::const_iterator iteEnd##No = Var.end();
#define it(Typ, No, Var)		idef(Typ, No, Var)	irep(ite##No, iteEnd##No)




int main()
{
	ifstream ifs("A-large.in");
	ofstream ofs("output.txt");
	string sLine = "";
	bool bFirstLineRead = false;
	int iTestCaseCount = 0;
	int iTestCaseNo = 0;
	while(getline(ifs, sLine))
	{
		istringstream ss(sLine);
		if(!bFirstLineRead)
		{
			ss >> iTestCaseCount;
			bFirstLineRead = true;
			continue;
		}
		++iTestCaseNo;
		if(iTestCaseNo > iTestCaseCount)
			break;

		int n;
		ss>>n;
		int i;
		int plays[100][100];
		int stats[100][2];
		vector<int> opponents[100];
		double owp[100];
		repp(i, 0, n)
		{
			getline(ifs, sLine);
			int j;
			int played = 0;
			int wins = 0;
			repp(j, 0, n)
			{
				if('0' == sLine[j])
				{
					plays[i][j] = 0;
					++played;
					opponents[i].push_back(j);
				}
				else if('1' == sLine[j])
				{
					plays[i][j] = 1;
					++played;
					++wins;
					opponents[i].push_back(j);
				}
				else
				{
					plays[i][j] = -1;
				}
			}
			stats[i][0] = wins;
			stats[i][1] = played;
		}

		ofs << "Case #" << iTestCaseNo << ":" << endl;

		repp(i, 0, n)
		{
			vector<int>::iterator it = opponents[i].begin();
			double sum = 0.0;
			for( ; it != opponents[i].end(); ++it)
			{
				int w = (plays[*it][i] == 1) ? (stats[*it][0] - 1) : (stats[*it][0]);
				int p = stats[*it][1] - 1;
				sum += ((double)w) / p;
			}
			owp[i] = (sum / opponents[i].size());
		}

		repp(i, 0, n)
		{
			double oowp = 0;
			vector<int>::iterator it = opponents[i].begin();
			for( ; it != opponents[i].end(); ++it)
			{
				oowp += (owp[*it]);
			}
			oowp /= opponents[i].size();

			double val = (0.25 * ((double)(stats[i][0]) / stats[i][1])) + (0.5 * owp[i]) + (0.25 * oowp);
			char zz[25];
			sprintf(zz, "%.12f", val);
			ofs<<zz<<endl;
		}
	}
}