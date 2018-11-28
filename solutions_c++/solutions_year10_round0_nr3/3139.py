#include <iostream>
#include <list>
using namespace std;

int main()
{
	long long N,I;
	cin >> N;
	for(I=0;I<N;I++)
	{
		long long R,t,n,g,i,j,k,ans;
		list<long long> q;
		
		cin >> R >> t >> n;
		for(i=0;i<n;i++)
		{
			cin >> g;
			q.push_back(g);		
		}
		
		ans = 0; 
		g = q.front(); q.pop_front(); q.push_back(g);
		for(i=0;i<R;i++)
		{
			k = 0; j = 1;
			while(k+g<=t && j <= n)
			{
				k += g;
				g = q.front(); q.pop_front(); q.push_back(g);
				j++;
			}
			ans += k;	
		}
		
		cout << "Case #" << I+1 << ": " << ans << endl;	
	}
	return 0;
}
