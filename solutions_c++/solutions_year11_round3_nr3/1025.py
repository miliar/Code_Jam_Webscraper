#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int T, N, L, H;
int notes[101];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> T;
	for(int t=1; t<=T; t++)
	{
		cin >> N >> L >> H;
		for(int i=0; i<N; i++)
			cin >> notes[i];
		printf("Case #%d: ", t);
		int i=L;
		for(; i<=H; i++)
		{
			int j=0;
			for(; j<N; j++)
				if(notes[j]%i && i%notes[j])
					break;
			if(j < N)
				continue;
			else 
			{
				cout << i << endl;
				break;
			}
		}
		if(i>H)
			cout << "NO\n";
	}
	return 0;
}
