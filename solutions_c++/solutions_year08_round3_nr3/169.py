#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int ncase;
	cin >> ncase;
	for(int icase=0; icase < ncase; icase++)
	{
		cout << "Case #" << icase+1 << ": ";

		long long n,m,X,Y,Z;
		cin >> n >> m >> X >> Y >> Z;
//		cout << n << " " << m << " " << X << " " << Y << " " << Z << endl;
		vector<long long> A(m);
		for(long long ia=0; ia < m; ia++)
			cin >> A[ia];
		vector<long long> vsp;
		for (long long i = 0; i < n; i++)
		{
			vsp.push_back(A[i % m]);
		  A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z; 
		}
//		for(long long i=0; i < vsp.size(); i++)
//			cout << vsp[i] << " ";
//		cout << endl;
		long long ret = 0;
		for(long long start=0; start < vsp.size(); start++)
		{
		vector<long long> vseq(n);
		vseq[start] = 1;
		for(long long i=start+1; i < vsp.size(); i++)
		{
			for(long long j=i-1; j >= start; j--)
			{
				if (vsp[j] < vsp[i])
				{
					vseq[i] = (vseq[i] + vseq[j]) % 1000000007L;
				}
			}
		}
		for(long long i=0; i < vseq.size(); i++)
			ret = (ret + vseq[i]) % 1000000007L;
//		cout << ret << endl;
		}
		cout << ret << endl;
	}
}
