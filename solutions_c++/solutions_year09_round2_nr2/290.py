#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <algorithm>
#include <numeric>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <iterator>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i = 0; i < n; i++)
#define FOR(i,s,e) for(int i = s; i < e; i++)
#define FORD(i,e,s) for(int i = e; i > s; i--)
#define ALL(x) x.begin(), x.end()
#define OUT(x) cout<<#x<<" = "<<x<<endl;
#define PB push_back
typedef long long ll;


int main()
{
	int t;
	cin>>t;
	
	char T[30];
	cin.getline(T,30);

	REP(tests, t)
	{
		cin.getline(T,30);
		int S = strlen(T);
		if(!next_permutation(T,T+S) )
		{
			sort(T,T+S);
			char least = '0';
			for(int i =0;i<S;i++)
				if(T[i]!='0')
				{
					least = T[i];
					T[i]='0';
					break;
				}

			for(int i = S; i>0; i--)
				T[i] = T[i-1];
			T[0]=least;
			T[S+1]=0;
		}
		printf("Case #%d: %s\n", tests+1, T);

			
	}

	return 0;
}

