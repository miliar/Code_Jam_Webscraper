#include<iostream>
#include<string>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;

int fre[10000+10];
int N,L,H;

bool check(int Num)
{
	for(int i=0; i<N; i++)
	{
		if(Num % fre[i] != 0 && fre[i] % Num != 0)
			return false;
	}
	return true;
}

int main()
{
	freopen ("C-small-attempt0.in", "r", stdin);
	freopen ("C-small-attempt0.out", "w", stdout);
	int tc;
	cin >> tc;
	for(int TC=1; TC<=tc; TC++)
	{
		cin >> N >> L >> H;
		for(int i=0; i<N; i++)
		{
			cin >> fre[i];
		}

		bool flag = false;
		int answer = 0;
		for(int i=L; i<=H; i++)
		{
			if( check(i) )
			{
				answer = i;
				flag = true;
				break;
			}
		}
		cout << "Case #" << TC << ": ";
		if(!flag)
			cout << "NO" << endl;
		else
			cout << answer << endl;
	}
	return 0;
}