#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<sstream>
#include<map>
#include<queue>
#include<set>
#define vi vector<int>
#define vs vector<string>

#define REP(i,n) for(int i=0;i<(int) n;i++)
#define LL long long
#define INF (2<<29)

using namespace std; 

string words[5001];

bool Valid[16][26];
void decode(const string& pattern)
{
	memset(Valid , false, sizeof(Valid));
	
	int index = 0;
	int start = -1;
	for(int i = 0; i < pattern.size(); ++i)
	{
		if(pattern[i] == '(')
		{
			start = i+1;
		}
		else if(pattern[i] ==')')
		{
			for(int j = start; j < i; ++j)
			{
				Valid[index][pattern[j]-'a'] = true;
			}
			start = -1;
			++index;
		}
		else if(start == -1)
		{
			Valid[index][pattern[i]-'a'] = true;
			++index;
		}
	}
	
	return;
}

int main()
{
	int N, L, D;
	cin >> L >> D >> N;
	
	for(int i = 0; i < D; ++i)
	{
		cin >> words[i];
	}
	
	for(int i = 0; i < N; ++i)
	{
		string pattern;
		cin >> pattern;
		decode(pattern);
		
		int res = 0;
		for(int j = 0; j < D; ++j)
		{
			int k = 0;
			for(k = 0; k < L; ++k)
			{
				if(!Valid[k][words[j][k] - 'a'])
					break;
			}
			if( k == L )
				++res;
		}
		cout <<"Case #" << i + 1 << ": " << res << endl;
		
	}
}
