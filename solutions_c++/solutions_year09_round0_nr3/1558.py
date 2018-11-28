#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int N;
	scanf("%d",&N);
	char s[1024];
	int r[1024];
	gets(s);
	for(int ll=0;ll<N;ll++)
	{
		gets(s);
		memset(r,0,sizeof(r));
		for(int i=0;i<strlen(s);i++)
		{
			switch(s[i])
			{
			case 'w':
				r[0]=(r[0]+1)%10000;
				break;
			case 'e':
				r[1]=(r[1]+r[0])%10000;
				r[6]=(r[6]+r[5])%10000;
				r[14]=(r[14]+r[13])%10000;
				break;
			case 'l':
				r[2]=(r[2]+r[1])%10000;
				break;
			case 'c':
				r[3]=(r[3]+r[2])%10000;
				r[11]=(r[11]+r[10])%10000;
				break;
			case 'o':
				r[4]=(r[4]+r[3])%10000;
				r[9]=(r[9]+r[8])%10000;
				r[12]=(r[12]+r[11])%10000;
				break;
			case 'm':
				r[5]=(r[5]+r[4])%10000;
				r[18]=(r[18]+r[17])%10000;
				break;
			case ' ':
				r[7]=(r[7]+r[6])%10000;
				r[10]=(r[10]+r[9])%10000;
				r[15]=(r[15]+r[14])%10000;
				break;
			case 't':
				r[8]=(r[8]+r[7])%10000;
				break;
			case 'd':
				r[13]=(r[13]+r[12])%10000;
				break;
			case 'j':
				r[16]=(r[16]+r[15])%10000;
				break;
			case 'a':
				r[17]=(r[17]+r[16])%10000;
				break;
			}
		}
		printf("Case #%d: ",ll+1);
		if(r[18]<10)
			printf("000");
		else if(r[18]<100)
			printf("00");
		else if(r[18]<1000)
			printf("0");
		printf("%d\n",r[18]);
	}
}