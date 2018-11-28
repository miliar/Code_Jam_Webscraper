#include <iostream>
#include <vector>
using namespace std;

int mask[15];
int L, D, N;
vector<string> dict;

int main()
{
	cin >> L >> D >> N;

	for(int i=0 ; i<D ; i++)
	{
		string s;
		cin >> s;
		dict.push_back(s);
	}

	for(int i=1 ; i<=N ; i++)
	{
		int cnt = 0;

		string pat;
		cin >> pat;

		for(int j=0, k=0 ; j<L ; j++, k++)
		{
			int m = 0;

			char ch = pat[k];

			if(ch == '(')
			{
				while(true)
				{
					ch = pat[++k];
					if(ch == ')')
						break;
					m |= (1<<(ch-'a'));
				}
			}
			else
				m |= (1<<(ch-'a'));

			mask[j] = m;
		}

		for(int j=0 ; j<dict.size() ; j++)
		{
			bool good = true;
			for(int k=0 ; k<L ; k++)
			{
				char ch = dict[j][k];
				if((mask[k] & (1<<(ch-'a'))) == 0)
					good = false;
			}

			if(good) cnt++;
		}

		cout << "Case #" << i << ": " << cnt << endl;
	}

	return 0;
}
