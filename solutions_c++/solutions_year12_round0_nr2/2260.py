// B.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <functional>
#include <fstream>
using namespace std;

bool is_ok_no_surp(int score, int p)
{
	int v=score / 3;
	if(v*3<score)
		v++;
	if(v>=p)
		return true;
	return false;
}

bool is_ok_surp(int score, int p)
{
	if((p-2)*2 > score-p)
		return false;
	return true;
}

int get_ans(int n, int s, int p, vector<int> & vi)
{
	int ret = 0;
	int np_cnt = 0;

	for(int i=0; i<vi.size(); i++)
	{
		if(is_ok_no_surp(vi[i], p))
		{
			ret++;
		}else {
			if(s<=0)
				break;
			if(vi[i]>=p && is_ok_surp(vi[i], p))
			{
				ret++;

				s--;
				if(s<=0)
					break;
			}
		}
	}

	return ret;
}

int main()
{
	char chline[10000];
	ifstream inf(L"in.txt");
	ofstream outf(L"out.txt");

	inf.getline(chline,10000);
	istringstream iss(chline);

	int cnt;
	iss>>cnt;
	for(int zi=0; zi<cnt; zi++)
	{
		inf.getline(chline,10000);
		istringstream iss_l(chline);
		int n, s, p;
		iss_l>>n>>s>>p;
		vector<int> vi;
		for(int si=0; si<n; si++)
		{
			int t;
			iss_l>>t;
			vi.push_back(t);
		}
		sort(vi.begin(), vi.end(), greater<int>());

		int ans = 0;
		if(p<=1)
		{
			for(int si=0; si<vi.size(); si++)
			{
				if(vi[si]>=p)
					ans++;
			}
		}else {
			ans = get_ans(n, s, p, vi);
		}

		outf<<"Case #"<<zi+1<<": "<<ans<<endl;
	}


	inf.close();
	outf.close();
	return 0;
}

