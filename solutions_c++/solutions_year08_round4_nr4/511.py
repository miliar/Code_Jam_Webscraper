#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;

char a[51200];
int  b[51200];

int p[32];

int m,n;


int skip()
{
	int i,j,k,t,temp;
	for(i=m-1;i>=1;i--)
		if(p[i]<p[i+1])
			break;
	if(i==0)
		return 0;
	k=i;
	t=-1;
	for(i=k+1;i<=m;i++)
		if(p[i]>p[k]&& (t<0 || p[i]<p[t]) )
			t=i;
	temp=p[k];
	p[k]=p[t];
	p[t]=temp;
	sort(p+k+1,p+m+1);
	return 1;
}


int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("output.out","w",stdout);
	int i,seq,num,maxi_result,cc;
	scanf("%d",&num);
	p[0]=0;
	for(seq=1;seq<=num;seq++)
	{
		scanf(" %d",&m);
		scanf(" %s", &a[1]);

		n=strlen( (char*) (&a[1]) );

		maxi_result=0;

		cc=0;
		for(i=2;i<=n;i++)
			if(a[i]==a[i-1])
				cc++;
		maxi_result=cc;
		for(i=1;i<=m;i++)
			p[i]=i;
		while(skip())
		{
			//for(i=1;i<=m;i++)
			//	cout<<p[i]<<' ';
			//cout<<endl;
			for(i=1;i<=n;i++)
			{
				b[i]=a[ (i-1)/m * m + p[ (i-1)%m+1]  ];
			}
			cc=0;
			for(i=2;i<=n;i++)
				if(b[i]==b[i-1])
					cc++;
			if(cc>maxi_result)
				maxi_result=cc;
		}
		printf("Case #%d: %d\n",seq,n-maxi_result);
	}
	return 0;
}

