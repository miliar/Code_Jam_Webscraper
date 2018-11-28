#include<stdio.h>
#include<string.h>
int main()
{
	int c;
	char str[1000000];
	char te[10000]="aybhcedseofcgvhxidjukilgmlnbokprqzrtsntwujvpwfxmyazq";
	scanf("%d\n",&c);
	for(int x=0;x<c;x++)
	{
		printf("Case #%d: ",x+1);
		gets(str);
		for(int n=0;n<strlen(str);n++)
		{
			if(str[n]>='a'&&str[n]<='z')
			{
				for(int m=0;m<strlen(te);m+=2)
				{
					if(te[m]==str[n])
					{
						printf("%c",te[m+1]);
						break;
					}
				}
			}
			else
				printf("%c",str[n]);
		}
		printf("\n");
	}
}
