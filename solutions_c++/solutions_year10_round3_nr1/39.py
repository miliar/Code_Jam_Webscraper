#include <iostream>
#include <vector>

using namespace std;


int T, N;

vector <int> lv;
vector <int> rv;

bool Intrs(int i, int j)
{
	if( (lv[i] - lv[j])*(rv[i] - rv[j]) < 0 )
		return true;
	return false;
}	

void ReadData()
{
	cin >> N;

	int A, B;

	lv.clear();
	rv.clear();

	for(int i = 0; i < N; i++)
	{
		cin >> A >> B;
		lv.push_back(A);
		rv.push_back(B);
	}
}

int Func()
{
	int ans = 0;

	for(int i = 0; i < N; i++)
	{
		for(int j = 0; j < N; j++)
		{
			if( Intrs(i, j) )
				ans++;
		}
	}

	ans /= 2;

	return ans;
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	cin >> T;

	for(int i = 0; i < T; i++)
	{
		ReadData();
		cout << "Case #" << i + 1 << ": " << Func() << endl;
	}


	return 0;
}