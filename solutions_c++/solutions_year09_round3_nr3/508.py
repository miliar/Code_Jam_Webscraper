#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
using namespace std;

int tests, test;
int p,q,i,j,res,mres;
int a[10];
bool pris[110];

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);

	scanf("%d",&tests);
	for (test=1; test<=tests; test++)
	{
		mres=999999999;
		scanf("%d %d",&p,&q);
		for (i=1; i<=q; i++)
			scanf("%d",&a[i]);
		do
		{
			memset(pris,0,sizeof(pris));
			res=0;
			for (i=1; i<=q; i++)
			{
				pris[a[i]]=1;
				j=a[i];
				while (j>1 && pris[j-1]==0) {j--; res++;}
				j=a[i];
				while (j<p && pris[j+1]==0) {j++; res++;}
			}
			if (mres>res) mres=res;
		}
		while (next_permutation(&a[1],&a[q+1]));
		printf("Case #%d: %d\n",test,mres);
	}

    return 0;
}
