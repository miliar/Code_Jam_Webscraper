#include <iostream>
using namespace std;

int main(void)
{
	int T, N;
	
	cin >> T;
	for(int numCase = 1; numCase <= T; numCase++)
	{
		int psum = 0, sum = 0, vmin = 2<<29, v;
		
		cin >> N;
		for(int i = 1; i <= N; i++)
		{
			cin >> v;
			psum ^= v;
			sum += v;
			vmin = min(vmin, v);
			
		}
		
		if(psum == 0) cout << "Case #" << numCase << ": " << sum - vmin << endl;
		else cout << "Case #" << numCase << ": NO" << endl;
	}
}
