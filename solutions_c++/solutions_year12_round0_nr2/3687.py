#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


int main()
{
	freopen("F:\\B.in","r",stdin);
	freopen("F:\\B.out","w",stdout);
	int t;
	cin>>t;
	for (int c = 1; c <= t; c++)
	{
		int n, s, p;
		int res = 0;
		vector <int> gs;
		cin>>n>>s>>p;
		for (int i = 0;i < n; i++)
		{
			int sc;
			cin>>sc;
			if (sc >= p*3-2)
				res++;
			else if (p*3-4 > 0 && sc >= p*3-4 && s > 0 )
			{
				s--;
				res++;
			}
		}
		cout<<res<<endl;
	}
}