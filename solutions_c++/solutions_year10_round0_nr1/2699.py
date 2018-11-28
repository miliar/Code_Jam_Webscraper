#include <iostream>

using namespace std;

void prepare()
{
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
}
int n,k;

bool solve()
{
	int c = 1;
	c <<= n;
	--c;
	int  d = k & c;
	if(d == c)
		return true;
	return false;
	
}

int main()
{
	prepare();

	int t;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		cin >> n >> k;
		if(solve())
		{
			cout << "Case #" << i+1 <<": ON"<<endl;
		}
		else
		{
			cout << "Case #" << i+1 << ": OFF"<<endl;
		}
	}
	return 0;
}