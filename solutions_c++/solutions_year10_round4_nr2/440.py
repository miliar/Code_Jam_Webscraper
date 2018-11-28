#include<set>
#include<cstdio>
#include<vector>
#include<string>
#include<fstream>
#include<iostream>
using namespace std;

ifstream in("plik.in");
ofstream out("plik.out");

typedef long long ll;

ll P, pP;
ll input[1<<10];
ll M[1<<10];

ll DP[1<<10][11];
bool was[1<<10][11];

ll rek(ll pos, ll won, ll left, ll right)
{
	if(left == right)
	{
		if(M[left] < won)
		{
			return 10000000000LL;
		} else return 0;
	}

	if (was[pos][won])
		return DP[pos][won];

	ll &ret = DP[pos][won];
	was[pos][won] = true;

	ll lchild, rchild;



	lchild = pP - 2 - (((pP - 2 - pos) + 1) * 2) + 0;
	rchild = pP - 2 - (((pP - 2 - pos) + 1) * 2) + 1;
	
	ret = input[pos] + rek(lchild, won, left, (left + right) / 2) + rek(rchild, won, (left + right) / 2 + 1, right);
	ret = min(ret, rek(lchild, won + 1, left, (left + right) / 2) + rek(rchild, won + 1, (left + right) / 2 + 1, right));

	ret = min(ret, 10000000000LL);

	//cout << pos << " " << won << " " << left << " " << right << " " << ret << "\n";

	return ret;
}

int lecim()
{
	in >> P;
	pP = 1<<P;
	for(int i = 0; i < pP; ++i) in >> M[i];
	for(int i = 0; i < pP - 1; ++i) in >> input[i];

	for(int i = 0; i < pP; ++i)
		for(int j = 0; j < P + 1; ++j)
			was[i][j] = 0;

	return rek(pP - 2, 0, 0, pP - 1);
}

int main()
{
	int t;
	in >> t;

	for(int i = 1; i <= t; ++i)
	{
		cout << i << "\n";
		out << "Case #" << i << ": " << lecim() << "\n";
	}
	in.close();
	out.close();
	cin >> t;
	return 0;
}