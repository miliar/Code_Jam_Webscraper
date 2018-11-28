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

string n;
int t[100];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int tests;
	cin >> tests;
	for(int c = 0; c < tests; c++)
	{
		cin >> n;
		int w = 0;
		for(int i = 0; i < n.length(); i++)		
			t[w++] = int(n[i])-48;		
		if(!next_permutation(t, t+w))
		{
			t[w++] = 0;
			sort(t, t+w);
			int i;
			for(i = 0; t[i] == 0; i++);
			swap(t[0], t[i]);
		}
		
			cout << "Case #" << c+1 <<": ";
			for(int i = 0; i < w; i++)
				cout << t[i];
			cout << "\n";
		
	}
	return 0;
}