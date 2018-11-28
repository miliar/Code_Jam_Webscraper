#include <iostream>
#include <sstream>
#include <cstring>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <map>
#include <deque>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
	ofstream fout("C-large.out");
 	ifstream fin("C-large.in");
	
	int T;
	fin >> T;
	for(int i = 0; i < T; i++)
	{
		long long R,k;
		int N;
		int siz[1005];
		
		fin >> R >> k >> N;
		for(int j = 0; j < N; j++)
			fin >> siz[j];
		
		long long tot = 0;
		for(int j = 0; j < N; j++)
			tot += siz[j];
	
		long long ans = 0;
		if(tot <= k)
			ans = tot*R;
		else
		{
			int per[1005];
			bool seen[1005];
			long long euros[1005];
			memset(seen,0,sizeof seen);
			euros[0] = 0;
			per[0] = 0;
			seen[0] = 1;
			
			int cnt = 0;
			int loc = 0;
			
			int perbegin, perend;
			
			while(1)
			{
				cnt++;
				long long a = 0;
				while(a + siz[loc] <= k)
				{
					a += siz[loc], loc++;
					if(loc == N) loc = 0;
				}
				euros[cnt] = euros[cnt-1]+a;
				per[cnt] = loc;
				if(seen[loc] == 0)
					seen[loc] = 1;
				else
				{
					for(int x = 0; x < cnt; x++)
						if(per[x] == loc)
						{
							perbegin = x;
							break;
						}
					perend = cnt-1;
					break;
				}	
			}
			
			cout << perbegin << " " << perend << endl;
			
			if(R <= cnt)
				ans = euros[R];
			else
			{
				ans = euros[perbegin];
				R -= perbegin;
				long long numper = R/(perend-perbegin+1);
				long long numleft = R%(perend-perbegin+1);
				cout << numper << " " << numleft << endl;
				ans += numper*(euros[perend+1]-euros[perbegin]);
				ans += euros[perbegin+numleft]-euros[perbegin];
			}	
			
		}
		fout << "Case #" << i+1 << ": " << ans << endl;
	}

return 0;
}
		
