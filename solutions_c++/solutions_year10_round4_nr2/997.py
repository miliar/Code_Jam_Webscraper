/*
 * Google Code Jam template :-)
 */

#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
//#include <ctype.h>
//#include <assert.h>
//#include <math.h>
//#include <set>
//#include <map>

using namespace std;

typedef signed long long idx;


void solve(const idx t)
{
    idx P;
    cin >> P;
    idx powP = 1<<P;
    idx m[powP], next[powP];
    string nulStr;
    idx price = 0;


    for(idx i=0; i<powP; ++i)
    {
	cin >> m[i];
    }
    for(idx i=0; i<=P; ++i) getline(cin,nulStr);


    while(powP)
    {
	powP >>= 1;
	for(idx j=0; j<powP; ++j)
	{
	    idx a=m[j*2], b=m[j*2+1];
	    if (a == 0 || b == 0)
	    {
		++price;
		next[j] = 0;
	    }
	    else
	    {
		next[j] = min(a-1,b-1);
	    }
//	    cerr << "A=" << a << ", B=" << b << ", next="<< next[j] << endl;
	}
//	cerr << "it" <<endl;
	for (idx j=0; j<powP; ++j)
	{
	    m[j] = next[j];
	}
    }

    cout << "Case #" << t << ": " << price << endl;
}

int main(void)
{
    idx T;

    cin >> T;
    for(idx t=1; t<=T; ++t) solve(t);

    return 0;
}
