//written on C++ (compatible with DevC++ / MS Visual C++ 6)
#include<stdio.h>

int main()
{
	char s[20],x[501];
	int i,j,k,len,n,n1,tab[501][19];
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	s[0]='w';s[1]='e';s[2]='l';s[3]='c';s[4]='o';s[5]='m';s[6]='e';s[7]=' ';
	s[8]='t';s[9]='o';s[10]=' ';
	s[11]='c';s[12]='o';s[13]='d';s[14]='e';s[15]=' ';
	s[16]='j';s[17]='a';s[18]='m';s[19]=0;
	scanf("%d\n",&n);
	for(i=1;i<=n;i++)
	{
		gets(x);
		len=0;while(x[len])len++;
		if(x[0]==s[0])tab[0][0]=1;
		else tab[0][0]=0;
		for(j=1;j<19;j++)tab[0][j]=0;
		for(j=1;j<len;j++)
		{
			tab[j][0]=tab[j-1][0];
			if(x[j]==s[0]){tab[j][0]++;tab[j][0]%=10000;}
			for(k=1;k<19;k++)
			{
				tab[j][k]=tab[j-1][k];
				if(x[j]==s[k]){tab[j][k]+=tab[j-1][k-1];tab[j][k]%=10000;}
			}
		}
		n1=tab[len-1][18];
		printf("Case #%d: ",i);
		if(n1<1000)printf("0");
		if(n1<100)printf("0");
		if(n1<10)printf("0");
		printf("%d\n",n1);		
	}
	return 0;
}