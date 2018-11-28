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
int T,A,B;
int ct;

char szA[100], szB[20],szn[20],szm[20];
int solve()
{
	_snprintf(szA,sizeof szA,"%d",A);
	_snprintf(szB,sizeof szA,"%d",B);
	for (int i = A;i< B;i++)
	{
		_snprintf(szn,sizeof szn,"%d",i);
		if (strlen(szn)>1)
		{
			for (int j = 1;j<strlen(szn);j++)
			{
				if (szn[j] == '0')
				{
					continue;
				}
				memcpy(szm,szn+j,strlen(szn)-j);
				memcpy(szm+strlen(szn)-j,szn,j);
				szm[strlen(szn)] = 0;
				if (strcmp(szm,szn)>0 && strcmp(szB,szm) >=0)
				{
					ct++;
				}
			}
		}
	}
	return ct;

}
int main()
{
	//	freopen("a-test.in","r",stdin);//freopen("a-test.out","w",stdout);
	//	freopen("A-small-attempt0.in","r",stdin);freopen("a-small.out","w",stdout);
	FILE *fp = NULL;
//	fp = freopen("c-test.in","r",stdin);

	fp = freopen("C-small-attempt0.in","r",stdin);
	fp = freopen("C.out","w",stdout);

	int T;
	cin>>T;

	int tmp;
	for (int caseId=1;caseId<=T;caseId++)
	{
		cin>>A;
		cin>>B;
		ct = 0;
		cout<<"Case #"<<caseId<<": "<<solve()<<endl;

	}


	return 0;
}