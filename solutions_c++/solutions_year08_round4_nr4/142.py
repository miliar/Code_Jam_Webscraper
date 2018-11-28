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
#include <ctime> 

using namespace std;

char s[60000];
int a[20];

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);

	char last,now;
	int l,t,i,best,tmp,k,len;
	scanf("%d",&t);
	for (l=0;l<t;l++)
	{
		scanf("%d",&k);
		scanf("%s",s);
		len=strlen(s);
		for (i=0;i<k;i++) a[i]=i;
		best=2000000000;
		do
		{
			last='A';
			tmp=0;
			for (i=0;i<len;i++)
			{
				now=s[i/k*k+a[i%k]];
				if (now!=last) tmp++;
				last=now;
			}
			if (tmp<best) best=tmp;
		}while (next_permutation(a,a+k));
		printf("Case #%d: %d\n",l+1,best);
	}
	return 0;
}

