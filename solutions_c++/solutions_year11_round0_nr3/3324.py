/*
 * CandySplitting.cpp
 *
 *  Created on: 2011/05/08
 *      Author: masamichi1222
 */

#include <iostream>
#include <vector>
using namespace std;

class CandySplitting
{
public:
	int solve(vector <int> C, int N)
	{
		int ans=0;
		int S1, S2, P1, P2, pat;

		for(int i=1; i<(1 << N)-1; i++){
			pat = i;
			S1 = 0;
			S2 = 0;
			P1 = 0;
			P2 = 0;
			for(int j=0; j<N; j++){
				if((pat % 2) == 1){
					S1 += C[j];
					P1 = ad(P1,C[j]);
				}
				if((pat % 2) != 1){
					S2 += C[j];
					P2 = ad(P2,C[j]);
				}
				pat = pat >> 1;
//				cout << C[j] << " " << P1 << P2 << S1 << S2 << " ";
			}
//			cout << endl;
			if(P1==P2) ans = max(ans, max(S1,S2));
		}

		return ans;
	}

	int ad(int a, int b)
	{
		return ( ( a | b ) & ~( a & b ) );
	}
};

int main()
{
	int T, N, ans;
	int temp;
	vector <int> C;

	CandySplitting CS;

	cin >> T;
	for(int i=0; i<T; i++){
		cin >> N;
		C.clear();
		for(int j=0; j<N; j++){
			cin >> temp;
			C.push_back(temp);
		}
		ans = CS.solve(C, N);
		cout << "Case #" << i+1 << ": ";
		if(ans==0) cout << "NO" << endl;
		if(ans>0) cout << ans << endl;
	}

	return 0;
}
