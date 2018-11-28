#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>

using namespace std;

ofstream fout;

void solve(int c, int t, vector<pair<int,int> > &va, vector<pair<int,int> > &vb)
{
	sort(va.begin(),va.end());
	sort(vb.begin(),vb.end());
	int ia = 0;
	int ib = 0;
	vector<int> ta;
	vector<int> tb;
	int reta = 0;
	int retb = 0;
	while(ia < va.size() || ib < vb.size())
	{
		sort(ta.begin(),ta.end());
		sort(tb.begin(),tb.end());
		if(ib >= vb.size() || (ia < va.size() && va[ia].first < vb[ib].first))
		{
			if(ta.size()>0 && ta.front() <= va[ia].first)
				ta.erase(ta.begin());
			else
				reta++;
			tb.push_back(va[ia].second+t);
			ia++;
		}
		else
		{
			if(tb.size()>0 && tb.front() <= vb[ib].first)
				tb.erase(tb.begin());
			else
				retb++;
			ta.push_back(vb[ib].second+t);
			ib++;
		} 
	}
	fout << "Case #" << c+1 << ": " << reta << " " << retb << endl;
}

int main(int argc, char *argv[])
{
	string z;
	ifstream f(argv[1]);
	fout.open(argv[2]);
	int n;
	f >> n;
	getline(f,z);
	for(int i = 0; i < n; i++)
	{
		int t;
		f >> t;
		getline(f,z);
		int na,nb;
		f >> na;
		f >> nb;
		getline(f,z);
		vector<pair<int,int> > va(na);
		vector<pair<int,int> > vb(nb);
		for(int j = 0; j < na; j++)
		{
			getline(f,z);
			va[j].first = ((z[0]-'0')*10+(z[1]-'0'))*60+(z[3]-'0')*10+(z[4]-'0');
			va[j].second = ((z[6]-'0')*10+(z[7]-'0'))*60+(z[9]-'0')*10+(z[10]-'0');
		}
		for(int j = 0; j < nb; j++)
		{
			getline(f,z);
			vb[j].first = ((z[0]-'0')*10+(z[1]-'0'))*60+(z[3]-'0')*10+(z[4]-'0');
			vb[j].second = ((z[6]-'0')*10+(z[7]-'0'))*60+(z[9]-'0')*10+(z[10]-'0');
		}
		solve(i,t,va,vb);
	}
	f.close();
	fout.close();
}
