#include <stdio.h> 
#include <vector> 
#include <list>
#include <string>
#include <set>
#include <algorithm> 
#include <fstream> 
#include <iostream> 
using namespace std; 
int main() 
{ 
	int T;
	cin >> T;
	
	for (int test = 1; test <= T; ++test)
	{
		int n, btime=0, otime = 0;
		int BluePos = 1;
		int OrangePos = 1;

		cin >> n;
		char prev=0;
		int luft = 0;
		for (int i = 1; i <= n; ++i)
		{
			char R;
			int k;
			cin >> R >> k;
			if (R == 'B')
			{
				int needtogo = abs(k-BluePos);
				if (prev == 'O')
				{
					needtogo -= luft;
					if (needtogo < 0)
						needtogo = 0;
					luft = 0;
				}
				btime += needtogo + 1;
				luft += needtogo + 1;
				prev = 'B';
				BluePos = k;
			}
			else if (R == 'O')
			{
				int needtogo = abs(k-OrangePos);
				if (prev == 'B')
				{
					needtogo -= luft;
					if (needtogo < 0)
						needtogo = 0;
					luft = 0;
				}
				otime += needtogo + 1;
				luft += needtogo + 1;
				prev = 'O';
				OrangePos = k;
			}
			else
			{
				__asm __emit 0xCC;
			}
		}
		cout << "Case #" << test << ": " << (btime + otime) << "\n";		
	}
#ifndef ONLINE_JUDGE
#ifndef FULLREDIRECT
	ifstream console("CONIN$");
	char fdasfadsfdasfdsa;
	console.getline(&fdasfadsfdasfdsa,1);
	console.close();
#endif
#endif
	return 0; 
}