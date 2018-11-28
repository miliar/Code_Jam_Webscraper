#include<iostream>
#include<algorithm>
#include<set>
#include<map>
#include<vector>
#include<string>
#include<queue>
#include<deque>
using namespace std;

const int inf = 1000000000;
string s;
long long ile;
int t[200];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int tests;
	cin >> tests;
	for(int c = 0; c < tests; c++)
	{
		for(int i = 0; i < 200; i++)
			t[i] = -1;
		cin >> s;
		bool b = false;	//czy juz bylo 0
		int p = 1;
		for(int i = 0; i < s.length(); i++)
		{
			if(t[int(s[i])] == -1)
			{
				//przyporzadkuj min. symbol
				if(i == 0)
					t[int(s[i])] = p++;
				else
				{
					if(!b)
					{
						t[int(s[i])] = 0;
						b = 1;
					}
					else
						t[int(s[i])] = p++;
				}
			}
		}
		//koniec przyporzadkowywania, przy okazji mamy wyliczona podstawe p
		ile = 0;
		long long mn = 1;
		for(int i = s.length(); i; i--)
		{
			ile = ile + t[int(s[i-1])]*mn;
			mn *= p;
		}
		cout << "Case #" << c+1 <<": " << ile << "\n";		
	}
	return 0;
}