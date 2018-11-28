#include<stdio.h>
#include<string.h>

using namespace std;

char decrypt[30] = "yheso vxduiglbkrztnwjpfma ";

int main()
{
	decrypt[5] = 'c';
	decrypt[25] = 'q';
	int N;
	scanf("%d\n",&N);
	for(int t=0;t<N;t++)
	{
		char temp[150];
		gets(temp);
		for(int i=0;i<strlen(temp);i++)
		{
			if(temp[i] >= 'a' && temp[i] <= 'z')
				temp[i] = decrypt[temp[i]-'a'];
		}
		printf("Case #%d: %s\n",t+1,temp);
	}
	return 0;
}
