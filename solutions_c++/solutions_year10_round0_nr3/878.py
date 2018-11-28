#include <iostream>
#include <map>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t=1; t<=T; ++t)
	{
		int R, k, N;
		int g[1000];
		cin >> R >> k >> N;
		for(int n=0; n<N; ++n)
			cin >> g[n];
		int s[1000];
		map<int, int> sp_to_s; // Start pos in g -> first occurance
		int n, sp=0;
		for(n=0; n<N; ++n)
		{
			if(sp_to_s.find(sp) != sp_to_s.end())
				break;
			sp_to_s[sp] = n;
			s[n] = 0;
			int pos=sp;
			for(int nn=0; nn<N; ++nn)
			{
				if(s[n] + g[pos] > k)
					break;
				s[n] += g[pos];
				pos = (pos+1)%N;
			}
			sp = pos;
		}
		int f = sp_to_s.find(sp)->second;
		int p = n-f;
		long long total = 0;
		int ftill = f < R ? f : R;
		for(int i=0; i<ftill; ++i)
			total += s[i];
		if(f < R)
		{
			int rem = R - f;
			if(rem > p) // even if its equal, don't find sum for p
			{
				long long psum = 0;
				for(int i=f; i<n; ++i)
					psum += s[i];
				total += psum * static_cast<long>(rem/p);
				rem = rem%p;
			}
			for(int i=0; i<rem; ++i)
				total += s[f+i];
		}
		cout << "Case #" << t << ": " << total << endl;
	}
	return 0;
}
