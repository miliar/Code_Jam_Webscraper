#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

#include <fstream>

using namespace std;

int o[100];
int b[100];
int cmds[100];
void main()
{
	ifstream f;
	f.open("A-large-attempt0.in");

	char l[1];
	int cases;
	f >> cases;
	f.getline(l, 1);

	ofstream out;
	out.open("A-large-attempt0.out");

	for (int i = 0; i < cases; ++i)
	{
		memset(b, 0, sizeof(b));
		memset(o, 0, sizeof(o));

		int but;
		f >> but;
		int c = 0;
		int cp = 0;
		int bp = 0;
		int op = 0;
		while (but-- > 0)
		{			
			char color;
			f >> color;
			int pos;
			f >> pos;

			if (color == 'B')
				b[bp++] = pos;
			else if (color =='O')
				o[op++] = pos;
			cmds[cp++] = color;
		}
	
		int mcp = cp;
		cp = 0;
		op = 1;
		bp = 1;
		int oi = 0, bi = 0;
		int sec = 0;

		while (cp < mcp)
		{
			bool pushed = false;
			if (op < o[oi])
				++op;
			else if (op > o[oi])
				--op;
			else if (cmds[cp] == 'O')
			{
				++oi;
				++cp;
				pushed = true;
			}

			if (bp < b[bi])
				++bp;
			else if (bp > b[bi])
				--bp;
			else if (cmds[cp] == 'B' && !pushed)
			{
				++bi;
				++cp;
			}

			++sec;
		}

		out << "Case #" << i+1 << ": " << sec << endl;
	}

	out.close();



}