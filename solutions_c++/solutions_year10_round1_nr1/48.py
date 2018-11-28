#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <complex>

#define mp make_pair
#define pb push_back
#define sqr(x) ((x)*(x))
#define foreach(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;
typedef long long LL;
typedef complex<double> Point;

template<typename T> inline int size(const T &a) { return a.size(); }
template<typename T> inline bool operator<(const int &a,const vector<T> &b) { return a<b.size(); }

int N,K;
VS data,nex;

PII dds[] = { PII(1,0), PII(0,1), PII(1,1), PII(1,-1) };

bool check(int x,int y,int dx,int dy,char chk)
{
	if(x + dx*K > N || x + dx*K < -1) return false;
	if(y + dy*K > N || y + dy*K < -1) return false;
	for(int i=0;i<K;i++)
	{
		if(nex[x+dx*i][y+dy*i] != chk) return false;
	}
	return true;
}

bool process(void)
{
	cin >> N >> K;
	data.clear();
	data.resize(N);
	for(int i=0;i<N;i++)
	{
		string str;
		cin >> str;
		for(int j=0;j<size(str);j++)
		{
			if(str[j] != '.')
				data[i].pb(str[j]);
		}
		std::reverse(data[i].begin(), data[i].end());
	}

	nex = VS(N,string(N,' '));

	for(int i=0;i<N;i++)
	{
		for(int j=0;j<size(data[i]);j++)
		{
			nex[N-1-j][N-1-i] = data[i][j];
		}
	}

	bool red = false, blue = false;
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<N;j++)
		{
			if(!red)
			{
				for(int k=0;k<4;k++)
				{
					red |= check(i,j,dds[k].first, dds[k].second, 'R');
				}
			}
			if(!blue)
			{
				for(int k=0;k<4;k++)
				{
					blue |= check(i,j,dds[k].first, dds[k].second, 'B');
				}
			}
		}
	}

	if(!red && !blue)
	{
		cout << "Neither" << endl;
		return true;
	}
	if(red && blue)
	{
		cout << "Both" << endl;
		return true;
	}
	cout << (red?"Red":"Blue") << endl;
	return true;
}

int main(void)
{
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
		cout << "Case #" << i << ": ";
		process();
	}
	return 0;
}

