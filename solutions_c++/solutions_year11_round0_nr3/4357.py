#include <iostream>
#include <fstream>
using namespace std;
#define LET(x,a) typeof(a)x(a)
#define FOR(i,a,n) for(LET(i,a);i<n;++i)
#define REP(i,n) FOR(i,0,n)

ifstream fin("C:\\Users\\Arvind\\Desktop\\inputC.in");
ofstream fout("C:\\Users\\Arvind\\Desktop\\outputC.txt");

int main() {
	int T; fin>>T;
	REP(kase,T)
	{
		int N; fin>>N;
		int candies[N]; REP(i, N)fin>>candies[i];
		
		int best = -1;
		for(int bitmask = 1; bitmask < (int)(1<<N) - 1; ++bitmask)
		{
			int actualSumA = 0, actualSumB = 0, wrongSumA = 0, wrongSumB = 0;
			REP(i, N)
			if((bitmask & (1<<i)) != 0){ actualSumA += candies[i]; wrongSumA ^= candies[i];}
			else { actualSumB += candies[i]; wrongSumB ^= candies[i];}

			if(wrongSumA == wrongSumB){ if(actualSumA > best)best = actualSumA; if(actualSumB > best)best= actualSumB; }
		}
		
		
		fout<<"Case #"<<(kase+1)<<": ";
		if(best == -1)fout<<"NO"<<endl;
		else fout<<best<<endl;
	}
	return 0;  
}
