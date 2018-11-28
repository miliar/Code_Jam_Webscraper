#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
vector<char> vr;
vector<int> vpb;
vector<int> vpo;
int N;
int solve()
{
	int cbp = 1,cop = 1;
	int bop = 0,bp = 0,op = 0;
	int nbp,nop;
	int second = 0;
	char who;
	int totals = 0;
	while (1)
	{
		who = vr[bop];
		if (vpb.size() > bp)
		{
			nbp = vpb[bp];
		}
		else
			nbp = 1000000;
		if (vpo.size() > op)
		{
			nop = vpo[op];
		}
		else
			nop = 1000000;
		
		int t1 = abs(cbp-nbp),t2 = abs(cop-nop);
		if (who == 'B')
		{
			second = t1+1;
			cbp = nbp;
			if (t2 <= second)
			{
				cop = nop;
			}
			else
			{
				if (nop > cop)
				{
					cop += second;
				}
				else
				{
					cop -= second;
				}
			}
			bp++;
		}
		else
		{
			second = t2+1;
			cop = nop;
			if (t1 <= second)
			{
				cbp = nbp;
			}
			else
			{
				if (nbp > cbp)
				{
					cbp += second;
				}
				else
				{
					cbp -= second;
				}
			}
			op++;
		}
		bop++;
		totals += second;
		if (bop == vr.size())
		{
			break;
		}
		

	}

	return totals;
}
int main()
{
//	freopen("a-test.in","r",stdin);//freopen("a-test.out","w",stdout);
//	freopen("A-small-attempt0.in","r",stdin);freopen("a-small.out","w",stdout);
	FILE *fp = NULL;
	
	fp = freopen("A-large.in","r",stdin);
	fp = freopen("A-large.out","w",stdout);
	
	int testcase;
	cin>>testcase;
	char chr;
	int p;
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		vr.clear();
		vpb.clear();
		vpo.clear();
		cin>>N;
		for (int i=0;i<N;i++)
		{
			cin>>chr;
			cin>>p;
			vr.push_back(chr);
			if(chr == 'O')
			vpo.push_back(p);
			else
			vpb.push_back(p);
		}

		printf("Case #%d: %d\r\n",caseId,solve());
		cerr<<caseId<<"/"<<testcase<<endl;
	}
	

	return 0;
}