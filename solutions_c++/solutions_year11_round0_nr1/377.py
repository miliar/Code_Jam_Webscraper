#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <list>
#include <set>
#include <numeric>
#include <queue>
#include <stack>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
using namespace std;
typedef long long LL;

struct SCOPE
{
	int run(int Case)
	{
		int move;
		cin >> move;
		int otime=0;
		int	opos=1;
		int btime=0;
		int bpos=1;
		for(int i=0;i<move;i++){
			char c;
			int dest;
			cin >> c >> dest;
			if(c=='O'){
				otime=max(btime+1,otime+abs(opos-dest)+1);
				opos=dest;
			}
			else
			{
				btime=max(otime+1,btime+abs(bpos-dest)+1);
				bpos=dest;
			}
			//cout << c << ":" << dest << ", " << otime << ", " << opos << ", " << btime << ", " << bpos << endl;
		}
		cout << "Case #" << Case << ": " << max(otime,btime) << endl;
		return 0;
	}
};
int main() {
	int n;
	cin >> n;
	int Case=1;
	for (int i=0;i<n;i++) {
		SCOPE* pSCOPE = new SCOPE();
		if(pSCOPE->run(i+1)){
			return 0;
		}
		Case++;
		delete pSCOPE;
	}
}
