#include<cstdio>
#include<iostream>

using namespace std;

int n,k;

int main()
{
	freopen("a-large.in","r",stdin);
	freopen("out.out","w",stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		cin >> n >> k;
		int temp = ((1<<n)-1);
		cout << "Case #" << i + 1 << ": " << ((temp^(temp&k))?"OFF":"ON") << endl;
	}
}