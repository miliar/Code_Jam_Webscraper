#include<stdio.h>
#include<string.h>

int main()
{
char arr[102][502];
int i;

int n;
scanf("%d",&n);

int j=0;
char ch;
scanf("%c",&ch);
for(i=0;i<n;i++)
{j=0;
while(1)
{
char ch;
scanf("%c",&ch);
arr[i][j]=ch;
j++;
if(ch=='\n')
break;
}
arr[i][j-1]='\0';

}



for(i=0;i<n;i++)
{
int num[21];
for(j=0;j<20;j++)
{
num[j]=0;
}
int len=strlen(arr[i]);

for(j=0;j<len;j++)
{
	if(arr[i][j]=='w')
	{
	num[0]++;
	}
	else if(arr[i][j]=='e')
	{

		if(num[18]!=0)
		{
		num[19]=(num[19]+num[18])%10000;
		}

		if(num[13]!=0)
		{
		num[14]=(num[14]+num[13])%10000;
		}

		if(num[0]!=0)
		{
		num[1]=(num[1]+num[0])%10000;
		}

		if(num[5]!=0)
		{
		num[6]=(num[6]+num[5])%10000;
		}

	}

	else if(arr[i][j]=='l')
	{

		if(num[1]!=0)
		{
		num[2]=(num[2]+num[1])%10000;
		}

	}

	else if(arr[i][j]=='c')
	{

		if(num[2]!=0)
		{
		num[3]=(num[3]+num[2])%10000;
		}

		if(num[10]!=0)
		{
		num[11]=(num[11]+num[10])%10000;
		}

	}

	else if(arr[i][j]=='o')
	{

		if(num[3]!=0)
		{
		num[4]=(num[4]+num[3])%10000;
		}

		if(num[11]!=0)
		{
		num[12]=(num[12]+num[11])%10000;
		}
		
		if(num[8]!=0)
		{
		num[9]=(num[9]+num[8])%10000;
		}
	
	}

	else if(arr[i][j]=='m')
	{

		if(num[17]!=0)
		{
		num[18]=(num[18]+num[17])%10000;
		}

		if(num[4]!=0)
		{
		num[5]=(num[5]+num[4])%10000;
		}

	}

	else if(arr[i][j]=='t')
	{

		if(num[7]!=0)
		{
		num[8]=(num[8]+num[7])%10000;
		}

	}

	else if(arr[i][j]=='d')
	{

		if(num[12]!=0)
		{
		num[13]=(num[13]+num[12])%10000;
		}

	}
	
	else if(arr[i][j]=='j')
	{

		if(num[15]!=0)
		{
		num[16]=(num[16]+num[15])%10000;
		}

	}

	else if(arr[i][j]=='a')
	{
		
		if(num[16]!=0)
		{
		num[17]=(num[17]+num[16])%10000;
		}

	}

	else if(arr[i][j]==' ')
	{

		if(num[6]!=0)
		{
		num[7]=(num[7]+num[6])%10000;
		}
		
		if(num[9]!=0)
		{
		num[10]=(num[10]+num[9])%10000;
		}
		if(num[14]!=0)
		{
		num[15]=(num[15]+num[14])%10000;
		}

	}

}

printf("Case #%d: %'04d\n",i+1,num[18]%10000);

}

return 0;}
