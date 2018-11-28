#include<cstdio>
#include<cstring>
int main()
{
	int t,a[26],i,ca=0;
	char str[200],ch;
	a[0] = 24;
	a[1] = 7;
	a[2] = 4;
	a[3] = 18;
	a[4] = 14;
	a[5] = 2;
	a[6] = 21;
	a[7] = 23;
	a[8] = 3;
	a[9] = 20;
	a[10] = 8;
	a[11] = 6;
	a[12] = 11;
	a[13] = 1;
	a[14] = 10;
	a[15] = 17;
	a[16] = 25;
	a[17] = 19;
	a[18] = 13;
	a[19] = 22;
	a[20] = 9;
	a[21] = 15;
	a[22] = 5;
	a[23] = 12;
	a[24] = 0;
	a[25] = 16;
	scanf("%d%c",&t,&ch);
	while(t--)
	{
		ca++;
		scanf("%[^\n]%c",str,&ch);
		printf("Case #%d: ",ca);
		for (i=0;str[i]!=0;i++)
		{
			if (str[i]==' ')
				printf("%c",str[i]);
			else
				printf("%c",a[str[i]-'a']+'a');
		}
		printf("\n");
	}
	return 0;
}
