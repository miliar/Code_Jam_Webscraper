#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;




int main()
{
//	clock_t start, finish;
//  double  duration;
//	start = clock();
	int L, D, N;
	bool flag[5005];
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	

	cin >> L >> D >> N;

	vector<string> dict;
	string word;
	int i;
	for(i = 0; i < D; i ++)
	{
		cin >> word;
		dict.push_back(word);	
	}
	
//	sort(dict.begin(), dict.end());
	
//	for(i = 0; i < D; i ++)
//	{
//		cout << dict[i] << endl;	
//	}
	
	int kase;
	for(kase = 1; kase <= N; kase ++)
	{
		memset(flag, 0, sizeof(flag));	
		string pat;
		char p[20][30];
		memset(p, 0, sizeof(p));
		cin >> pat;
		int j = 0;
		int len = pat.length();
		for(i = 0; i < L; i ++)
		{
			if(j < len)
			{
				if(pat[j] == '(')
				{
					j ++ ;
					while(pat[j] != ')')
					{
						p[i][0]++;
						p[i][p[i][0]] = pat[j];
						j ++;		
					}
					j ++;	
				}
				else	
				{
					p[i][0]++;
					p[i][p[i][0]] = pat[j];
					j ++;
				}
			}
		}
		
		int k;
		int ans = 0;
		for(i = 0; i < D; i ++)
		{
			bool f = true;
			for(j = 0; j < L; j ++)
			{				
				for(k = 1 ; k <= p[j][0]; k ++)
				{
					if(dict[i][j] == p[j][k])
						break;
				}
				if(k == p[j][0] + 1)
				{
					f = false;
					break;
				}				
			}
			if(f)	ans ++;			
		}
		cout <<	"Case #" << kase << ": " << ans << endl;
		
	}
//	finish = clock();
//   	duration = (double)(finish - start) / CLOCKS_PER_SEC;
//   printf( "%2.1f seconds\n", duration );

//	system("pause");
	return 0;
}
