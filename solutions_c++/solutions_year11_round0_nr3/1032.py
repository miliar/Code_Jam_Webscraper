#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <deque>
#include <map>
#include <list>
#include <cstdlib>
using namespace std;

//Google Code Jam 2011 Qualification Round, Task C code.google.com/codejam
// Disable warning messages C4996.
//#pragma warning(disable:4996)

#define INPUT_FROM 0
#if INPUT_FROM
#define fromc from
#else
#define fromc cin
#endif

//long long fr(vector<long long>&, long long);

int main(int argc, char **argv)
{
	ifstream from;
	const long long nmin=2, nmax=1000, cmin=2, cmax=1000000;
	long long test, cases, n, m, mt, res, rt, i, j, k, t, ax, x0, x1;
	//char ch;
	//string sres[2]={"N", "Y"};
	//string s, st;
	//long double dt;

	if(INPUT_FROM) from.open("test.txt");
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	//list<char> lc;
	//vector<long long> v;
	//vector<vector<char> > vc(n);
	//deque<vector<long long> > dq;
	//map<long long, long long> mi;
	//typedef map<string, long long>::const_iterator CI;
	//list<char>::iterator it, it0, it1;

	fromc>>cases;

	for(test=1;test<=cases;test++){
		fromc>>n;
		x0=cmax+1;
		res=x1=0;
		for(i=0;i<n;i++){
			fromc>>rt;
			x1+=rt;
			x0=(rt<x0)?rt:x0;
			res^=rt;
		}
		x1-=x0;
		res=(res==0)?x1:0;

		cout<<"Case #"<<test<<": ";
		if(res==0) cout<<"NO"<<endl;
		else cout<<res<<endl;
	}

	return 0;
}