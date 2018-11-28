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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

////file selection
void SetInputFile()
{ char filename[32], infile[32], outfile[32]; scanf("%s", filename);
  strcpy(infile, filename); strcpy(outfile, filename); strcat(infile, ".in"); strcat(outfile, ".out");
  freopen(infile, "r", stdin); freopen(outfile, "w", stdout);
}

long test,tcounter;

int main()
{
    SetInputFile();
	
	long x,n,maxi;

	cin >> test;
	tcounter = 1;

	while(test--)
	{
		cin >> n;		
		long tt = 0; maxi = 0;
		long smallest = 9999999;
		while(n--)
		{
			cin >> x;
			
			maxi += x;
			if(x<smallest) smallest = x;
			tt = tt ^ x;
			
		}
		
		if(tt!=0)
			cout << "Case #"<< tcounter++<<": NO" << endl;
		else
		{
			cout << "Case #"<< tcounter++<<": " << (maxi - smallest) << endl;
		}
	}
    return 0;
}
