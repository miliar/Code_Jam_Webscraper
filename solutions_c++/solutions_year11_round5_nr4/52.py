#include <iostream>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <deque>
#include <cstring>
#include <ctime>
#include <complex>

using namespace std;

#define MSG(a) cout << #a << " = " << a << endl;
#define FOR(a,start,end) for(int a = int(start); a < int(end); a++)
#define PB push_back

int main()
{
// 	ifstream fin("D-sample.in");
// 	ofstream fout("D-sample.out");
	ifstream fin("D-small-attempt1.in");
	ofstream fout("D-small-attempt1.out");
//	ifstream fin("D-large.in");
//	ofstream fout("D-large.out");

	int T;
	fin >> T;
	for(int trz = 0; trz < T; trz++)
	{
		fout << "Case #" << trz+1 << ": ";
		
		string s;
		fin >> s;
		
		MSG(s);
		
		long long baseNum = 0;
		vector<int> qns;
		FOR(i,0,s.size())
		{
			FOR(t,0,qns.size())
				qns[t]++;
			if(s[i] == '1')
				baseNum *= 2, baseNum++;
			else if(s[i] == '0')
				baseNum *= 2;
			else if(s[i] == '?')
			{
				baseNum *= 2;
				qns.PB(0);
			}
			
		}	
		
		long long ans = 0;
		
		FOR(t,0,(1<<qns.size()))
		{
			long long a = baseNum;
			FOR(p,0,qns.size())
			if((t>>p)%2)
				a += (1LL<<qns[p]);
			
			long long b = sqrt((double)a);
			while(b*b < a) b++;
			if(b*b == a)
			{
				ans = a;
				break;
			}
		}
		
		string ss;
		while(ans > 0)
		{
			ss = (char)('0'+ans%2) + ss;
			ans /=2;
		}
		fout << ss << endl;
		cout << ss << endl;
			
	}

	return 0;
}






