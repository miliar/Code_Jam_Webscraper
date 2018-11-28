#include <cstdio>
#include <fstream>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <iterator>

using namespace std;

long long once(vector<int> &v, int K)
{
	vector<int>::iterator it;
	vector<int> temp;

	long long result = 0;
	int need_to_remove = 0;

	for(it = v.begin(); it != v.end(); it++)
	{
		if(result + *it <= K)
		{
			result += *it;
			temp.push_back(*it);
			need_to_remove++;
		}
		else
		{
			break;
		}
	}

	v.erase(v.begin(), v.begin() + need_to_remove);
	for(int i = 0; i < temp.size(); i++)
	{
		v.push_back(temp[i]);
	}
	return result;
}

int main()
{
	FILE *in = fopen("F:\\C-small-attempt0.in", "r");
	FILE *out = fopen("F:\\result.txt", "w");
	int T;
	fscanf(in, "%d", &T);

	for(int l = 0; l < T; l++)
	{
		int R, K, N;
		fscanf(in, "%d %d %d", &R, &K, &N);

		vector<int> v;
		int *people = new int[N];

		for(int i = 0; i < N; i++)
		{
			fscanf(in, "%d", &people[i]);
			v.push_back(people[i]);
		}
		
		long long money = 0;

		int times;
		for(times = 0; times < R; times++)
		{
			money += once(v, K);
			int i;
			for(i = 0; i < N; i++)
			{
				if(v[i] != people[i])
				{
					break;
				}
			}
			if(i == N)
			{
				break;
			}
		}
		
		if(times != R)
		{
			times++;
			money *= (R / times);
			if(times != 1)
			{
				for(int i = 0; i < R % times; i++)
				{
					money += once(v, K);
				}
			}
		}

		

		fprintf(out, "Case #%d: %lld\n", l+1, money);

	}
}