#include <cstdio>
#include <string>
#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
	int n,N;
	char s[1001];
	char t[1001];
	int a[5];
	int i,j,k,l,bests,hb,nhb,o;
	scanf("%d",&N);
	for (n=1;n<=N;n++)
	{
		scanf("%d\n",&k);
		gets(s);
		l=strlen(s);
		for (i=0;i<k;i++)
			a[i]=i;
		bests=50000;
		do{
			for (i=0;i<l;i+=k)
			{
				for (j=0;j<k;j++)
				t[i+j]=s[i+a[j]];
			}
			o=1;
			for (i=1;i<l;i++)
			if (t[i]!=t[i-1]) o++;
			if (o<bests) bests=o;
		//	for (i=0;i<k;i++)
		//		printf("%d ",a[i]);
		//	printf("\n");
		}while(next_permutation(a,a+k));
		printf("Case #%d: %d\n",n,bests);
	//	fprintf(stderr,"%d\n",n);
	}
  	return 0;
}
