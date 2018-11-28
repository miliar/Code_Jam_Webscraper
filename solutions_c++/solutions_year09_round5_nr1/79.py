#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
using namespace std;

#define PT pair<int,int >
		int R,C;

set<vector<PT> > memo;

bool isdanger(const vector<PT> &v)
{
	int N = v.size();
	static int p[5][5];
	for(int i=0;i<N;++i)
	{
		for(int j=i;j<N;++j)
		{
		if(abs(v[i].first-v[j].first) + abs(v[i].second-v[j].second) <= 1)
		{
			p[i][j] = p[j][i] = 0;
		}
		else
		{
			p[i][j] = p[j][i] = 1000;

		}
		}
	}
	for(int k=0;k<N;++k)
	{
		for(int i=0;i<N;++i)
		{
			for(int j=0;j<N;++j)
			{
				p[i][j] <?= p[i][k] + p[k][j];
			}
		}
	}
	for(int i=0;i<N;++i)
	{if(p[i][0] != 0){return true;}}
	return false;
}

void fix(vector<PT> &v)
{sort(v.begin(),v.end());}

vector<PT> GOAL;

int dr[]= {0,0,1,-1};
int dc[] = {1,-1,0,0};

void getcand(const vector<PT> &v,vector<vector<PT> > &out,const vector<string> &vs)
{
	out.clear();
	static int taken[16];
	memset(taken,0,sizeof(taken));
	for(int i=0;i<v.size();++i)
	{
		taken[v[i].first] |= (1<<(v[i].second));
	}
	int NR,NC;
	int NNR,NNC;
	vector<PT> tmp = v;
	for(int i=0;i<v.size();++i)
	{
		for(int t=0;t<4;++t)
		{
			NR = v[i].first+dr[t];
			NC = v[i].second+dc[t];
			if(NR >= R || NR <0 || NC >= C || NC < 0 || vs[NR][NC] == '#' || (taken[NR] & (1<<NC)) != 0)
			{continue;}
			NR = v[i].first-dr[t];
			NC = v[i].second-dc[t];
			if(NR >= R || NR <0 || NC >= C || NC < 0 || vs[NR][NC] == '#'|| (taken[NR] & (1<<NC)) != 0)
			{continue;}
			NR = v[i].first+dr[t];
			NC = v[i].second+dc[t];


			tmp[i] = make_pair(NR,NC);
			out.push_back(tmp);
			tmp[i] = v[i];
		}
	}
}

int main(int argc,char **argv)
{
	int CASES;
	cin >> CASES;
	for(int cn=1;cn<=CASES;++cn)
	{
		scanf("%d %d",&R,&C);
		memo.clear();
		vector<string> vs(R,string());
		for(int i=0;i<R;++i)
		{cin >> vs[i];}
		GOAL.clear();
		vector<PT> start;start.clear();
		for(int i=0;i<R;++i)
		{
			for(int j=0;j<C;++j)
			{
				char c = vs[i][j];
				if(c=='x' || c=='w')
				{
					GOAL.push_back(make_pair(i,j));
				}
				if(c=='o' || c=='w')
				{
					start.push_back(make_pair(i,j));
				}
			}
		}
		fix(start);
		fix(GOAL);
		vector<vector<PT> > curr(1,start);
		vector<vector<PT> > next;
		int out = 0;
		vector<vector<PT> > cands;
		while(!curr.empty())
		{
			//cerr << curr.size() << endl;
			next.clear();
			for(int i=0;i<curr.size();++i)
			{
				vector<PT> &v = curr[i];
				if(v==GOAL){goto yay;}
				cands.clear();
				bool b = isdanger(v);
			//	cerr << "v" << b << endl;
				getcand(v,cands,vs);
			//	cerr << cands.size() << endl;
				for(int j=0;j<cands.size();++j)
				{
					fix(cands[j]);
					bool c = isdanger(cands[j]);
					if(b && c){continue;}
					if(memo.find(cands[j]) != memo.end()){continue;}
					memo.insert(cands[j]);
					next.push_back(cands[j]);
				}
			}
			curr = next;next.clear();
			++out;
		}
		out = -1;
yay:;
		printf("Case #%d: %d\n",cn,out);
		fflush(stdout);
	}
	return 0;
};
