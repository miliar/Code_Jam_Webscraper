#include <iostream>
#include <queue>;

using namespace std;

void prepare()
{
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
}

int t;
int r,k,n;
int cost = 0;
queue <int> q;	

void gonah(int ncase)
{
	cost = 0;
	for( int i = 0; i < r; i++)
	{
		int pp = 0;
		int fr;
		for( int j = 0; j < q.size(); j++ )
		{
			fr =  q.front();
			pp += fr;
			if( pp > k )
				break;
			cost += fr;
			q.pop();
			q.push(fr);
		}
		
	}
	cout << "Case #" << ncase << ": "<< cost << endl;
}

void solve()
{	
	
	cin  >> t;
	for(int i = 0; i < t; i++ )
	{
		q = queue<int>();  
		cin >> r >> k >> n;
		for( int j = 0; j < n; j++ )
		{
			int ff;
			cin >> ff;
			q.push(ff);
		}
		gonah(i+1);
		
	}

	
}

int main()
{
	prepare();
	solve();
}