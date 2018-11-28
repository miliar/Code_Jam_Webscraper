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

fstream In("c-large.in", ios::in);
fstream Out("c-large.out", ios::out);

int tests;

In >> tests;

for(int h=0; h<tests; h++)
{
int N;
In >> N;
int total = 0;
int t2 = 0;
int low = 1e8;
int temp = 0;
for(int i=0; i<N; i++)
{
In >> temp;
t2 += temp;
low = min(low, temp);
total ^= temp;
}


Out << "Case #" << h+1 << ": ";
if(total)
Out << "NO" << endl;
else
Out << t2-low << endl;
}

In.close();

Out.close();

return 0;

}
 
