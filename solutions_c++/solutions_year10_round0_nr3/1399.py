#include <iostream>
#include <queue>
using namespace std;

int n, i, j, k, r, cap, aux, money;
queue<int> q;

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin >> t;
	for(int tc=1;tc<=t;++tc)
	{
		cout << "Case #" << tc << ": ";
		money = 0;
		cin >> r >> k >> n;
		while(!q.empty()) q.pop();
		for(i=0;i<n;++i)
		{
			cin >> j;
			q.push(j);
		}
		while(r--)
		{
			j = n;
			cap = 0;
			while(j-- && cap+q.front() <= k)
			{
				cap += (aux = q.front());
				q.pop();
				q.push(aux);
			}
			money += cap;
		}
		cout<<money<<endl;
	}
}
