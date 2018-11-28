#include<iostream>
#include<cstdio>
#include<queue>
#include<cstring>
#include<map>
#include<algorithm>
#include<cmath>
#include<set>
#include<sstream>
#include<map>
#include<utility>

#define S(n) scanf("%d",&n)


#define REP(i,n) for(i=0; i<n; i++)
#define REPA(i,a,n) for(i=a; i<n; i++)
#define SOR(x) sort(x.begin(), x.end())
#define REV(x) reverse(x.begin(), x.end())
#define FOREACH(iter,var) for(__typeof((var).begin()) iter=(var).begin(); iter!=(var).end(); iter++)
#define PB push_back
#define VI vector<int>
#define SZ size()
#define VS vector<string>

#define MP make_pair
#define VVI vector< vector<int> >
#define INF 2000000000

#define CLR(var,val) memset(var,val,sizeof((var)))
#define S(n) scanf("%d",&n)
#define LL unsigned long long
#define LD long double
#define triple pair<int, pair<int,int> >
#define OFF 0
#define MAX(a,b) (a>b?a:b)

using namespace std;


int main()
{
	//freopen("inp.in", "r", stdin);
	int T;
	cin >> T;
	char b[110][110];
	int c = 0;
	while(T--)
	{
		c++;
		int N, K;
		cin >> N >> K;
		int i, j;
		REP(i,N) REP(j,N) cin>>b[i][j];
		char r[110][110];
		REP(i,N) REP(j,N) 
		if(b[N-j-1][i] != '.')
			r[i][j] = b[N-j-1][i];
		else r[i][j] = '.';
		/*
		REP(i,N)
		{
			REP(j,N) cout << r[i][j];
			cout << endl;
		}*/
		
		for(i = N - 1; i >= 0; i--)
			for(j = 0; j < N; j++)
				if(r[i][j] == '.')
					for(int k = i - 1; k >= 0; k--)
						if(r[k][j] != '.')
						{
							r[i][j] = r[k][j];
							r[k][j] = '.';
							break;
						}
		/*			
		REP(i,N)
		{
			REP(j,N) cout << r[i][j];
			cout << endl;
		}*/	
		
		bool w[2]; w[0] = 0; w[1] = 0;
		//Horizontal
		int cur = 0, streak = 0;
		for(i = 0; i < N; i++)
		{
			streak = 0;
			for(j = 0; j < N; j++)
			{
				if(r[i][j] == '.') { if(streak >= K) w[cur] = 1; cur = 0; streak = 0; }
				if(r[i][j] == 'R') 
				{
					if(cur != 0) {  if(streak >= K) w[cur] = 1; cur = 0; streak = 0; }
					streak++;
					if(streak >= K) { w[cur] = 1; }
				}
				else if(r[i][j] == 'B')
				{
					if(cur != 1) {  if(streak >= K) w[cur] = 1; cur = 1; streak = 0;  }
					streak++;
					if(streak >= K) w[cur] = 1;
				}
			}
		}
		//Vertical
		
		cur = 0; streak = 0;
		for(j = 0; j < N; j++)
		{
			streak = 0; cur = 0;
			for(i = 0; i < N; i++)
			{
				if(r[i][j] == '.') { if(streak >= K) w[cur] = 1; cur = 0; streak  = 0;}
				if(r[i][j] == 'R') 
				{
					if(cur != 0) {  if(streak >= K) w[cur] = 1; cur = 0; streak = 0;  }
					streak++;
					if(streak >= K) w[cur] = 1;
				}
				else if(r[i][j] == 'B')
				{
					if(cur != 1) {  if(streak >= K) w[cur] = 1; cur = 1; streak = 0;  }
					streak++;
					if(streak >= K) w[cur] = 1;
				}
			}
		}
		
		cur = 0; streak = 0;
		int k;
		
		for(i = 0; i < N; i++)
		{
			for(j = 0; j < N; j++)
			{
				cur = 0; streak = 0;
				for(k = 0; ; k++)
				{
					if((i + k) < N && (j + k) < N)
					{
						if(r[i+k][j+k] == '.') { if(streak >= K) w[cur] = 1; cur = 0; streak = 0;  }
						if(r[i+k][j+k] == 'R') 
						{
							if(cur != 0) {  if(streak >= K) w[cur] = 1; cur = 0; streak = 0;  }
							streak++;
							if(streak >= K) w[cur] = 1;
						}
						else if(r[i+k][j+k] == 'B')
						{
							if(cur != 1) {  if(streak >= K) w[cur] = 1; cur = 1; streak = 0;  }
							streak++;
							if(streak >= K) w[cur] = 1;
						}
					} else break;	
				}
				
				cur = 0; streak = 0;
				for(k = 0; ; k--)
				{
					if((i-k) < N  && (j + k) >=0)
					{
						if(r[i-k][j+k] == '.') { if(streak >= K) w[cur] = 1; cur = 0; streak = 0;  }
						if(r[i-k][j+k] == 'R') 
						{
							if(cur != 0) {  if(streak >= K) w[cur] = 1; cur = 0; streak = 0;  }
							streak++;
							if(streak >= K) w[cur] = 1;
						}
						else if(r[i-k][j+k] == 'B')
						{
							if(cur != 1) {  if(streak >= K) w[cur] = 1; cur = 1; streak = 0;  }
							streak++;
							if(streak >= K) w[cur] = 1;
						}
					} else break;	
				}
			}
		}
		
		cout << "Case #" << c << ": ";
		if(w[0] && w[1]) cout << "Both";
		else if(w[0]) cout << "Red";
		else if(w[1]) cout << "Blue";
		else cout << "Neither";
		
		cout << endl;
	}
	
	return 0;
}
