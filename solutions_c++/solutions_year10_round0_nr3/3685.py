#include <iostream>
using namespace std;

int main()
{
	freopen("C-small-attempt1.in","r",stdin); freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	for(int t=1; t<=T; t++)
	{
		int R, K, N;
		cin >> R >> K >> N;
		int g[N];
		for(int i=0; i<N; i++) cin >> g[i];
		
		int turn = 0, total = 0;
		bool exist[N];
		
		for(int i=0; i<R; i++)
		{
			memset(exist , 0, sizeof(exist));
			int aboard = 0;
			while(aboard + g[turn] <= K)
			{
				aboard += g[turn];
				exist[turn] = 1;
				turn ++;
				if(turn == N) turn = 0;
				if(exist[turn]) break;
			}
			total += aboard;
		}
		
		cout << "Case #" << t << ": " << total << endl;
	}
}
