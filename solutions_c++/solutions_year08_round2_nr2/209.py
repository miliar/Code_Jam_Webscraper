#include <algorithm>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define fo(a,n) for(a=0;a<n;a++)
#define memset0(v) memset(v,0,sizeof(v))
typedef vector<string> vs;
typedef vector<int> vi;

bool isprime(int num)
{
	if(num==1) return true;
	if(num==2) return true;
	int sq=(int)sqrt((double)num);
	for(int a=2;a<=sq;a++)
		if(num%a==0) return false;

	return true;
}

bool shareP(int a, int b, int P)
{
	for(int factor=P;factor<=a && factor<=b;factor++)
		if(a%factor==0 && b%factor==0 && isprime(factor))
			return true;

	return false;
}


int main()
{
	int a,b,c,d,tests;
	int A,B,P;

	freopen("b-small.in", "rt", stdin);
	freopen("b-small.out", "wt", stdout);

	scanf("%d", &tests);
	int belongs[1001];

for(int test=1;test<=tests;test++)
{

	scanf("%d%d%d",&A,&B,&P);
	
	for(a=A;a<=B;a++)
		belongs[a]=a;

	int changed=1;
	while(changed)
	{
		changed=0;
		for(a=A;a<=B;a++)
		{
			for(b=a+1;b<=B;b++)
			if(belongs[a]!=belongs[b] && shareP(a,b,P))
			{
				for(c=A;c<=B;c++)
					if(belongs[c]==belongs[b]) belongs[c]=belongs[a];
			}

			if(changed) break;
		}
	}

	set<int> sets;
	for(a=A;a<=B;a++)
		sets.insert(belongs[a]);

	printf("Case #%d: %d\n",test,sets.size());
}

	fclose(stdout);
	fclose(stdin);
	return 0;
}
