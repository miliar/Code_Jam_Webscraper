#include <queue>
#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	
	for(int i=0; i<T; i++)
	{
		queue<int> q;
		int R,k,N,g;
		
		cin >> R >> k >> N;
		
		for(int j=0; j<N; j++)
		{
			cin >> g;
			q.push(g);
		}
		
		int ans=0;
		
		for(int j=0; j<R; j++)
		{
			int tot=0;
			for(int l=0; l<N; l++)
			{
				int nxt=q.front();
				if(tot+nxt>k)
					break;
				else
				{
					tot += nxt;
					q.push(nxt);
					q.pop();
				}
			}
			ans+=tot;
		}
		
		cout << "Case #" << i+1 << ": " << ans << endl;
	}	
}
