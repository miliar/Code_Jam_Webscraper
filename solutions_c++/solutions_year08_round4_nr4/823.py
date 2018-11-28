#include<iostream>
#include<string>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;
char a[50003],b[50003];
int main()
{
		freopen("D-small-attempt0.in","r",stdin);
freopen("D-small-attempt0.out","w",stdout);
	int N,ca;
	scanf("%d",&N);
	for(ca=1;ca<=N;ca++)
	{
		int k,i;
		scanf("%d",&k);
		scanf("%s",a);
		int len=strlen(a);
		int d[6]={0,1,2,3,4,5};
		int mins=2000;
		do
		{
                 char last='0';
				 int sum=0;
			for(i=0;i<len;i++)
			{
				b[i]=a[d[i%k]+i/k*k];
				if(b[i]==last)
					;
				else
				{
					sum++;
					last=b[i];
				}
			}
			if(sum<mins)
				mins=sum;

		}while(next_permutation(d,d+k));
			printf("Case #%d:",ca);
			printf(" %d\n",mins);
	}
	return 0;
}