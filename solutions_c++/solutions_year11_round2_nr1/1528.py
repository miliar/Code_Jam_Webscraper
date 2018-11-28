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

//Google Code Jam 2011 Round 1B, Task A code.google.com/codejam
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
	const long long nmin=3, nmax=100;
	long long test, cases, n, m, mt, res, rt, i, j, k, t, ax, x0, q, r;
	char ch;
	//string sres[2]={"Possible", "Broken"};
	//string s, st, st0, st1;
	long double dt;

	if(INPUT_FROM) from.open("test.txt");
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	//list<char> lc;
	vector<long double> owp, oowp, vr;
	vector<long long> wpm, wp, owpm;
	vector<vector<char> > v;
	//deque<vector<long long> > dq;
	//map<string, long long> ms;
	//map<long long, vector<string> > mi;
	//map<long long, vector<string> >::iterator it;
	//typedef map<string, long long>::const_iterator CI;
	//list<char>::iterator it, it0, it1;

	fromc>>cases;

	for(test=1;test<=cases;test++){
		fromc>>n;
		v.resize(n);
		wpm.resize(n);
		wp.resize(n);
		owpm.resize(n);
		owp.resize(n);
		oowp.resize(n);
		vr.resize(n);

		for(i=0;i<n;i++) v[i].resize(n);

		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				fromc>>v[i][j];
			}
		}

		for(i=0;i<n;i++){
			rt=0;
			m=0;
			for(j=0;j<n;j++){
				if(v[i][j]!='.'){
					m++;
					if(v[i][j]=='1') rt++;
				}
			}
			wpm[i]=m;
			wp[i]=rt;
		}

		for(i=0;i<n;i++){
			dt=0.0;
			for(j=0;j<n;j++){
				if(j==i) continue;
				m=wpm[j];
				k=wp[j];
				if(v[j][i]!='.'){
					m--;
					if(v[j][i]=='1') k--;
					dt+=1.0*k/m;
				}
			}
			owp[i]=dt/wpm[i];
			//cout<<1.0*owp[i]<<endl;
		}

		for(i=0;i<n;i++){
			dt=0.0;
			for(j=0;j<n;j++){
				if(j==i) continue;
				if(v[j][i]!='.'){
					dt+=1.0*owp[j]/wpm[i];
				}
			}
			oowp[i]=dt;
		}

		for(i=0;i<n;i++){
			vr[i]=1.0*wp[i]/(4.0*wpm[i])+owp[i]/2.0+oowp[i]/4.0;
		}


		cout<<"Case #"<<test<<":"<<endl;
		cout.precision(12);
		cout.setf(ios::fixed);
		for(i=0;i<n;i++) cout<<vr[i]<<endl;


		v.clear();
		wpm.clear();
		wp.clear();
		owpm.clear();
		owp.clear();
		oowp.clear();
		vr.clear();
	}

	return 0;
}
