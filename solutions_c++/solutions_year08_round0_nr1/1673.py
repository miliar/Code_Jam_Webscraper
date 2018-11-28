#include <iostream>
#include <fstream>
using namespace std;

//ifstream in;
ofstream out;

const int MAX_L = 128;
const int MAX_S = 128;
const int MAX_Q = 1024;
const int INF = 1 << 20;

int N, S, Q, ans;
int dp[MAX_Q][MAX_S];
string names[MAX_S];
char temp[MAX_L];

void Read()
{
	scanf("%d\n", & S);
	
	for(int i = 0; i < S; i ++)
	{
		gets(temp);
		
		names[i] = string(temp);
		
		cout << names[i] << "\n";
	}
	
	cout << ".............\n\n";
}

void Solve()
{
string now;
	
	for(int i = 0; i < MAX_Q; i ++)
	{
		for(int j = 0; j < MAX_S; j ++)
		{
			dp[i][j] = INF;
		}
	}
	
	scanf("%d\n", & Q);
	
	gets(temp);
	
	now = string(temp);
	
	cout << now << "\n";
	
	Q --;
	
	for(int i = 0; i < S; i ++)
	{
		if(names[i] != now)
		{
			dp[0][i] = 0;
		}
	}
	
	for(int q = 0; q < Q; q ++)
	{
		cin.getline(temp, MAX_L);
		
		now = string(temp);
		
		cout << now << "\n";
		
		for(int i = 0; i < S; i ++)
		{
			if(names[i] == now)
			{
				for(int j = 0; j < S; j ++)
				{
					if(i != j)
					{
						dp[q + 1][j] = min(dp[q + 1][j], dp[q][i] + 1);
					}
				}
			}
			else
			{
				dp[q + 1][i] = min(dp[q + 1][i], dp[q][i]);
			}
		}
	}
	
	cout << "----------------------\n\n";
	
	ans = INF;
	
	for(int i = 0; i < S; i ++)
	{
		ans = min(ans, dp[Q][i]);
	}
}

int main()
{
//	in.open("save.in");
	out.open("save.out");
	
	cin >> N;
	
	for(int i = 1; i <= N; i ++)
	{
		Read();
		
		Solve();
		
		out << "Case #" << i <<": "<< ans << "\n";
	}
	
//	in.close();
	out.close();
	
	return 0;
}
