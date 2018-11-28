#include <stdio.h>
#include <string.h>

char str[600];
char model[600];
int a[600];

int main()
{
	freopen("cl.in", "r", stdin);
	freopen("cl.txt", "w", stdout);
	int ti, m, i, j, T;
	strcpy(model, "#welcome to code jam");
	m=strlen(model);
	scanf("%d\n", &T);
for (ti=1; ti<=T; ti++)
{
	gets(str);
	memset(a, 0, sizeof(a));
	a[0]=1;	
	for (i=0; str[i]!='\0'; i++)
	{
		for (j=m-1; j>=1; j--)
		  if (model[j]==str[i])
		    a[j]=(a[j]+a[j-1])%10000;    
	}
	
	printf("Case #%d: ", ti);
	if (a[m-1]<10) printf("000");
	else
	if (a[m-1]<100) printf("00");
	else
	if (a[m-1]<1000) printf("0");		
	printf("%d\n", a[m-1]);
}
	return 0;
}
