#include <vector>        
#include <map>        
#include <set>        
#include <deque>        
#include <algorithm>        
#include <utility>        
#include <sstream>        
#include <iostream>        
#include <cstdio>        
#include <cmath>        
#include <cstdlib>        

using namespace std;   

#define SZ(a) ((int)(a).size())   
#define pii pair<int, int>  
#define mp make_pair  
template<class A, class B> A convert(B x) {stringstream s; s << x; A r; s >> r; return r;}

int main()
{
	int testCnt;
	cin >> testCnt;
	for (int T = 0; T < testCnt; ++T)
	{
		string s, ts;
		cin >> s;
		ts = s;
		next_permutation(s.begin(), s.end());
		if (s <= ts)
		{
			sort(ts.begin(), ts.end());
			string z = "0";
			while (ts[0] == '0') { z += "0"; ts.erase(0, 1); }
			
			s = ts.substr(0, 1) + z + ts.substr(1);
		}
		cout << "Case #" << T+1 << ": " << s << endl;
	}
	/*cout << "500\n";
	for (int T = 0; T < 500; ++T)
	{
		cout << "98765432100000000000\n";
	}*/
	return 0;
}