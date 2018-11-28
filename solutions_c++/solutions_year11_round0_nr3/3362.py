#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;
typedef unsigned int uint;

class Info
{
public:
	Info(int a, int b, int c, uint d, uint e, uint f)
	:	i(a)
	,	numS(b)
	,	numP(c)
	,	sSum(d)
	,	sSumP(e)
	,	pSumP(f)
	{}
	int i;
	int numS; // number of candies sean has
	int numP; // number of candies patrick has
	uint sSum; // sean's real sum
	uint sSumP; // sean's sum as counted by patrick
	uint pSumP; // patric's sum as counted by patrick
};
map<Info, uint> resMap;

uint check(const vector<int> &c, const Info &inf)
{
	// no more candy
	if (inf.i >= c.size())
	{
		// if patrick won't cry, keep sSum
		return (inf.numS && inf.numP && inf.sSumP == inf.pSumP) ? inf.sSum : 0;
	}
	
	// 2 possibilities here, either sean gets a piece, or patrick gets one
	Info inf1(inf.i + 1, inf.numS+1, inf.numP, inf.sSum + c[inf.i], inf.sSumP ^ c[inf.i], inf.pSumP);
	Info inf2(inf.i + 1, inf.numS, inf.numP+1, inf.sSum, inf.sSumP, inf.pSumP ^ c[inf.i]);
	uint res1 = check(c, inf1);
	uint res2 = check(c, inf2);
	return max(res1, res2);
}

int main(int argc, char **argv)
{
	ifstream in(argv[1]);
	if (!in)
	{
		cout << "Cannot open file";
		return 1;
	}

	int T, N;
	in >> T;
	for (int i = 1; i <= T; ++i)
	{
		in >> N;
		int cost;
		vector<int> candies;
		// read candies
		for (int n = 0; n < N; ++n)
		{
			in >> cost;
			candies.push_back(cost);
		}			
		// recursive version
		resMap.clear();
		Info inf(0, 0, 0, 0, 0, 0);
		uint res = check(candies, inf);

		if (res)		
			printf("Case #%d: %u\n", i, res);	
		else
			printf("Case #%d: NO\n", i);
	}	

	return 0;
}
