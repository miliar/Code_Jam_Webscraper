#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../output.txt");
ifstream fin("../../input.txt");

bool cmp(pair<int,int> a, pair<int,int> b)
{
	return (a.second < b.second);
}

int main(void)
{
	fout.precision(18);
	cout.precision(18);
	int ttt;
	fin >> ttt;
	int ct = 0;
	string s;
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		int n,i,j,k;
		
		int b,e,w;
		
		int len, walk, run, tm;
		
		fin >> len >> walk >> run >> tm >> n;
		
		k = 0;
		
		vector<pair<int,int> > lis;
		
		for(i=0; i<n; i++)
		{
			fin >> b >> e >> w;
			lis.push_back(make_pair(e-b,w+walk));
			k+=(e-b);
		}
		lis.push_back(make_pair(len-k,walk));
		
		sort(lis.begin(),lis.end(),cmp);
		
		for(i=0; i<lis.size() && i<5; i++)
		{
			cout << lis[i].first << " " << lis[i].second << endl;
		}
		
		
		double ans = 0.0;
		
		double timeleft = ((double)tm);
		
		double p,q,r;
		
		for(i=0; i<lis.size(); i++)
		{
			p = lis[i].first;
			q = lis[i].second;
			r = lis[i].second + run- walk;
			if( p / r < timeleft)
			{
				ans+=p/r;
				timeleft-=p/r;
			}
			else {
				ans+=timeleft;
				p-=timeleft*r;
				timeleft=0.0;
				ans+=p/q;
			}
		}

		
		
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
		
		
	}
	
	
	return 0;
}

