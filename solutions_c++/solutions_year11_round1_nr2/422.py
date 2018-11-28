#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

const int MaxN = 105;
const int MaxM = 15;

int N, M;
int attr[MaxN][30];
bool ok[MaxN];
string word[MaxN];

int main()
{
	int Ncase;
	freopen("b_small.in", "r", stdin);
	freopen("b_small.out", "w", stdout);
	cin >> Ncase;
	for (int run = 0; run < Ncase; ++run)
	{
		cin >> N >> M;
		for (int i = 0; i < N; ++i)
		{
			string tmp;
			cin >> tmp;
			word[i] = tmp;
			attr[i][0] = tmp.size();
			for (int j = 1; j <= 26; ++j)
			{
				int sum = 0;
				for (int k = 0; k < tmp.size(); ++k)
					if (tmp[k] == 'a' + j - 1)
						sum += 1 << k;
				attr[i][j] = sum; // 0 meas no
			}
		}
		string ans = "";
		for (int i = 0; i < M; ++i)
		{
			string seq;
			cin >> seq;
			int max = 0;
			int answer = 0;
			for (int j = 0; j < N; ++j)
			{
				int score = 0;
				for (int k = 0; k < N; ++k)
					if (attr[k][0] != attr[j][0]) ok[k] = false;
					else ok[k] = true;
				for (int k = 0; k < 26; ++k)
				{
					//for (int t = 0; t < N; ++t)
					//	cout << ok[t];
					//cout << endl;
					bool skip = true;
					for (int t = 0; t < N; ++t)
						if (ok[t] && attr[t][seq[k]-'a'+1] > 0)
						{
							skip = false;
							break;
						}
					if (skip) continue;
					if (attr[j][seq[k]-'a'+1] == 0)
						score++;
					for (int t = 0; t < N; ++t)
						if (ok[t] && attr[t][seq[k]-'a'+1] != attr[j][seq[k]-'a'+1])
							ok[t] = false;
				}
				if (score > max)
				{
					max = score;
					answer = j;
				}
				//cout << word[j] << score << endl;
			}
			if (i > 0) ans += " ";
			ans += word[answer];
		}
		cout << "Case #" << run+1 << ": " << ans << endl;
	}
}
