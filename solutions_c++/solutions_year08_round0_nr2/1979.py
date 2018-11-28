#include <fstream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int time2n(string s)
{
	s[2]=' ';
	stringstream aux;
	int a,b;
	aux<<s;
	aux>>a>>b;
	return a*60+b;
}

void main()
{
	ifstream fin("1.in");
	ofstream fout("1.out");
	int test;
	fin>>test;
	for (int t=1;t<=test;++t)
	{
		int n,m,turn;
		fin>>turn>>n>>m;
		vector <pair <int, int> > left, right,both;
		left.push_back(make_pair(-1,-1));
		for (int q=0;q<n;++q)
		{
			string aux,aux2;
			fin>>aux>>aux2;
			left.push_back(make_pair(time2n(aux),time2n(aux2)));
		}
		right.push_back(make_pair(-1,-1));
		for (int q=0;q<m;++q)
		{
			string aux,aux2;
			fin>>aux>>aux2;
			right.push_back(make_pair(time2n(aux),time2n(aux2)));
		}
		both.push_back(make_pair(-1,-1));
		for (int q=1;q<=n;++q)
		{
			both.push_back(left[q]);
		}
		for (int q=1;q<=m;++q)
		{
			both.push_back(right[q]);
		}
		bool g[202][202];
		memset(g,false,sizeof(g));
		for (int q=1;q<=n;++q)
		{
			for (int w=1;w<=m;++w)
				if (left[q].second+turn<=right[w].first) g[q][n+w]=true;
		}
		for (int q=1;q<=m;++q)
		{
			for (int w=1;w<=n;++w)
				if (right[q].second+turn<=left[w].first) g[n+q][w]=true;
		}
		int N=n+m,sol1=0,sol2=0;
		vector <bool> was(N+1,false);
		while (1)
		{
			int node=-1;
			for (int q=1;q<=N;++q)
			{
				if (was[q]) continue;
				bool ok=true;
				for (int w=1;w<=N;++w)
					if (!was[w] && g[w][q])
					{
						ok=false;
						break;
					}
				if (ok)
				{
					node=q;
					break;
				}
			}
			if (node==-1) break;
			was[node]=true;
			if (node<=n) ++sol1;
			else ++sol2;
			int next;
			while (1)
			{
				next=-1;
				for (int i=1;i<=N;++i)
					if (!was[i] && g[node][i] &&
							(next==-1 || both[next].first>both[i].first)) next=i;
				if (next==-1) break;
				g[node][next]=false;
				node=next;
				if (was[node]) fout<<"Nagy baj van!"<<endl;
				was[node]=true;
			}
		}
		for (int q=1;q<=N;++q)
			if (!was[q])
			{
				fout<<"Nagy baj van!"<<endl;
			}
		if (sol1+sol2>N) fout<<"Nagy baj van!"<<endl;
		fout<<"Case #"<<t<<": "<<sol1<<" "<<sol2<<endl;
	}
	fin.close();
	fout.close();
}