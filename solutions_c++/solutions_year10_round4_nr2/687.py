#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Problem
{
    int P, N;
    vector<int> M;
    vector<vector<int> > price;
    int get_price(int ix, int lev)  { return price[lev-1][ix>>lev]; }
public:
	void ReadData()
	{
	    cin >> P;
	    N = 1 << P;
	    M.resize(N);  for (int i=0; i<N; ++i) cin >> M[i];
	    price.resize(P);
	    for (int p=0; p<P; ++p)
	    {
	        price[p].resize(N>>(p+1));
	        for (int i=0; i<price[p].size(); ++i)  cin >> price[p][i];
	    }
	    
	}
	int solve(int start, int n, int p)
	{
	    if (p==0)  return 0;
	    int pmin = *min_element(M.begin()+start, M.begin()+start+n);
	    if (pmin>p)  return 0;

	    int res = get_price(start, p) + solve(start, n/2, p-1) + solve(start+n/2, n/2, p-1);
	    if (pmin>0)
	    {
	        for (int i=start; i<start+n; ++i)  --M[i];
	        res = min(res, solve(start, n/2, p-1) + solve(start+n/2, n/2, p-1));
	        for (int i=start; i<start+n; ++i)  ++M[i];
	    }
	    return res;
	}
	void Solve(int nCase)
	{
		ReadData();
		cout << "Case #" << nCase << ": " << solve(0, N, P) << endl;
	}
};

int main()
{
	int N;  cin >> N;
	Problem sol;	for (int i=1; i<=N; ++i)  sol.Solve(i);
	return 0;
}