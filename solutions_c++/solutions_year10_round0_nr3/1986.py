#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

typedef unsigned long long ul;
ul sum[1001];
ul pos[1001]; //UGH!! fugly
int main()
{	
	ifstream fin("C:\\C-large.in");
	ofstream fout("C:\\C-large.out");
	int T, nCase=1;
	fin>>T;
	while(nCase <= T)
	{
		ul R, k, N; //total bits, total snaps.
		fin>>R>>k>>N;
		vector<ul> v;
		for(ul i=0; i<N; ++i)
		{
			ul gi;
			fin>>gi;
			v.push_back(gi);
			//sum[i] = -1;
			pos[i] = -1;
		}

		ul iStart = 0;
		ul total=0;
		while(R) //these many rounds;
		{
			if(pos[iStart] != -1)
			{
				total += sum[iStart];
				iStart = pos[iStart];
			}
			else
			{
				ul pers = 0;
				ul iStart1 = iStart;
				while(pers <= k-v[iStart])
				{
					pers += v[iStart];
					++iStart;
					if(iStart == N) //wrap around and never jump the pos frm where you start in every round
						iStart = 0;
					if(iStart == iStart1)
						break;
				}
				pos[iStart1] = iStart;
				sum[iStart1] = pers;
				total += pers;
			}
			--R;
		}
		fout<<"Case #"<<nCase<<": "<<total<<endl;
		++nCase;
	}
	fout<<flush;
	fout.close();
	return 0;
}