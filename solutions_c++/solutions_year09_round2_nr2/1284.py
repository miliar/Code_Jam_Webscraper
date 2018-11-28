#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>

using namespace std;

typedef __int64 ll;

char s[10100];

int main()
{
	int i,j,k,ca;
	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	scanf("%d",&ca);
	ll n;
	int kk=1;
	while(ca--) 
	{
		scanf("%s",s);
		int len=strlen(s);
		n=0;
		ll mi=(ll)1<<60;
		for(i=0;i<len;i++) n=n*10+s[i]-'0';
		s[len++]='0';
		sort(s,s+len);
		do
		{
			ll temp=0;
			for(i=0;i<len;i++) temp=temp*10+s[i]-'0';
			if(temp>n&&temp<mi) mi=temp;
		}while(next_permutation(s,s+len)>0);
		printf("Case #%d: %I64d\n",kk++,mi);
	}
	return 0;
}