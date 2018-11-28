#include<iostream>
#include<queue>
using namespace std;
int A[102*102], flow[102*102], color[102*102];
const int dir[4] = {-102,-1,1,102};
int cnt;
int T, H, W;
int main()
{
	cin >> T;
	for(int k=1; k<=T; ++k)
	{
		cin >> H >> W;
		for(int i=0; i<102; ++i)
		for(int j=0; j<102; ++j)
		{
			A[i*102+j] = 10000;
			flow[i*102+j] = -1;
			color[i*102+j] = -1;
		}
		for(int i=1; i<=H; ++i)
		for(int j=1; j<=W; ++j)
			cin >> A[i*102+j];
		for(int i=1; i<=H; ++i)
		for(int j=1; j<=W; ++j) {
			int m=10000;
			for(int t=0; t<4; ++t)
			if(A[i*102+j+dir[t]] < A[i*102+j] && A[i*102+j+dir[t]]<m)
			{
					flow[i*102+j] = i*102+j+dir[t];
					m=A[i*102+j+dir[t]];
			}
		}
		cnt = 0;
		for(int i=1; i<=H; ++i)
		for(int j=1; j<=W; ++j)
		if(color[i*102+j]==-1)
		{
			queue<int> Q;
			color[i*102+j] = cnt++;
			Q.push(i*102+j);
			while(!Q.empty())
			{
				int u=Q.front();
				Q.pop();
				for(int t=0; t<4; ++t)
					if(color[u+dir[t]]==-1 && (flow[u] == u+dir[t] || flow[u+dir[t]] == u))
					{
						color[u+dir[t]] = color[u];
						Q.push(u+dir[t]);
					}
			}
		}
		cout << "Case #" << k << ":" << endl;
		for(int i=1; i<=H; ++i)
		for(int j=1; j<=W; ++j)
		{
			cout << (char)('a'+ color[i*102+j]);
			if(j==W)
			    cout << endl;
			else
			    cout << " ";
		}
	}
	return 0;
}
