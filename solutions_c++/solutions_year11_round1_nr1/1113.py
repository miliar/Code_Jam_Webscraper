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

//Google Code Jam 2011 Round 1A, Task A code.google.com/codejam
// Disable warning messages C4996.
//#pragma warning(disable:4996)

#define INPUT_FROM 0
#if INPUT_FROM
#define fromc from
#else
#define fromc cin
#endif

//long long fr(vector<long long>&, long long);
long long euclid(long long, long long); 

int main(int argc, char **argv)
{
	ifstream from;
	const long long nmin=1, nmax=1000000000000000;
	long long test, cases, n, m, mt, res, rt, i, j, k, t, ax, pd, pg, a0, a1;
	//char ch;
	string sres[2]={"Possible", "Broken"};
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
		fromc>>n>>pd>>pg;

		a0=euclid(100, pd);
		//a1=euclid(100, pg);

		res=0;

		if(pd>0){
			if(n/(100/a0)==0) res=1;
			else if((pg==100)&&(pd<100)) res=1;
			else if((pd>0)&&(pg==0)) res=1;
		}else if((pd==0)&&(pg==100)) res=1;

		cout<<"Case #"<<test<<": "<<sres[res]<<endl;
	}

	return 0;
}

long long euclid(long long a, long long b){ 
	long long r, r0, r1, x, x0, x1, y, y0, y1, q; 
 
	r0=r=a; 
	x0=x=1; 
	y0=y=0; 
	r1=b; 
	x1=0; 
	y1=1; 
	while(r1!=0){ 
		q=r/r1; 
		r0=r1; 
		x0=x1; 
		y0=y1; 
		r1=r-q*r1; 
		x1=x-q*x1; 
		y1=y-q*y1; 
		r=r0; 
		x=x0; 
		y=y0; 
		//(r,x,y,r1,x1,y1)=(r1,x1,y1,r-qr1,x-qx1,y-qy1) 
	} 
	return r0; 
} 