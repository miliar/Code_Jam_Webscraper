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


long long gcd(long long a, long long b)
{
	return a < b ? gcd(b, a) : b ? gcd(b, a%b) : a;
}

int main()
{

fstream In("a-large.in", ios::in);
fstream Out("a-large.out", ios::out);

int tests;

In >> tests;

for(int h=0; h<tests; h++)
{

long long N, PG, PD;

In >> N >> PD >> PG;

long long mintoday = 100/gcd(100, PD);

bool flag = true;

if(mintoday > N) flag = false;

if((PG==100 || PG==0) && PD != PG) flag = false;

Out << "Case #" << h+1 << ": " << (flag ? "Possible" : "Broken") << endl;

}

In.close();

Out.close();

return 0;

}
 
