#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;

int main()
{
	int test,i,j,n,len,k=1;
	char T[100],temp[100],ch;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
    scanf("%d%c",&test,&ch);
    
	while(test--)
	{
		gets(T);
		len=strlen(T);
		temp[0]='0';
		for(i=0;i<len;i++)
			temp[i+1]=T[i];
		temp[len+1]='\0';
		next_permutation(&temp[0],&temp[len+1]);
		printf("Case #%d: ",k++);
		if(temp[0]=='0')
		{
			for(i=1;i<=len;i++)
				printf("%c",temp[i]);
			printf("\n");
		}
		else
			printf("%s\n",temp);
	}
	return 0;
}
