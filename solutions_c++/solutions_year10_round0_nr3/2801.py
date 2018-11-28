
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
#include <queue>

using namespace std;

deque<int> Q;
int T, R, K, N;

//map<string, int, less<string> > koko[10000000];

string getKey()
{
	string key = "";
	for(int i = 0 ; i < N ; i++)
	{
		ostringstream oss;
		oss << Q[i];
		oss << "-";
		key += oss.str();
	}
	return key;
}

int main()
{

	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	
	scanf("%d", &T);
	for(int t = 1 ; t <= T ; t++)
	{
		scanf("%d %d %d", &R, &K, &N);
		int g;
		Q.clear();
		for(int i = 0 ; i < N ; i++)
		{
			scanf("%d", &g);
			Q.push_back(g);
		}

		map<string, int, less<string> > key;
		map<string, string, less<string> > koko;
		string keyString = getKey();
		string lastkey = keyString;
		koko[keyString] = "-";

		long long y = 0;
		
		for(int i = 0 ; i < R ; i++)
		{
			int j = 0;
			int count = 0;
			while(j < N && count <= K)
			{
				int temp = Q.front();
				if(temp + count > K)
					break;
				count += temp;
				Q.pop_front();
				Q.push_back(temp);
				j++;
			}
			y += count;
			
			//keyString = getKey();
			//koko[keyString] = lastkey;
			//key[keyString] = count;
			//lastkey = keyString;
		}

		printf("Case #%d: %lld\n", t, y);
	}
	return 0;
}