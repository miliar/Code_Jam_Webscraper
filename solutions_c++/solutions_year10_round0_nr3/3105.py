#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

struct st
{
	int awal, akhir, jum;
};

int main()
{
	int T;
	scanf("%d", &T);
	
	for(int test=1; test<=T; test++)
	{
		int R, K, N;
		int G[1005];
		//int Ans = 0;
		long long Ans=0;
		int ct = 0;
		vector<st> JumSave;
		
		cin >> R >> K >> N;
		for (int i=0; i<N; i++)
			cin >> G[i];
			
		for (int i=0; i<R; i++)
		{
			int Jum = 0;
			int tempct = ct;

			while (G[ct]+Jum <= K)
			{
				Jum += G[ct];
				ct++;
				if (ct==N) ct=0;
				if (ct==tempct) break;
			}
			
			st tempST;
			tempST.awal = tempct;
			tempST.akhir = ct;
			tempST.jum = Jum;
			
			if (JumSave.empty()) 
			{
				Ans += Jum;
				JumSave.push_back(tempST);
			}
			else if (JumSave[0].awal==tempST.awal && JumSave[0].akhir==tempST.akhir)
			{
				int Sisa = R-i;
				int Pjg = JumSave.size();
				int JumSisa = Sisa/Pjg;
				Sisa -= (JumSisa*Pjg);
				for (int j=0; j<Pjg; j++)
				{
					long long rrr = (long long) JumSisa*JumSave[j].jum;
					Ans += (rrr);
					if (j<Sisa) Ans += (JumSave[j].jum);
				}
				i=R;
			}
			else
			{
				Ans += Jum;
				JumSave.push_back(tempST);
			}
		}
		
		cout << "Case #" << test << ": " << Ans << "\n";
	}

	return 0;
}
