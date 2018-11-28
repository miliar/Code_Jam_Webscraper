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

//Google Code Jam 2011 Qualification Round, Task A code.google.com/codejam
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
	const long long nmin=1, nmax=100;
	long long test, cases, n, m, mt, res, rt, i, j, k, t, t0, t1, ax, x, x0, x1;
	char ch;
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
	//map<vector<long long>, long long > vi;
	//typedef map<string, long long>::const_iterator CI;
	//list<char>::iterator it, it0, it1;

	fromc>>cases;

	for(test=1;test<=cases;test++){
		fromc>>n;

		x0=x1=1;
		res=t0=t1=0;
		for(i=0;i<n;i++){
			fromc>>ch>>x;
			if(ch=='O'){
				t=(x>x0)?(x-x0):(x0-x);
				t=(t>t0)?(t-t0):0;
				t1+=t+1;
				t0=0;
				x0=x;
			}else{
				t=(x>x1)?(x-x1):(x1-x);
				t=(t>t1)?(t-t1):0;
				t0+=t+1;
				t1=0;
				x1=x;
			}
			res+=t+1;
		}

		cout<<"Case #"<<test<<": "<<res<<endl;
	}

	return 0;
}