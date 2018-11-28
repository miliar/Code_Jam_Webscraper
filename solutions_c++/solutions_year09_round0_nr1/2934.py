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


const int maxd=5000;
const int maxe=500;

int l,d,n;
string sd[maxd];
string sn[maxe];

void init()
{
	cin >> l >> d >> n;
	for (int i=0;i<d;i++)
		cin >> sd[i];
	for (int i=0;i<n;i++)
		cin >> sn[i];
}
int solve(string &reg)
{
	int rc=0;
	for(int x=0;x<d;x++){
		string w = sd[x];
		int cur=0;
		int match=0;
		for(int i=0;i<l;i++){
			match=0;
			if(reg[cur]==w[i]) {
				match=1;
				cur++;
			}else if(reg[cur]=='(') {
				while(reg[++cur]!=')') {
					if(reg[cur]==w[i]) {
						match=1;
						while(reg[cur++]!=')')
							;
						break;
					}
				}
			}
			if(match==0)
				break;
		}
		if(match!=0) {
			rc++;
		}
	}
	return rc;
}

int main()
{
	//freopen("..\\A.in","r",stdin);
	//freopen("..\\A-small-attempt0.in","r",stdin);freopen("..\\A-small-attempt0.out","w",stdout);
	freopen("..\\A-large.in","r",stdin);freopen("..\\A-large.out","w",stdout);
	init();
	for (int caseId=1;caseId<=n;caseId++)
	{
		printf("Case #%d: ",caseId);
		//init();
		int ret=solve(sn[caseId-1]);
		printf("%d\n",ret);
		fflush(stdout);
	}
	return 0;
}

