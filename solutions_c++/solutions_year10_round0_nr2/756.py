#include <stdio.h>

int Gcd(int a,int b)
{
            if (0 == b) return a;
            else return Gcd(b, a % b);
}

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);

	int c,n,t[3];
	int caseNum,i,j,r;

	scanf("%d",&c);
	for(caseNum=1;caseNum<=c;caseNum++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d",t+i);

		j=0;
		for(i=1;i<n;i++)
		{
			j=Gcd(j,t[i]>t[0]?t[i]-t[0]:t[0]-t[i]);
		}

		if(t[0]%j==0)r=0;
		else r=j-t[0]%j;

		printf("Case #%d: %d\n",caseNum,r);
	}
	
	return 0;
}