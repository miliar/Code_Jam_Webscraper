#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	int l,d,n,i,j,k,m,len,bal,p;
	scanf("%d %d %d\n",&l,&d,&n);
	char dic[5001][16];
	//printf("%d\n",d);
	for(i=0;i<d;i++)
	{
		//fgets(dic[i],15,stdin);
		gets(dic[i]);
		//printf("HI%s\n",dic[i]);
	}
	char back[5001][16];
	k=d;
	bal=d;
	char arr[421];
	char a[16][27];
	for(p=0;p<n;p++)
	{
		for(j=0;j<d;j++)
			strcpy(back[j],dic[j]);
		fgets(arr,420,stdin);
		len=strlen(arr);
		len--;
		//printf("%d",len);
		m=0;
		for(i=0;i<l;i++)
		{
			k=0;
			if(arr[m]=='(')
			{
				m++;
				for(;m<len;m++)
				{
					if(arr[m]==')')
						break;
					a[i][k]=arr[m];
					k++;
				}
			}
			else
			{
				a[i][k]=arr[m];
				k++;
			}
			a[i][k]='\0';
			m++;
		}
		k=0;
		for(i=0;i<d;i++)
		{
			//checking dic[i]
			for(j=0;j<l;j++)
			{
				len=strlen(a[j]);
				for(m=0;m<len;m++)
				{
					if(a[j][m]==dic[i][j])
						break;
				}
				if(m==len)
					break;
			}	
			if(j==l)
			{
				k++;
				//printf("%s\n",dic[i]);
			}
			
		}
		printf("Case #%d: %d\n",p+1,k);
	}
}