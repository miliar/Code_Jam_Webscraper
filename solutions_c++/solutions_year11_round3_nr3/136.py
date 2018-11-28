#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <map>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <numeric>

#define all(x) x.begin() , x.end()
#define pb(x) push_back(x)
#define sz(x) ((int) x.size())
#define INF 0x7fffffff
#define LL long long
#define LD long double
#define VI vector<int>
#define VS vector<string>

using namespace std;


int main()
{
	int Te;
	cin >> Te;
	for(int te=0 ; te<Te  ; te++)
	{
		cout << "Case #"<<te+1 << ": ";
		int N,L,H;
		int vals[101];
		cin >> N >> L >> H;
		for(int i=0 ; i<N ; i++) cin >> vals[i];		

		int note = -1;
		for(int n=L ; n<=H ; n++)
		{
			int cnt = 0;
			for(int i=0 ; i<N ; i++)
				if(n % vals[i] == 0 || vals[i] % n == 0)
					cnt++;
			if(cnt == N)
			{
				note = n;
				break;
			}
		}

		if(note == -1) cout << "NO\n";
		else cout << note << endl; 
	}
}
