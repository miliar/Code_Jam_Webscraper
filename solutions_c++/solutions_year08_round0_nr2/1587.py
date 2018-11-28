// BEGIN CUT HERE
#include "stdafx.h"
// END CUT HERE

#include <map>
#include <set>
#include <sstream>
#include <iostream>
#include <list>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <queue>
#include <fstream>
using namespace std;
int gettime(string time){
	int h,m;
	sscanf(time.c_str(),"%d:%d",&h,&m);
	return 60*h+m;
}
int main()
{
	ifstream inf;
	ofstream of;
	inf.open("d:\\input.in",ios::in);
	of.open("d:\\output.txt");

	int n;
	string ssss;
	inf>>ssss;
	sscanf(ssss.c_str(),"%d",&n);

	for(int ii=0;ii<n;++ii)
	{
		string s;
		int turn;
		int na,nb;
		int resa,resb;
		resa=resb=0;
		inf>>s;
		sscanf(s.c_str(),"%d",&turn);
		inf>>s;
		sscanf(s.c_str(),"%d",&na);
		inf>>s;
		sscanf(s.c_str(),"%d",&nb);
		
		vector<pair<int,int> > basea;
		vector<pair<int,int> > baseb;
		for(int i=0;i<na;++i){
			string t1,t2;
			inf>>t1;
			inf>>t2;
			int tim1 = gettime(t1);
			int tim2 = gettime(t2);
			basea.push_back(make_pair(tim1,tim2));
		}
		for(int i=0;i<nb;++i){
			string t1,t2;
			inf>>t1;
			inf>>t2;
			int tim1 = gettime(t1);
			int tim2 = gettime(t2);
			baseb.push_back(make_pair(tim1,tim2));
		}
		sort(basea.begin(),basea.end());
		sort(baseb.begin(),baseb.end());

		vector<int> counta(100000);
		vector<int> countb(100000);
		for(int t=0;t<24*60;++t){
			while(basea.size()&&basea.front().first == t){
				if(counta[t]){
					counta[t]--;
				} else {
					resa++;
				}
				int newt = basea.front().second+turn;
				countb[newt]++;
				basea.erase(basea.begin(),basea.begin()+1);
			}
			while(baseb.size()&&baseb.front().first == t){
				if(countb[t]){
					countb[t]--;
				} else {
					resb++;
				}
				int newt = baseb.front().second+turn;
				counta[newt]++;
				baseb.erase(baseb.begin(),baseb.begin()+1);
			}
			counta[t+1]+=counta[t];
			countb[t+1]+=countb[t];
		}
		of << "Case #" << (ii+1)<<": ";
		of << resa << " " << resb;
		of << '\n';
	}
	inf.close();
	of.close();
	return 0;
}

