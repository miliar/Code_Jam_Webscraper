#include <string.h>       
#include <vector>       
#include <set>       
#include <map>       
#include <algorithm>       
#include <math.h>       
#include <sstream>       
#include <ctype.h>       
#include <queue>       
#include <stack>       
#include <iostream> 
#include <gmp.h>	// if GMP is not allowed, I apologize
#include <fstream>
using namespace std;

int curtime = 0;

int BT = 0, BX = 1, OT = 0, OX = 1;

int process(char C, int b)
{
	if(C == 'B')
	{
		curtime = max(curtime, BT + abs(BX-b) );
		curtime++;
		BX = b;
		BT = curtime;
	}
	else
	{
		curtime = max(curtime, OT + abs(OX-b) );
		curtime++;
		OX = b;
		OT = curtime;
	}
}
int main()
{

fstream In("a-large.in", ios::in);
fstream Out("a-large.out", ios::out);

int tests;

In >> tests;

for(int h=0; h<tests; h++)
{
curtime = 0;

BT = 0, BX = 1, OT = 0, OX = 1;

int N;

In >> N;

for(int i=0; i<N; i++)
{
char c; int b;
In >> c >> b;

process(c, b);

}
Out << "Case #" << h+1 << ": " << curtime << endl;

}

In.close();

Out.close();

return 0;

}
 
