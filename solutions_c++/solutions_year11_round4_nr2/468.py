#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int T; cin >> T;
	for ( int test=1; test<=T; test++ )
	{
		int R,C,D; cin>>R>>C>>D;
		vector<string> wt(R);
		for ( int y=0; y<R; y++ )
			cin>>wt[y];
		D = 0;

		vector<vector<long long> > w(R,vector<long long>(C,D) );
		for ( int y=0; y<R; y++ )
		for ( int x=0; x<C; x++ )
			w[y][x] += wt[y][x]-'0';

		vector<vector<long long> > M(R+1,vector<long long>(C+1));
		vector<vector<long long> > Mpx = M, Mpy = M;

		for ( int y=1; y<=R; y++ )
		for ( int x=1; x<=C; x++ )
		{
			M  [y][x] = w[y-1][x-1]+  M  [y-1][x]+M  [y][x-1]-M  [y-1][x-1],
			Mpx[y][x] = w[y-1][x-1]*x+Mpx[y-1][x]+Mpx[y][x-1]-Mpx[y-1][x-1],
			Mpy[y][x] = w[y-1][x-1]*y+Mpy[y-1][x]+Mpy[y][x-1]-Mpy[y-1][x-1];
		}

		//for ( int y=0; y<=R; y++ )
		//{
		//	for ( int x=0; x<=C; x++ )
		//		cout << " " << Mpy[y][x];
		//	cout << endl;
		//}



		int K;
		for ( K=min(C,R); K>=3; K-- )
		{
			for ( int y=1; y<=R-K+1; y++/*,cout << endl*/ )
			for ( int x=1; x<=C-K+1; x++ )
			{
				long long m   = M[y+K-1][x+K-1]   - M[y+K-1][x-1]   - M[y-1][x+K-1]   + M[y-1][x-1]   - w[y-1][x-1]   - w[y+K-2][x-1]   - w[y-1][x+K-2] - w[y+K-2][x+K-2];
				long long mpx = Mpx[y+K-1][x+K-1] - Mpx[y+K-1][x-1] - Mpx[y-1][x+K-1] + Mpx[y-1][x-1] - w[y-1][x-1]*x - w[y+K-2][x-1]*x - w[y-1][x+K-2]*(x+K-1) - w[y+K-2][x+K-2]*(x+K-1);
				long long mpy = Mpy[y+K-1][x+K-1] - Mpy[y+K-1][x-1] - Mpy[y-1][x+K-1] + Mpy[y-1][x-1] - w[y-1][x-1]*y - w[y+K-2][x-1]*(y+K-1) - w[y-1][x+K-2]*y - w[y+K-2][x+K-2]*(y+K-1);

				//cout << " " << mpy;

				//if ( mpx/m == x+(K-1)/2
				if ( mpx*2 == (2*x+(K-1))*m  &&
					 mpy*2 == (2*y+(K-1))*m )
					goto found;
			}
		}

found:;
		cout << "Case #" << test << ": ";
		if ( K>=3 )
			cout << K << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
}
