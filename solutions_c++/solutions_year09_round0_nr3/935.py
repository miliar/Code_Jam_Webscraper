#include<iostream>
using namespace std;
char i[1000],i2[500]="welcome to code jam";
int b[500],b2[500];
int main()
{
	int a,s,n,m;
	m=strlen(i2);
int T,X;
scanf("%d",&T); scanf("%*[\r\n]s");
for(X=1;X<=T;X++)
{
	scanf("%[^\r\n]s",i); scanf("%*[\r\n]s");
	n=strlen(i);
//printf("%d\n",n);
	b[0]=1; for(a=1;a<=m;a++) b[a]=0;
	for(a=0;a<n;a++)
	{
		for(s=0;s<=m;s++) b2[s]=b[s];
		for(s=0;s<m;s++) if( i[a]==i2[s] ) b[s+1]=(b[s+1]+b2[s])%10000;
//printf("%d %d\n",a,b[1]);
	}
	printf("Case #%d: %04d\n",X,b[m]);
}
	return 0;
}
