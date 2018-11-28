#include<iostream.h>
#include<stdlib>
using namespace std;
int main()
{
	long long int N,n,i,j,k,s[200],r,flag,m,w,sum;
	char c[100];
	int a[37]={1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,
			   24,25,26,27,28,29,30,31,32,33,34,35,36};
	memset(s,0,200);
	FILE *fp;
	fp=fopen("D:\\lsm\\B.txt","w");
	scanf("%I64d",&N);
	for(i=0;i<N;i++)
	{
		scanf("%s",c);
		n=strlen(c);
		r=1;
		s[0]=1;
		for(j=1;j<n;j++)
		{
			flag=1;
			for(k=0;k<j;k++)
				{
					if(c[j]==c[k]) { flag=0; m=k; break; }
				}
				if(!flag) {s[j]=s[m];}
				else {s[j]=a[r]; r++; }
		}
		if(r==1) r++;
		w=1;
		sum=0;
		while(n--)
		{
			sum=sum+s[n]*w;
			w=w*r;
		}
		fprintf(fp,"Case #%I64d: %I64d\n",i+1,sum);
		printf("%d\n",sum);
	}
	fclose(fp);
}
