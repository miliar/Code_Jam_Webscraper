#include <vector>
#include <string>
#include <iostream>
#include <memory.h>
#include <algorithm>
#include <stack>
#include <fstream>

using namespace std;


#define All(v) (v).begin(), (v).end()
#define ffor(i,n) for(int i=0; i<n; i++)
#define LL long long
#define LD long double
#define psh push_back
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))


int main()
{
	int c;
	cin >> c;

	for(int i = 0; i < c; i++)
	{
		int p,q;
		cin >> p >> q;

		vector<int> bad;

		vector<bool> pri;
		ffor(j,p)
			pri.psh(true);


		ffor(j,q)
		{
			int t;
			cin >> t;
			bad.psh(t);
		}

		sort(All(bad));

		vector<int> result;

		do
		{
			int res	= 0;
			ffor(j,pri.size())
				pri[j]	= true;

			ffor(j,bad.size())
			{
				int c	= bad[j]-1;
				//cout << c;
				pri[c] = false;
				if(c > 0)
					for(int k = c-1; k >= 0; k--)
					{
						if(pri[k])
							res++;
						else
							break;
					}

				if(c < p)
					for(int k = c+1; k < p; k++)
					{
						if(pri[k])
							res++;
						else
							break;
					}
			}
			result.psh(res);
		}while(next_permutation(All(bad)));

		sort(All(result));

		cout << "Case #" << i+1 << ": " << result[0] << endl;
	}
}
