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
	ifstream ifs("B-large.in");
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

		long long c, d;
		ss>>c;
		ss>>d;

		int i;
		long long pos = 0;
		long double tt = 0.0;
		repp(i, 0, c)
		{
			getline(ifs, sLine);
			istringstream ss2(sLine);
			long long p, v;
			ss2>>p;
			ss2>>v;
			long long dist = 0;
			if(0 == i)
			{
				dist = ((v - 1) * d);
				pos = (p + ((v-1)*d));
			}
			else
			{
				long long dif = p - pos;
				if(dif < d)
					dist += (d - dif);
				dist += ((v-1)*d);
				pos = p + dist;
			}
			
			

			long double t = (((long double)dist)) / 2;
			if(t > tt)
			{
				tt = t;
			}
			
		}

		char zz[25];
		sprintf(zz, "%.12f", tt);
		ofs << "Case #" << iTestCaseNo << ": " << zz << endl;
	}
}