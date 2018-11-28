#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
using namespace std;
#define LET(x,a) typeof(a)x(a)
#define FOR(i,a,n) for(LET(i,a);i<n;++i)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define cs c_str()
#define GI ({int t; scanf("%d",&t); t;})
#define EACH(it,v) for(LET(it,v.begin()); it!=v.end(); ++it)
#define dbg(x) (fout << #x << ":" << (x) << "\t")
#define dbge(x) (dbg(x), fout << endl)
#define PII pair<int,int>

int dx[4] = {-1,0,0,1};
int dy[4] = {0,-1,1,0};

ifstream fin("input.txt");
ofstream fout("output.txt");

int maxval;
map<PII, int >mp;
vector< vector<int> >v;
int R, C;

int go(int row, int col)
{
	if(mp.count(PII(row,col)))return mp[PII(row,col)];
	
	int ndir = -1, maxalt = v[row][col];
	
	REP(dir, 4)
	{
		int nrow = row + dx[dir], ncol = col + dy[dir];
		
		if(nrow >= 0 && nrow < R && ncol >=0 && ncol < C)
		{
			if(v[nrow][ncol] < maxalt)
			{
				ndir = dir;
				maxalt = v[nrow][ncol];
			}
		}
	}
	
	if(ndir == -1){mp[PII(row,col)] = maxval; return maxval++;}
	
	return mp[PII(row,col)] = go(row + dx[ndir], col + dy[ndir]);

}

int main()
{
	int N; fin>>N;
	
	REP(kase,N)
	{
		v.clear();
		mp.clear();
		maxval = 0;
		
		fin>>R>>C;
		REP(i, R)
		{
			vector<int> tmp;
			REP(j,C){int val; fin>>val; tmp.pb(val);}
			v.pb(tmp);
		}
		
		REP(i,R)REP(j,C)go(i,j);
		
		fout<<"Case #"<<(kase+1)<<":"<<endl;
		
		EACH(it, mp)
		{
			int row = it->first.first;
			int col = it->first.second;
			
			v[row][col] = it->second;
		}
		
		REP(i, v.sz)REP(j,v[i].sz){fout<<(char)(v[i][j]+'a'); if(j!= v[i].sz-1)fout<<" "; else fout<<endl;}
	}
	
	return 0;
}
