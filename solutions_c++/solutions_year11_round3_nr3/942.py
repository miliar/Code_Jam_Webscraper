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

//Google Code Jam 2011 Round 1C, Task A code.google.com/codejam
//Disable warning messages C4996.
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
	const long long nmin=1, nmax=100, xmin=1, xmax=10000;
	long long test, cases, n, m, mt, res, rt, i, j, k, t, ax, bx, x, x0, x1;
	//char ch;
	//string sres[2]={"Possible", "Broken"};
	//string s, st, st0, st1;
	//long double dt;

	if(INPUT_FROM) from.open("test.txt");
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	//list<char> lc;
	vector<long long> v;
	//deque<vector<long long> > dq;
	//map<string, long long> ms;
	//map<long long, vector<string> > mi;
	//map<long long, vector<string> >::iterator it;
	//typedef map<string, long long>::const_iterator CI;
	//list<char>::iterator it, it0, it1;

	fromc>>cases;

	for(test=1;test<=cases;test++){
		fromc>>n>>x0>>x1;
		v.resize(n);

		for(i=0;i<n;i++) fromc>>v[i];

		res=0;
		ax=0;
		for(x=x0;(x<=x1)&&(ax==0);x++){
			bx=0;
			for(i=0;(i<n)&&(bx==0);i++){
				if((v[i]%x!=0)&&(x%v[i]!=0)) bx=1;
			}
			ax=1-bx;
			if(ax==1) res=x;
		}

		cout<<"Case #"<<test<<": ";
		if(ax==0) cout<<"NO"<<endl;
		else cout<<res<<endl;

		v.clear();
	}

	return 0;
}


