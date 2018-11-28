// ProblemD.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <hash_map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)

const int inf = 1000000;
const double pi = atan(1.0)*4.0;
const double eps = 1e-9;




int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;

	for(int t=0; t<T; t++)
	{
		int K;
		cin >> K;
		string S;
		cin >> S;

		int M = S.length()/K;
		vi perm(K);
		for (int i=0; i<K; i++)
			perm[i]=i;
		int res = S.length();

		do {
			int cnt=0;
			int last_char = 0;
			for(int i=0; i<M; i++)
			{
				for(int j=0; j<K; j++)
				{
					int next_char = S[i*K+perm[j]];
					if (next_char!=last_char)
						cnt++;
					last_char = next_char;
				}
			}
			res = min(res, cnt);
		} while (next_permutation(perm.begin(), perm.end()));
		
		cout << "Case #" << t+1 <<": " << res << endl;
	}

	return 0;
}

