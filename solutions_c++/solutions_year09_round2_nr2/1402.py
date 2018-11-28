#include <iostream>
#include <cstdio>
#include <algorithm>
#include <list>
#include <fstream>

using namespace std;



int main()
{
	int T;
	cin >> T;
	ofstream fout("bsmall.out");
	for (int test=1; test<=T; test++)
	{
		int N;
		cin >> N;
		bool Ada = false;
		int i;
		for (i=N; !Ada;)
		{
			i++;
			list<int> LInt;
			
			int W = N;
			while (W>0)
			{
				if (W%10)
					LInt.push_back(W%10);
				W/=10;
			}
			
			int x = i;
			bool Coba = true;
			//cout << i << "\n";
			while (x>0 && Coba)
			{
				list<int>::iterator LI = find(LInt.begin(), LInt.end(), x%10);
				
				//if (x%10!=0 && find(LInt.begin(), LInt.end(), x%10)==LInt.end())
				if (x%10!=0 && LI==LInt.end())
					Coba = false;
				else 
					if (x%10!=0)
						LInt.erase(LI);
				x /= 10;
			}
			if (Coba && LInt.empty()) Ada = true;
		}
		fout << "Case #" << test << ": " << i << "\n";
	}
	return 0;
}
