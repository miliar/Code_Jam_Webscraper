/*
 * Google Code Jam template :-)
 */

#include <iostream>
#include <string>
#include <sstream>
//#include <algorithm>
#include <vector>
//#include <ctype.h>
//#include <assert.h>
//#include <math.h>
//#include <set>
//#include <map>

using namespace std;

typedef unsigned idx;
typedef unsigned long long dist;
typedef unsigned long long veloc;
typedef unsigned long long cas;
typedef int num;

template<class T> void line2list(string &str, vector<T> &v)
{
    istringstream ss(str,istringstream::in);
    T t;
    while (ss >> t)
    {
	v.push_back(t);
    }
}


void solve(const num t)
{
    num N, K;
    dist B;
    cas T;
    num succ=0, before=0, swaps=0;
    vector<veloc> vv;
    vector<dist> vx;
    string line;

    cin >> N >> K >> B >> T;
    getline(cin,line);
    getline(cin,line);
    line2list(line,vx);
    getline(cin,line);
    line2list(line,vv);

    for(num i=N; i>0 && succ<K; --i)
    {
	//if dorazi(i)
	if (vx[i-1] + vv[i-1]*T >= B)
	{
	    ++succ;
	    swaps += before;
	}
	else
	{
	    ++before;
	}
    }

    if (succ == K)
    {
	cout << "Case #" << t << ": " << swaps << endl;
    }
    else
    {
	cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
    }
}

int main(void)
{
    num C;

    cin >> C;
    for(num t=1; t<=C; ++t) solve(t);

    return 0;
}

