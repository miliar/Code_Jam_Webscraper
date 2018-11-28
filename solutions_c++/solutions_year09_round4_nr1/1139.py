#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <fstream>
#include <iomanip>
#include <list>
using namespace std;
ifstream myin("A-large.in");
ofstream myout("out.out");
const int MAXN = 50;

int main()
{
	int T, N;
	//string mat[MAXN];
	myin >> T;
	for(int casei=1; casei<=T; ++casei)
	{
		myin >> N;
		list<int> rowTopestAim;
		unsigned int ans = 0;
		for(int i=0; i<N; ++i)
		{
			string aRow;
			myin >> aRow;
			int j = aRow.size()-1;
			while(j >= 0 && aRow[j] == '0')
			{
				--j;
			}
			rowTopestAim.push_back(j);
		}
		//vector<int> moved(N);
		if (N==1)
		{
			myout << "Case #" << casei << ": " << 0 << endl;
			continue;
		}
		list<int>::iterator it = rowTopestAim.begin();
		int curRow = 0;
		while(it != rowTopestAim.end())
		{
			while( (*it) > curRow )
			{
				++it;
			}
			ans += distance(rowTopestAim.begin(), it);
			rowTopestAim.erase(it);
			it = rowTopestAim.begin();
			++curRow;
		}
		myout << "Case #" << casei << ": " << ans << endl; //Case #1: 0
	}
	return 0;
}

