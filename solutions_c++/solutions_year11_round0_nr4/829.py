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

int main()
{
fstream In("d-large.in", ios::in);
fstream Out("d-large.out", ios::out);

int tests;

In >> tests;

for(int h=0; h<tests; h++)
{

int N;

In >> N;

int ret = N;
for(int i=1; i<=N; i++)
{
	int temp;
	In >> temp;
	if(temp==i) ret--;
}
Out << "Case #" << h+1 << ": " << ret << endl;

}

In.close();

Out.close();

return 0;

}
 
