#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <fstream>
#include <cmath>
#include <sstream>
using namespace std;

/**
* 1 => 8 in non-surprising.
* 2 => 8 not even in surprising. so, no need to consider.
* 3 => 8 in surprising.
*/
int cat(int n, int P)
{
	int q = n/3;
	int r = n % 3;

	//cout << n << " --> ";
	if(r == 0)
	{
		if(q >= P)
			return 1;

		if(q+1 >= P && q-1 >= 0)
			return 3;

		//q is guaranteed to be 6 or below and nos can be 5,6,7 at best
		return 2;
		//cout << "(" << q << "," << q << "," << q << ") or (" << q-1 << "," << q << "," << q+1 << ")";
	}
	else if (r == 1)
	{
		if(q+1 >= P)
		{ 
			return 1;
		}
	
		return 2;

		//cout << "(" << q << "," << q << "," << (q+1) << ") or (" << q-1 << "," << q+1 << "," << q+1 << ")";
	}
	else
	{
		/*n = 29
			9,10,10
			9,9,11
			
		q=9,P = 10*/
		if(q+1 >= P)
			return 1;

		if(q+2 >= P && q <= 8) //q <= 8 not reqd. but feeling scared
			return 3;

		return 2;
		//cout << "(" << q << "," << q+1 << "," << (q+1) << ") or (" << q << "," << q << "," << q+2 << ")";
	}

}

void find2()
{
	ifstream fin("D:\\jam.in");
	ofstream fout("D:\\jam.out");

	int T;
	
	string s;
	getline(fin, s);
	T = atoi(s.c_str());

	int ncase = 1;

	while(T-- > 0)
	{
		getline(fin, s);
		stringstream ss(s);

		int cnt = 0; //clear winners
		int sur = 0; //need surprising ones

		int N, S, P;
		ss >> N >> S >> P;

		for(int i=0; i<N; ++i)
		{
			int n;
			ss >> n;

			switch(cat(n, P))
			{
			case 1:
				++cnt;
				break;

			case 2:
				break;

			case 3:
				++sur;
				break;
			}
		}

		int res = cnt + min(sur, S);
		fout << "Case #"<< ncase++ << ": " << res << endl;
	}
}