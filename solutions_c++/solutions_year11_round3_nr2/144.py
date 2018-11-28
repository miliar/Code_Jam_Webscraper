#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cstring>

using namespace std;

const int MaxN = 1000005;
const int MaxC = 1005;

int L, N, C;
long long T;

vector<pair<int, int> > dis;

int cmp(pair<int, int> a, pair<int, int> b)
{
	if (a.first > b.first) return -1;
	if (a.first < b.first) return 1;
	return 0;
}

int main()
{
	int Ncase;
	freopen("b_large.in", "r", stdin);
	freopen("b_large.out", "w", stdout);
	cin >> Ncase;
	for (int run = 0; run < Ncase; ++run)
	{
		dis.clear();
		cin >> L >> T >> N >> C;
		long long sumC = 0, sumR = 0;
		for (int i = 0; i < C; ++i)
		{
			int tmp_dis, tmp_count;
			cin >> tmp_dis;
			tmp_count = N / C + (i < N % C ? 1 : 0);
			//cout << tmp_dis << " " << tmp_count << endl;
			dis.push_back(make_pair(tmp_dis, tmp_count));
			sumC += tmp_dis;
			if (i < N % C) sumR += tmp_dis;
		}
		long long sumAll = sumC * (N / C) + sumR;

		long long builtdis = T/2;
		long long count1 = builtdis / sumC;
		long long count2 = builtdis % sumC;
		for (int i = 0; i < C; ++i)
		{
			if (count1 <= dis[i].second)
				dis[i].second -= count1;
			else
				dis[i].second = 0;
		}
		int tmpsum = 0;
		int stoppos;
		for (int i = 0; i < C; ++i)
		{
			if (tmpsum + dis[i].first > count2)
			{
				for (int j = 0; j <= i; ++j)
					dis[j].second--;
				stoppos = i;
				break;
			}
			tmpsum += dis[i].first;
		}

		int gain = tmpsum + dis[stoppos].first - count2;
		//cout << gain << endl;
		dis.push_back(make_pair(gain, 1));
		sort(dis.begin(), dis.end());
		//for (int i = 0; i < dis.size(); ++i)
		//	cout << dis[i].first << " " << dis[i].second << endl;

		int remain = L;
		long long sumSave = 0;
		for (int i = dis.size()-1; i >= 0; --i)
		{
			if (dis[i].second <= 0) continue;
			int tmp = min(remain, dis[i].second);
			dis[i].second -= tmp;
			sumSave += (long long)dis[i].first * tmp;			
			remain -= tmp;
			if (remain == 0)
				break; 
		}
		//cout << sumAll << " " << sumSave << endl;
			
		cout << "Case #" << run+1 << ": " << (sumAll - sumSave) * 2 + sumSave << endl;
	}
}
