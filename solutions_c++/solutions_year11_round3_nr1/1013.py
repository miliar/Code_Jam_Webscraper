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
	const long long nmmin=1, nmmax=50;
	long long test, cases, n, m, mt, res, rt, i, j, j0, j1, k, t, ax;
	char ch;
	//string sres[2]={"Possible", "Broken"};
	//string s, st, st0, st1;
	//long double dt;

	if(INPUT_FROM) from.open("test.txt");
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	//list<char> lc;
	vector<vector<char> > v;
	//deque<vector<long long> > dq;
	//map<string, long long> ms;
	//map<long long, vector<string> > mi;
	//map<long long, vector<string> >::iterator it;
	//typedef map<string, long long>::const_iterator CI;
	//list<char>::iterator it, it0, it1;

	fromc>>cases;

	for(test=1;test<=cases;test++){
		fromc>>n>>m;
		v.resize(n);

		for(i=0;i<n;i++) v[i].resize(m);

		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				fromc>>v[i][j];
			}
		}

		ax=0;
		for(i=0;(i<n)&&(ax==0);i++){
			j0=j1=0;
			while((j1<m)&&(ax==0)){
				while((j1<m)&&(v[i][j1]!='#')) j1++;
				if((j1<m)&&(v[i][j1]=='#')){
					j0=j1;
					j1++;
					while((j1<m)&&(v[i][j1]=='#')) j1++;
					if((j1-j0)%2==1) ax=1;
				}
			}
		}

		for(i=0;(i<m)&&(ax==0);i++){
			j0=j1=0;
			while((j1<n)&&(ax==0)){
				while((j1<n)&&(v[j1][i]!='#')) j1++;
				if((j1<n)&&(v[j1][i]=='#')){
					j0=j1;
					j1++;
					while((j1<n)&&(v[j1][i]=='#')) j1++;
					if((j1-j0)%2==1) ax=1;
				}
			}
		}

		if(ax==0){
			for(i=0;i<n;i++){
				for(j=0;j<m;j++){
					if(v[i][j]=='#'){
						v[i][j]='/';
						v[i][j+1]='\\';
						v[i+1][j]='\\';
						v[i+1][j+1]='/';
					}
				}
			}
		}

		cout<<"Case #"<<test<<":"<<endl;
		if(ax==1) cout<<"Impossible"<<endl;
		else{
			for(i=0;i<n;i++){
				for(j=0;j<m;j++){
					cout<<v[i][j];
				}
				cout<<endl;
			}
		}

		v.clear();
	}

	return 0;
}
