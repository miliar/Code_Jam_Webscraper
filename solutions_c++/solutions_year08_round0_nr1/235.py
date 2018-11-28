#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;


int N;


void solve()
{
	cin >> N;
	for (int iii = 0; iii < N; iii++)
	{
		int S, Q;
		cin >> S;
		cin.get();
		vector<string> vs;
		for (int i = 0; i < S; i++)
		{
			string str;
			char c[100];
			memset(c, 0, sizeof(c));
			cin.getline(c, 100);
			str = c;
			vs.push_back(str);
		}
		cin >> Q;
		cin.get();
		vector<string> vq;
		for (int i = 0; i < Q; i++)
		{
			string str;
			char c[100];
			memset(c, 0, sizeof(c));
			cin.getline(c, 100);
			str = c;
			vq.push_back(str);
		}

		int res = 0, curInd = 0;

		string ss = "";
		if (vq.size() == 0) cout << "Case #" << iii + 1 << ": " << res << endl;
		while (curInd < vq.size())
		{
			int maxInd = curInd;
			bool e = false;
			for (int i = 0; i < vs.size(); i++)
			{
				int j = curInd;
				if (strcmp(vs[i].c_str(), ss.c_str()) == 0) continue;
				while (j < vq.size())
				{
					if (strcmp(vq[j].c_str(), vs[i].c_str()) == 0)
					{
						if (maxInd < j)
							maxInd = j;
						break;
					}
					j++;
				}
				if (j == vq.size())
				{
					e = true;
					break;
				}
			}
			if (e)
			{
				cout << "Case #" << iii + 1 << ": " << res << endl;
				break;
			}
			ss = vq[maxInd];
			res++;
			curInd = maxInd;
		}
		
	}
}


int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	solve();
	fclose(stdin);
	fclose(stdout);
	return 0;
}