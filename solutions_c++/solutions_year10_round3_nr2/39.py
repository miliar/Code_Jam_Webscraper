#include <iostream>
#include <vector>

using namespace std;

int T, L, P, C;

vector <int> ans;

void Pre()
{
	ans.push_back(0);
	ans.push_back(1);
	ans.push_back(2);

	for(int i = 3; i <= 32; i++)
	{
		ans.push_back( ans[i/2] + 1 );
	}
}


void ReadData()
{
	cin >> L >> P >> C;
}

int Func()
{
	long long cur = L;

	int num = 0;

	while( true )
	{
		if( cur * C >= P )
			break;

		cur *= C;

		num++;
	}

	return ans[num];
}


int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	cin >> T;

	Pre();

	for(int i = 0; i < T; i++)
	{
		ReadData();
		cout << "Case #" << i + 1 << ": " << Func() << endl;
	}


	return 0;
}