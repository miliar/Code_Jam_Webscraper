#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int no = 1; no <= T; no++)
	{
		int R, k, N;
		cin >> R >> k >> N;
		vector<int> roll(N);
		for(int i = 0; i < N; i++)
			cin >> roll[i];
		
		map<int,long long> cycle;
		int cycleini;
		for(int begin = 0; ; )
		{
			long long sum = 0;
			for(int i = 0; i < N ; i++)
			{
				if(sum + roll[(begin + i) % N] > k)
				{
					begin = (begin + i) % N;
					break;
				}
				sum += roll[(begin + i) % N];
			}
			if(cycle.count(begin) > 0)
			{
				cycle[begin] = sum;
				cycleini = begin;
				break;
			}
			cycle[begin] = sum;
		}
		int lengthcycle = 1;
		long long sumcycle = 0;
		for(int begin = cycleini; ; lengthcycle++)
		{
			long long sum = 0;
			for(int i = 0; i < N ; i++)
			{
				if(sum + roll[(begin + i) % N] > k)
				{
					begin = (begin + i) % N;
					break;
				}
				sum += roll[(begin + i) % N];
			}
			sumcycle += sum;
			if(begin == cycleini)
				break;
		}
		
		long long ans = 0;
		for(int i = 0, begin = 0; i < R; i++)
		{
			if(begin == cycleini && R - i >= lengthcycle)
			{
				ans += (R - i) / lengthcycle * sumcycle;
				i += (R - i) / lengthcycle * lengthcycle - 1;
				continue;
			}
			long long sum = 0;
			for(int i = 0; i < N ; i++)
			{
				if(sum + roll[(begin + i) % N] > k)
				{
					begin = (begin + i) % N;
					break;
				}
				sum += roll[(begin + i) % N];
			}
			ans += sum;
		}
		
		//cout << "Length:" << lengthcycle << " Sum:" << sumcycle << endl;;
		//for(map<long long,long long>::iterator it = cycle.begin(); it != cycle.end(); ++it)
		//	cout << it->first << "," << it->second << " ";
		//cout << endl;
		
		cout << "Case #" << no << ": " << ans << endl;
	}
	return 0;
}
