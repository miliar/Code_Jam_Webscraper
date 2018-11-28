#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
	int T;
	cin >> T;
	int N;
	int a;
	char c;
	for(int i=1;i<=T;i++)
	{
		cin >> N;
		vector<int> o,b;
		vector<char> ch;
		for(int j=0;j<N;j++)
		{
			cin >> c >> a;
			if(c == 'O')
			{
				o.push_back(a);
			}
			else
			{
				b.push_back(a);
			}
			ch.push_back(c);
		}
		int curO = 1;
		int curB = 1;
		int ret = 0;
		int posO = 0;
		int posB = 0;
		for(int j=0;j<ch.size();j++)
		{
			if(ch[j] == 'O')
			{
				int t = abs(o[posO] - curO) + 1;
				if(posB != b.size())
				{
					if(b[posB] > curB)
					{
						curB = min(b[posB], t+curB);
					}
					else
					{
						curB = max(b[posB], curB-t);
					}
				}
				ret += t;
				curO = o[posO];
				posO++;
			}
			else
			{
				int t = abs(b[posB] - curB) + 1;
				if(posO != o.size())
				{
					if(o[posO] > curO)
					{
						curO = min(o[posO], t+curO);
					}
					else
					{
						curO = max(o[posO], curO-t);
					}
				}
				ret += t;
				curB = b[posB];
				posB++;
			}
		}
		cout << "Case #" << i << ": " << ret << endl;
	}
	return 0;
}
