#include <cstdio>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;

#define All(a) (a).begin(),(a).end()
#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
#define Sort(c) sort((c).begin(),(c).end())

string solve(uint K, uint N, vector<string> v)
{
	vector<uint> pos(N);
	vector<string> w(N);
	
	for(uint i=0; i<N; i++) for(uint j=0; j<N; j++) if(v[j][i]=='.')
	{
		for(uint k=j+1; k<N; k++) if(v[k][i]!='.')
		{
			v[j][i] = v[k][i];
			v[k][i] = '.';
			break;
		}
	}
	
	bool red = false;
	bool blue = false;
	
	int dx[] = {1,0,1,1};
	int dy[] = {0,1,-1,1};
	
	for(uint i=0; i<N; i++)
	{
		for(uint j=0; j<N; j++)
		{
			if(v[i][j]=='.') continue;
			for(uint d=0; d<4; d++)
			{
				int x = j;
				int y = i;
				uint k = 1;
				for(; k<=K; k++)
				{
					x += dx[d];
					y += dy[d];
					if(x<0||x>=N||y<0||y>=N)
						break;
					if(v[y][x]!=v[i][j])
						break;
				}
				if(k==K)
				{
					if(v[i][j]=='R') red = true;
					if(v[i][j]=='B') blue = true;
				}
			}
		}
	}
	
	if(red&&blue)
		return "Both";
	else if(red)
		return "Red";
	else if(blue)
		return "Blue";
	else
		return "Neither";
}

int main(int argc, char* argv[])
{
	uint T;
	cin >> T;
	
	for(uint t=0;t<T;t++)
	{
		uint K, N;
		cin >> N >> K;
		vector<string> v(N);
		
		for(uint n=0;n<N;n++)
		{
		//	cin >> v[n];
			v[n] = string(N, ' ');
		}
		
		for(uint n=0;n<N;n++)
		{
			string s;
			cin >> s;
			for(uint j=0; j<N; j++)
			{
				v[N-1-j][N-1-n] = s[j];
			}
		}
		
		string r = solve(K, N, v);
		cout << "Case #" << t+1 << ": " << r << endl;
	}
	
	return 0;
}
