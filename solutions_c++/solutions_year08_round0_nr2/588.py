#include <iostream>
#include <utility>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <functional>
#include <iomanip>
#include <math.h>
#include <sstream>
#include <locale>
#include <fstream>

using namespace std;


vector<int> depa,arrb;
vector<int> depb,arra;

int main()
{
	ifstream iFile("B-large.in");
	ofstream oFile("B-large.out");

	int n;
	iFile >> n;

	int cases = 1;
	for (;cases<=n;cases++)
	{
		//init
		depa.resize(0),arrb.resize(0);
		depb.resize(0),arra.resize(0);
		int t,na,nb,i,h1,m1,h2,m2,t1,t2;
		char c;

		//read
		iFile >> t >> na >> nb;
		for (i=0;i<na;i++)
		{
			iFile >> h1 >> c >> m1;
			iFile >> h2 >> c >> m2;
			t1 = h1*60 + m1;
			t2 = h2*60 + m2;
			depa.push_back(t1);
			arrb.push_back(t2+t);
		}
		for (i=0;i<nb;i++)
		{
			iFile >> h1 >> c >> m1;
			iFile >> h2 >> c >> m2;
			t1 = h1*60 + m1;
			t2 = h2*60 + m2;
			depb.push_back(t1);
			arra.push_back(t2+t);
		}

		//work
		int sa = 0, sb = 0;

		for (i=0;i<na;i++)
		{
			sort(depa.begin(),depa.end());
			if (arra.size()==0)
			{
				depa.erase(depa.begin());
				sa++;
			}
			else
			{
				sort(arra.begin(),arra.end());
				if (depa[0]>=arra[0])//ready
				{
					depa.erase(depa.begin());
					arra.erase(arra.begin());
				}
				else//need more
				{
					depa.erase(depa.begin());
					sa++;
				}
			}
		}

		for (i=0;i<nb;i++)
		{
			sort(depb.begin(),depb.end());
			if (arrb.size()==0)
			{
				depb.erase(depb.begin());
				sb++;
			}
            else
			{
				sort(arrb.begin(),arrb.end());

				if (depb[0]>=arrb[0])//ready
				{
					depb.erase(depb.begin());
					arrb.erase(arrb.begin());
				}
				else//need more
				{
					depb.erase(depb.begin());
					sb++;
				}
			}
		}

		oFile << "Case #" << cases << ": " << sa << " " << sb << endl;
	}

	
    
	



	return 0;
}

