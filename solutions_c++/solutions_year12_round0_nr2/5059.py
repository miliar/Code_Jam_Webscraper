#include <iostream>
#include <cmath>
#include <map>
#include <fstream>
#include <cstring>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int countBits(int c)
{
	vector<int> v;
	int count = 0;
	while(c > 0)
	{
		count += (c % 2);
		c/=2;
	}
	return count;
}

int getMaxSpecial(int n)
{
	if (n == 0)
		return 0;
	if (n%3 == 0)
		return n/3 + 1;
	if (n%3 == 1)
		return n/3 + 1;
	if (n%3 == 2)
		return n/3 + 2;
}

int getAnswer(vector<int> v, int p, int S)
{
	int SZ = v.size();
	long long t = 1<<SZ;
	int maxWinners = 0;
	for (int i = 0; i < t; i++)
	{
		int winners = 0;
		int count = countBits(i);
		if (count == S)
		{
			int cc = i;
			for (int j = 0; j < v.size(); j++)
			{
				int score = 0;
				if (cc % 2 == 1)
				{
					score = getMaxSpecial(v[j]);
				}
				else
				{
					score = ceil(v[j]/3.0);
				}
				if (score >= p)
					winners++;
				cc /= 2;
			}
		}
		if (winners > maxWinners)
			maxWinners = winners;
	}
	return maxWinners;
}

int main() {
	
	ifstream cin("C:/Users/Qasim/Downloads/B-small-attempt0.in");
	ofstream cout("C:/Users/Qasim/Downloads/b.txt", ios::out);
	
	int T, N, S, P;
	cin>>T;
	for (int i = 0; i < T; i++)
	{
		cin>>N>>S>>P;
		vector<int> v;
		for (int j = 0; j < N; j++)
		{
			int c;
			cin>>c;
			v.push_back(c);
		}
		int ans = getAnswer(v, P, S);
		cout<<"Case #"<<(i+1)<<": "<<ans<<endl;
	}
	return 0;
}