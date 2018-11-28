#include <iostream>
#include <cstring>
#include <cctype>

using namespace std;

int m[512][20];
char s1[]="welcome to code jam";

int main()
{
	int t,_t;
	char buf[1024];
	cin.getline(buf,sizeof(buf));
	sscanf(buf,"%d",&_t);
	for (t=1;t<=_t;t++)
	{
		cin.getline(buf,sizeof(buf));
		memset(m,0,sizeof(m));
		int len = strlen(buf);
		for (int j=0;j<len;j++)
			if (buf[j]==s1[0]) m[j][0]=1;
		for (int i=1;i<19;i++)
		{
			int sum=0;
			for (int j=0;j<len;j++)
			{
				if (buf[j]==s1[i]) m[j][i]=sum % 10000;
				sum += m[j][i-1];
			}
		}
		int res=0;
		for (int j=0;j<len;j++)
			res += m[j][18];
		printf("Case #%d: %04d\n",t,res%10000);
	}

	return 0;
}
