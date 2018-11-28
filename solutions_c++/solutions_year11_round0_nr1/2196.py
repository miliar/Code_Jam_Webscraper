#include <algorithm>
#include <fstream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)

//vector<int> v;
//for(vector<int>::iterator it = v.begin(), end = v.end(); it != end; ++it)
//{
//}

int main(int argc, char* argv[])
{
	ifstream in("in");
	ofstream out("out");

	int T = 0;
	in >> T;

	REP (t, T)
	{
		int n = 0;
		in >> n;

		int total = 0, local = 0;
		int O = 1, B = 1;
		char prev = 'U';
		REP (i, n)
		{
			char ch = 0;
			int x = 0;
			in >> ch >> x;

			int temp = 0;
			if (ch == 'O')
			{
				if (prev == ch)
					temp = abs(x-O)+1;
				else
					temp = (abs(x-O)-local < 0) ? 1 : abs(x-O)-local+1;

				O = x;
			} 
			else
			{
				if (prev == ch)
					temp = abs(x-B)+1;
				else
					temp = (abs(x-B)-local < 0) ? 1 : abs(x-B)-local+1;
				B = x;
			}

			if (prev == ch)
				local += temp;
			else
				local = temp;
			prev = ch;

			total += temp;
		}

		out << "Case #" << t+1 << ": " << total << "\n";	
	}

	in.close();
	out.close();

	return 0;
}
