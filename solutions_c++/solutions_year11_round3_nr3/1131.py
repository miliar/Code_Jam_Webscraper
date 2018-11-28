#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <sstream>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <cmath>

#define INF 2000000000
#define EPS 1e-11
#define MAX_N 100002
using namespace std;

#ifdef _WIN32 
typedef __int64 int64; 
#else 
typedef long long int64; 
#endif 

int
main()
{
	int T,N,L,H,res;
	int sum[105];
	bool cek,cek2;
	cin >> T;
	for(int tc = 1;tc <= T;tc++)
	{
		cin >> N >> L >> H;
		for(int i = 0;i < N;i++)
		{
			cin >> sum[i];
		}
		cek2 = false;
		for(int i = L;i <= H;i++)
		{
			cek = true;
			for(int j = 0;j < N;j++)
			{
				if(i >= sum[j])
				{
					if(i % sum[j] != 0)
					{
						cek = false;
						break;
					}
				}
				else
				{
					if(sum[j] % i != 0)
					{
						cek = false;
						break;
					}
				}
			}
			if(cek == true)
			{
				res = i;
				cek2 = true;
				break;
			}
		}
		cout << "Case #" << tc << ": ";
		if(cek2 == false)cout << "NO" << endl;
		else cout << res << endl;
	}
return 0;
}