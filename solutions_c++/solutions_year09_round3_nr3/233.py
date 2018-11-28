#include <stdio.h>
#include <algorithm>
using namespace std;

int main()
{
	int n;
	scanf("%d",&n);
	int ni;
	for (ni=1;ni<=n;ni++)
	{
		int p,q;
		scanf("%d %d",&p,&q);
		int qarr[100];
		int qinterval[101];
		int qi;
		for (qi=0;qi<q;qi++)
		{
			scanf("%d",&qarr[qi]);
			if (qi==0) qinterval[qi]=qarr[qi]-1;
			else qinterval[qi]=qarr[qi]-qarr[qi-1]-1;
		}
		qinterval[q]=p-qarr[q-1];
		int perm[100];
		bool released[100];
		for (qi=0;qi<q;qi++)
			perm[qi]=qi;
		int min=2147483647;
		do
		{
			for (qi=0;qi<q;qi++)
				released[qi]=false;
			int sum=0;
			for (qi=0;qi<q;qi++)
			{
				int i;
				for (i=perm[qi];i>=0;i--)
				{
					if (released[i]) break;
					sum+=qinterval[i]+1;
				}
				sum--;
				for (i=perm[qi];i<q;i++)
				{
					if (released[i]) break;
					sum+=qinterval[i+1]+1;
				}
				sum--;
				released[perm[qi]]=true;
			}
			if (sum<min) min=sum;
		}while (next_permutation(perm,perm+q));
		printf("Case #%d: %d\n",ni,min);
	}
	return 0;
}
