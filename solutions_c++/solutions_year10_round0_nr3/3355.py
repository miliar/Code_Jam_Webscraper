#include <iostream>
#include <vector>
using namespace std;

int main (int argc, char * const argv[]) {
    // insert code here...

	long long T, R, k, N;

	
	cin >> T;
	for(int i=0; i<T; i++)
	{
		vector<long long> V;
		long long result = 0;
		cin >> R >> k >> N;
		for(int j=0; j<N; j++)
		{
			long long g;
			cin >> g; 
			V.push_back(g);
		}
		long long pos = 0, cnt = 0;
		result = 0;
		for (int j=0, cnt = 0; j<R; j++)
		{
			long long start_pos = -1;
			while(1)
			{
				if (pos == start_pos) break;
				if (start_pos == -1) start_pos = pos;
				if((cnt+V[pos]) > k) break;
				cnt+=V[pos]; pos=((pos+1)%N);				
			}
			result+=cnt;
			cnt = 0;
		}
		cout << "Case #" << i+1 << ": " << result << endl;
	}
	
    return 0;
}
