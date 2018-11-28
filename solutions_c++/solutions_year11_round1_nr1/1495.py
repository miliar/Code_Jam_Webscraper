// A.cpp : 定义控制台应用程序的入口点。
//

#include <iostream>

using namespace std;

bool Solve()
{
	int Pd, Pg;
	long long n;
	cin >> n >> Pd >> Pg;
	if(Pg == 100 && Pd < 100)
		return false;
	if(Pg == 0 && Pd > 0)
		return false;
	if(Pg % 100 == 0)
		return true;
	if(n >= 100)
		return true;
	if(Pd % 100 == 0 && n >= 1)
		return true;
	if(Pd % 50 == 0 && n >= 2)
		return true;
	if(Pd % 25 == 0 && n >= 4)
		return true;
	if(Pd % 20 == 0 && n >= 5)
		return true;
	if(Pd % 10 == 0 && n >= 10)
		return true;
	if(Pd % 4 == 0  && n >= 25)
		return true;
	if(Pd % 2 == 0 && n >= 50)
		return true;
	return false;
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	int nCase;
	cin >> nCase;
	for(int i = 1; i<=nCase; ++i){
		printf("Case #%d: %s\n", i, Solve()?"Possible": "Broken");
	}
	fclose(stdout);
	return 0;
}

