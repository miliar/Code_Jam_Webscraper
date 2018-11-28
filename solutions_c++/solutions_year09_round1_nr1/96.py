#include <iostream>
#include <cstring>
#include <cassert>
#include <bitset>
#include <sstream>

using namespace std;

int lmemo[11][900];
bitset<11814486> luckyNums[11];
bitset<11814486> curSet;

const int lucky = 0;
const int not_lucky = 1;
const int procing = 2;

int dSum(int base, int pos)
{
   int digitSum = 0;
   while(pos > 0)
   {
       digitSum += (pos % base) * (pos % base);
       pos /= base;
   }
   return digitSum;
}

bool doit(int base, int pos)
{
    if(pos == 0) return not_lucky;
    if(pos == 1) return lucky;

    int& memo = lmemo[base][pos];
    if(memo == procing) return memo = not_lucky;
    if(memo == lucky || memo == not_lucky) return memo;

    memo = procing;

    return memo = doit(base, dSum(base, pos));
}

int main()
{

    memset(lmemo, -1, sizeof lmemo);

    for(int i = 2; i <= 10; i++)
    {
	luckyNums[i].reset();
	for(int j = 2; j <= 11814485; j++)
	    if(doit(i, dSum(i, j)) == lucky) 
		luckyNums[i].set(j);
    }

    int T;
    cin >> T;
    cin.ignore();
    for(int z = 0; z < T; z++)
    {
	string s; int cur;
	getline(cin, s);
	stringstream str(s);
	str >> cur;

	curSet = luckyNums[cur];

	while(str >> cur)
	    curSet &= luckyNums[cur];

	for(int i = 2; i <= 11814485; i++)
	    if(curSet[i])
	    {
		cout << "Case #" << z + 1 << ": " << i << endl;
		break;
	    }
    }

    return 0;
}
