#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <queue>
#include <set>
#include <cassert>
#include <cmath>
#include <algorithm>
typedef long long LL; 
using namespace std;
 
#define FOR(k,a,b) for(int k(a); k < (b); ++k)
#define REP(k,a) for(int k=0; k < (a); ++k)



int main()
{
	int testCaseCounter;
	cin >> testCaseCounter;
	for(int actTestCase=1;actTestCase<=testCaseCounter;++actTestCase)
	{
		int N;
		cin >> N;
		const int R=10001;
		vector<int> v(R,0);
		REP(i,N)
		{
			int tmp;
			cin>> tmp;
			++v[tmp];
		}
		int mx=N;
		REP(i,R)
		{
			while(v[i])
			{
				--v[i];
				int l=1;
				int j=i;
				while(j<R && v[j+1]>v[j])
				{
					++l;
					++j;
					--v[j];
				}
				mx=min(l,mx);
			}	
		}
		cout << "Case #" << actTestCase << ": "<< mx << endl;

	}
	return 0;
}
