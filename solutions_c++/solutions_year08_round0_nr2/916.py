#include <iostream>
#include <algorithm>

using namespace std;

struct Time
{
	int st, en;
}Train[2][110];

int Q[2][110];
int ans[2];

inline int count(string s)
{
	return ((s[0] - '0') * 600 + (s[1] - '0') * 60 + 
			(s[3] - '0') * 10 + s[4] - '0');
} 

bool cmp(Time X, Time Y)
{
	return (X.en < Y.en);
}

int main()
{
	int NN, T, N[2], p[2], ss;
	
	freopen("1.txt","r",stdin);
	freopen("out.txt","w",stdout);
		
	cin >> NN;
	
	for (int ii = 1; ii <= NN; ++ii)
	{
		cin >> T;
		cin >> N[0] >> N[1];
		
		memset(Q, 0, sizeof(Q));
		memset(ans, 0, sizeof(ans));
				
		for (int i = 0; i < N[0]; ++i) 
		{
			string str1, str2;
			
			cin >> str1 >> str2;
			Train[0][i].st = count(str1);
			Train[0][i].en = count(str2) + T;
		}
		for (int i = 0; i < N[1]; ++i)
		{
			string str1, str2;
			
			cin >> str1 >> str2;
			Train[1][i].st = count(str1);
			Train[1][i].en = count(str2) + T;
		}
		
		sort(&(Train[0][0]),&(Train[0][N[0]]), cmp);
		sort(&(Train[1][0]),&(Train[1][N[1]]), cmp);
		
	/*	for (int i = 0; i < N[0]; ++i) 
			cout << Train[0][i].st << ' ' << Train[0][i].en << endl;
		for (int i = 0; i < N[1]; ++i)
			cout << Train[1][i].st << ' ' << Train[1][i].en << endl;	*/
		
		p[0] = p[1] = ss = 0;
		
		while (ss < N[0] + N[1])
		{
			while (Q[0][p[0]] && p[0] < N[0]) p[0]++;
			while (Q[1][p[1]] && p[1] < N[1]) p[1]++;
			
			if (p[0] >= N[0])
			{
				for (int i = 0 ; i < N[1]; ++i)
					if (!Q[1][i]) ans[1]++;
				
				break;
			}
			
			if (p[1] >= N[1])
			{
				for (int i = 0 ; i < N[0]; ++i)
					if (!Q[0][i]) ans[0]++;
				break;
			}
			
			if (Train[0][p[0]].en <= Train[1][p[1]].en)
			{
				int k = 1;
				int s = Train[0][p[0]].en;
				
				ans[0]++;
				ss++;
				Q[0][p[0]] = 1;
				while (1)
				{
					int flag = 0, mini;
					
					for (int i = 0 ; i < N[k]; ++i)	
						if (Train[k][i].st >= s && !Q[k][i])
						{
							mini = i;
							s = Train[k][i].en;
							flag = 1;
							break;
						}
					if (!flag) break;
					
					ss++; 
					Q[k][mini] = 1;
					k = 1 - k;
				}
				continue;
			}
			
			if (Train[0][p[0]].en > Train[1][p[1]].en)
			{
				int k = 0;
				int s = Train[1][p[1]].en;
				
				ans[1]++;
				ss++;
				Q[1][p[1]] = 1;
				while (1)
				{
					int flag = 0, mini;
					
					for (int i = 0 ; i < N[k]; ++i)	
						if (Train[k][i].st >= s && !Q[k][i])
						{
							mini = i;
							s = Train[k][i].en;	
							flag = 1;
							break;
						}
					if (!flag) break;
					
					ss++;
					Q[k][mini]	= 1;
					k = 1 - k;
				}
			}
		}
		
		printf("Case #%d: %d %d\n", ii, ans[0], ans[1]);
	}
}
