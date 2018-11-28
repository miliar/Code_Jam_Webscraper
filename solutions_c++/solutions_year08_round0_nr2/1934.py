// codejam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <map>
#include <iostream>
#include <string>
#include <bitset>
using namespace std;

map<string,pair<int,int> > sm;
map<string,pair<int,int> >::iterator it;
void addtime(string& s, int T)
{
	int S=((s[0]-'0')*10+(s[1]-'0'))*60+((s[3]-'0')*10+(s[4]-'0'))+T;
	s[4]=(S%60)%10+'0';
	s[3]=(S%60)/10+'0';

	s[1]=(S/60)%10+'0';
	s[0]=(S/60)/10+'0';
}
int _tmain(int argc, _TCHAR* argv[])
{
	bitset<200> bs;
	string s,ta,tb;

	int N;
	cin >>  N;
	for(int n=0;n<N;n++)
	{
		bs.reset();
		sm.clear();

		int T, NA, NB;
		cin >> T;
		getline(cin,s);
		cin >> NA;
		cin >> NB;
		getline(cin,s);
		for(int k=0;k<NA;k++)
		{
			std::getline(cin,s);
			ta=s.substr(0,5);
			tb=s.substr(6,5);
			addtime(tb,T);
			sm[ta].first--;
			sm[tb].second++;
//			cout << ta << "," << tb <<endl;
		}
		for(int k=0;k<NB;k++)
		{
			std::getline(cin,s);
			tb=s.substr(0,5);
			ta=s.substr(6,5);
			addtime(ta,T);
			sm[ta].first++;
			sm[tb].second--;
//			cout << tb << "," << ta <<endl;
		}
		int ca=0,cb=0,ma=0,mb=0;
		for(it=sm.begin();it!=sm.end();it++)
		{
//			cout << it->first << "," << it->second.first << "," << it->second.second << endl;
			ca=ca+it->second.first;
			cb=cb+it->second.second;
			ma=min(ca,ma);
			mb=min(cb,mb);
		}
		cout << "Case #" << n+1 <<": " << -ma << " " << -mb <<endl;
	}

	return 0;
}

