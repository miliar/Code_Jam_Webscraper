#include<stdio.h>
#include<stdlib.h>

using namespace std;
int N,n;
char goo[105],eng[105];
char decode[300];
char database[] = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	system("ren *.in input.in");
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	int check,i;
	for(i='a' ; i<='z' ; i++)
		decode[i] = database[i-'a'];
	scanf("%d ",&N);
	for(n=0 ; n<N ; n++)
	{
		gets(goo);
		printf("Case #%d: ",n+1);
		for(i=0 ; goo[i] ; i++)
		{
			printf("%c",goo[i]==' ' ? ' ' : decode[goo[i]]);
		}
		puts("");
	}
	scanf(" ");
	//for(;;);
	return 0;
}
