#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <deque>
#include <map>
#include <cstdlib>
using namespace std;

//Google Code Jam 2013 Qualification Round, Problem A code.google.com/codejam
//Disable warning messages C4996.
#pragma warning(disable:4996)

#define INPUT_FROM 0
#if INPUT_FROM
#define fromc from
#else
#define fromc cin
#endif

//long long fr(vector<long long>&, long long);

int main(int argc, char **argv)
{
	//ifstream from;
	const int nmin=1, nmax=4;
	int test, cases, n, m, mt, res, rt, i, j, k, t, ax, a;
	int i0, i1, i2;
	char ch;
	//string sres[2]={"YES", "NO"};
	string sres[4]={"O won", "X won", "Draw", "Game has not completed"};
	//string s, st, sr;
	//long double dt;

	//if(INPUT_FROM) from.open("test.txt");
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	static char vv[nmax][nmax];
	//vector<long long> v;
	//deque<long long> dq;
	//map<char, char> mc;
	//map<long long, long long>::iterator it;
	//typedef map<string, long long>::const_iterator CI;


	//scanf("%ld\n", &cases);
	fromc>>cases;
	for(test=1;test<=cases;test++){
		ax=2;
		for(i=0;i<nmax;i++){
			for(j=0;j<nmax;j++){
				fromc>>ch;
				vv[i][j]=ch;
				if(ch=='.') ax=3;
			}
		}

		for(i=0;(i<nmax)&&(ax>=2);i++){
			i0=i1=i2=0;
			for(j=0;j<nmax;j++){
				ch=vv[i][j];
				if(ch=='T') i2=1;
				else if(ch=='O') i0++;
				else if(ch=='X') i1++;
			}
			if(i2==1){
				if(i0==3) ax=0;
				else if(i1==3) ax=1;			
			}else{
				if(i0==4) ax=0;
				else if(i1==4) ax=1;
			}
		}

		for(i=0;(i<nmax)&&(ax>=2);i++){
			i0=i1=i2=0;
			for(j=0;j<nmax;j++){
				ch=vv[j][i];
				if(ch=='T') i2=1;
				else if(ch=='O') i0++;
				else if(ch=='X') i1++;
			}
			if(i2==1){
				if(i0==3) ax=0;
				else if(i1==3) ax=1;			
			}else{
				if(i0==4) ax=0;
				else if(i1==4) ax=1;
			}
		}
		
		i0=i1=i2=0;
		for(i=0;(i<nmax)&&(ax>=2);i++){
			ch=vv[i][i];
			if(ch=='T') i2=1;
			else if(ch=='O') i0++;
			else if(ch=='X') i1++;
		}
		if(i2==1){
			if(i0==3) ax=0;
			else if(i1==3) ax=1;			
		}else{
			if(i0==4) ax=0;
			else if(i1==4) ax=1;
		}

		i0=i1=i2=0;
		for(i=0;(i<nmax)&&(ax>=2);i++){
			ch=vv[i][nmax-i-1];
			if(ch=='T') i2=1;
			else if(ch=='O') i0++;
			else if(ch=='X') i1++;
		}
		if(i2==1){
			if(i0==3) ax=0;
			else if(i1==3) ax=1;			
		}else{
			if(i0==4) ax=0;
			else if(i1==4) ax=1;
		}

		cout<<"Case #"<<test<<": "<<sres[ax]<<endl;
	}

	return 0;
}

