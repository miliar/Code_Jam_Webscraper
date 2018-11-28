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
int rsl = 0;
int N;
vector<int> vv;
int vbits[1000][32];
int bits[32];
int main()
{
	//	freopen("a-test.in","r",stdin);//freopen("a-test.out","w",stdout);
	//	freopen("A-small-attempt0.in","r",stdin);freopen("a-small.out","w",stdout);
	FILE *fp = NULL;

	fp = freopen("C-large (1).in","r",stdin);
	fp = freopen("C-large (1).out","w",stdout);

	int T;
	cin>>T;

	int tmp;
	for (int caseId=1;caseId<=T;caseId++)
	{
		cin>>N;
		vv.clear();
		memset(vbits,0,sizeof vbits);
		memset(bits,0,sizeof bits);
		for (int i =0;i<N;i++)
		{
			cin>>tmp;
			vv.push_back(tmp);
		}
		sort(vv.begin(),vv.end());
		for (int i=0;i<vv.size();i++)
		{
			tmp = vv[i];
			for (int j = 31;j>=0;j--)
			{
				if ((tmp & (1<<j)) > 0)
				{
					vbits[i][j] = 1;
					bits[j]++;
				}
			}
		}
		rsl = 1;
		for (int i=0;i<32;i++)
		{
			if ((bits[i] % 2) == 1)
			{
				rsl = 0;
				break;
			}
		}
		if (rsl == 1)
		{
			rsl = 0;
			for (int i=1;i<vv.size();i++)
			{
				rsl += vv[i];
			}
		}

		cout<<"Case #"<<caseId<<": ";
		if (rsl == 0) cout<<"NO"<<endl;
		else
			cout<<rsl<<endl;
		cerr<<caseId<<"/"<<T<<endl;
	}


	return 0;
}