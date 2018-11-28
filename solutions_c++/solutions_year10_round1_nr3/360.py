#include <string>       
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

int main()
{

fstream In("c-small.in", ios::in);
fstream Out("c-small.out", ios::out);

int tests;

In >> tests;

for(int h=0; h<tests; h++)
{
int A1, A2, B1, B2;

In >> A1 >> A2 >> B1 >> B2;
int ret = 0;
for(int i=A1; i<=A2; i++)
for(int j=B1; j<=B2; j++)
{
	int cur1 = i, cur2 = j, curp = 1;
	if(cur1 < cur2) swap(cur1, cur2);

	while(true)
	{	if(cur1 < cur2) swap(cur1, cur2);
		if(cur1==cur2) {curp = 1-curp; break;}
		if(cur1 >= 2*cur2) break;
		cur1 -= cur2;
		curp = 1-curp;
	}
	ret += curp;
}
	

Out << "Case #" << h+1 << ": " << ret << endl;

}

In.close();

Out.close();

return 0;

}
 
