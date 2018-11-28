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

//Google Code Jam 2011 Qualification Round, Task D code.google.com/codejam
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
	const long long nmin=2, nmax=1000;
	long long test, cases, n, m, mt, res, rt, i, j, k, t, ax;
	//char ch;
	//string sres[2]={"N", "Y"};
	//string s, st;
	long double dt;

	if(INPUT_FROM) from.open("test.txt");
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	//list<char> lc;
	vector<long long> v, colour;
	//vector<vector<char> > vc(n);
	//deque<vector<long long> > dq;
	//map<long long, long long> mi;
	//typedef map<string, long long>::const_iterator CI;
	//list<char>::iterator it, it0, it1;

	fromc>>cases;

	for(test=1;test<=cases;test++){
		fromc>>n;
		v.resize(n);
		colour.resize(n);
		for(i=0;i<n;i++){
			fromc>>rt;
			rt--;
			v[i]=rt;
			colour[i]=0;
		}
		res=i=0;
		while(i<n){
			while((i<n)&&(colour[i]!=0)) i++;
			if(i<n){
				colour[i]=1;
				j=v[i];
				rt=1;
				while(colour[j]==0){
					colour[j]=1;
					j=v[j];
					rt++;
				}
				if(rt>1) res+=rt;
			}
		}

		dt=1.0*res;
		cout.precision(6);
		cout<<"Case #"<<test<<": "<<fixed<<dt<<endl;

		v.clear();
		colour.clear();
	}

	return 0;
}