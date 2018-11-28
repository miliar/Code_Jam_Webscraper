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

//Google Code Jam 2011 Qualification Round, Task B code.google.com/codejam
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
	long long test, cases, n, m, mt, res, rt, i, j, k, t, ax;
	char ch, ch0, ch1;
	//string sres[2]={"N", "Y"};
	string s, st;
	//long double dt;

	if(INPUT_FROM) from.open("test.txt");
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	//list<char> lc;
	vector<char> v;
	//vector<vector<char> > vc(n);
	//deque<vector<long long> > dq;
	map<string, char> msc;
	map<string, long long> msi;
	//typedef map<string, long long>::const_iterator CI;
	//list<char>::iterator it, it0, it1;

	fromc>>cases;

	for(test=1;test<=cases;test++){
		fromc>>n;
		for(i=0;i<n;i++){
			fromc>>ch0>>ch1>>ch;
			s="";
			s+=ch0;
			s+=ch1;
			msc[s]=ch;
			swap(ch0, ch1);
			s="";
			s+=ch0;
			s+=ch1;
			msc[s]=ch;
		}
		fromc>>n;
		for(i=0;i<n;i++){
			fromc>>ch0>>ch1;
			s="";
			s+=ch0;
			s+=ch1;
			msi[s]=0;
			swap(ch0, ch1);
			s="";
			s+=ch0;
			s+=ch1;
			msi[s]=0;
		}
		m=0;
		fromc>>n;
		for(i=0;i<n;i++){
			fromc>>ch;
			if(m==0){
				v.push_back(ch);
				m++;
			}else{
				ax=0;
				while((m>0)&&(ax==0)){
					s="";
					s+=v.back();
					s+=ch;
					if(msc.find(s)!=msc.end()){
						ch=msc[s];
						v.pop_back();
						m--;
					}else ax=1;
				}
				ax=0;
				for(j=0;(j<m)&&(ax==0);j++){
					s="";
					s+=v[j];
					s+=ch;
					if(msi.find(s)!=msi.end()) ax=1;
				}
				if(ax==1){
					v.clear();
					m=0;
				}else{
					v.push_back(ch);
					m++;
				}
			}
		}

		cout<<"Case #"<<test<<": [";
		for(i=0;i<m-1;i++) cout<<v[i]<<", ";
		if(m>0) cout<<v[m-1];
		cout<<']'<<endl;

		v.clear();
		msc.clear();
		msi.clear();
	}

	return 0;
}