#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;
string from="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvqz";
string to="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upzq";
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

	int T;
	cin>>T;
	getchar();
	for(int i=1;i<=T;++i)
	{
		printf("Case #%d: ",i);
		char str[1000];
		gets(str);	
		int k;
		for(int j=0;j<strlen(str);++j)
		{
			for(k=0;k<from.size();++k)
			{
				if(from[k]==str[j]) 
				{
					str[j]=to[k];
					break;
				}
			}
			if(k==from.size())
			{
				cout<<str[j]<<" is not found";
			}
		}
		cout<<str<<endl;
	}

	return 0;
}