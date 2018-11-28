#pragma warning(disable : 4996)
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#define F(i,a) for(int i=0;i<int((a).size());i++)
#define INF 1000000000
#define MP make_pair
#define ALL(a) (a).begin(), (a).end()
#define X first
#define Y second
#define LL long long
#define LD long double
#define SQR(a) ((a)*(a))
using namespace std;

int main()
{
#ifndef ONLINE_JUDGE 
	freopen("input.txt","r",stdin); 
	freopen("output.txt","w",stdout);
#endif
	int t;
	cin >> t;
	for (int iii=1; iii<=t; ++iii)
	{
		int n;
		cin >> n;
		vector<int> o,b,obef,bbef;
		while (n--)
		{
			int num;
			char ch;
			cin >> ch >> num;
			if (ch=='O')
				o.push_back(num), obef.push_back((int)b.size()-1);
			else
				b.push_back(num), bbef.push_back((int)o.size()-1);
		}
		vector<int> obut(101),bbut(101);
		int op=1,bp=1;
		bool odone=(o.size()==0), bdone=(b.size()==0);
		int oind=0,bind=0,time=0;
		while (!odone || !bdone)
		{
			++time;
			if (!odone)
			{
				if (oind==o.size())
					odone=true;
				else if (op!=o[oind]/* || op==o[oind] && obut[op]!=0 && time!=1*/)
					op+=(o[oind]-op)/abs(o[oind]-op);
				else if (op==o[oind] && bind>obef[oind])
					obut[op]=time, ++oind;
			}
			if (!bdone)
			{
				if (bind==b.size())
					bdone=true;
				else if (bp!=b[bind]/* || bp==b[bind] && bbut[bp]!=0 && time!=1*/)
					bp+=(b[bind]-bp)/abs(b[bind]-bp);
				else if (bp==b[bind] && oind>bbef[bind] && (bbef[bind]==-1 || obut[o[bbef[bind]]]!=time))
					bbut[bp]=time, ++bind;
			}
		}
		cout << "Case #" << iii << ": " << time-1 << endl;
	}
	return 0;
}
