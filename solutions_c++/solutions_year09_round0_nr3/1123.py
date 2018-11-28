#include <iostream>
#include<fstream>
#include <string>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include<math.h>
#include<sstream>
#include <algorithm>
using namespace std;
//ofstream fo("G:\\ASmallAns.txt",ios_base::out);
int main()
{
	int i,j,n,t,len,s;
	int a[1000],b[1000];
	char chars[20]="welcome to code jam";
	char str[1000];
	//ofstream fo("G:\\CSAns.txt",ios_base::out);
	scanf("%d",&t);
	cin.getline(str,1000-1);
	for (n=1;n<=t;n++)
	{
		//scanf("%s",&str);
		cin.getline(str,1000-1);
		len =strlen(str);
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		if (str[0]=='w')
			b[0]=1;
		for (i=1;i<len;i++)
			if (str[i]=='w')
				b[i]=b[i-1]+1;
			else
				b[i]=b[i-1];
		for (i=1;i<strlen(chars);i++)
		{
			for (j=i;j<len;j++)
				if (str[j]==chars[i])
				{
					a[j]=(b[j-1]+a[j-1])%10000;
				}
				else
					a[j]=a[j-1];
			for (j=0;j<len;j++)
			{
				b[j]=a[j];
				a[j]=0;
			}
		}
		//fo<<"Case #"<<n<<": ";
		printf("Case #%d: ",n);
		s=1000;
		for (i=0;i<4;i++)
		{
			printf("%d",b[len-1]/s);
			//fo<<b[len-1]/s;
			b[len-1]=b[len-1]%s;
			s=s/10;
		}
		printf("\n");
		//fo<<endl;
		

	}
	//cin>>i;
	return 0;
}