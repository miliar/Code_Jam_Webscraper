#include<iostream>
#include<string>
#include<cstring>
#include<vector>
#include<sstream>
#include<fstream>
#include<cmath>
#include<algorithm>
using namespace std;

int table[1010];
string BinarY[1010];
string Copy[1010];
int N;

void gobi(int idx)
{
	int n = table[idx];
	string tmp = "";
	while(n > 0)
	{
		tmp += n%2+'0';
		n /= 2;
	}
	BinarY[idx] = tmp;
	return;
}

bool process(int except_idx)
{

	string tmp = "";
	
	int max_size = -1;
	for(int i=0; i<N; i++)
	{
		Copy[i] = BinarY[i];
//		cout << BinarY[i].size() << " ";
		int that_size = Copy[i].size();
		if(that_size > max_size)
			max_size = that_size;
	}
	for(int i=0; i<N; i++)
	{
		int that_size = Copy[i].size();
		if(that_size < max_size){
			for(int j=that_size; j<max_size; j++)
				Copy[i] += '0';
		}
	}
	string A = Copy[except_idx];
	string B = "";
	for(int i=0; i<max_size; i++)
	{
		int numofone = 0;
		for(int j=0; j<N; j++)
		{
			if(j != except_idx && Copy[j][i] == '1')
				numofone++;
		}
		if(numofone%2 == 1)
			B += '1';
		else
			B += '0';
	}
	if(A == B)
		return true;
	else
		return false;
}

int main()
{
	freopen ("C-small-attempt0.in", "r", stdin);
	freopen ("C-small-attempt0.out", "w", stdout);

	int tc;
	cin >> tc;
	for(int i=1; i<=tc; i++)
	{
		memset(table, 0, sizeof table);
		memset(BinarY, 0, sizeof BinarY);

		cout << "Case #" << i << ": ";

		cin >> N;

		int total = 0;
		for(int i=0; i<N; i++)
		{
			cin >> table[i];
			total += table[i];
		}
		sort( table, table+N );
		for(int i=0; i<N; i++)
			gobi(i);

		int except = -1;
		for(int i=0; i<N; i++)
		{
			if( process(i) )
			{
				except = i;
				break;
			}
		}

		if(except == -1)
			cout << "NO" << endl;
		else
		{
			int answer = 0;
			for(int i=0; i<N; i++) answer += table[i];
			answer -= table[except];

			cout << answer << endl;
		}
	}
	return 0;
}