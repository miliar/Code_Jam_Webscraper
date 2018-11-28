#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
using namespace std;

int t,test;
long long code[256];
long long res,tmp;
long long base;
char mes[70];
int i,j,l;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

	scanf("%d\n",&t);
	for (test=1; test<=t; test++)
	{
		printf("Case #%d: ",test);
		gets(mes);
		l=strlen(mes);
		memset(code,-1,sizeof(code));
		base=0;
		for (i=0; i<l; i++)
		{
			if (code[mes[i]]==-1)
			{
				code[mes[i]]=base;
				base++;
			}
		}
		if (base==1) base=2;
		code[mes[0]]=1;
		i=0;
		while (i<l-1 && mes[i]==mes[0]) i++;
		if (mes[i]!=mes[0]) code[mes[i]]=0;
		res=0;
		tmp=1;
		for (i=l-1; i>=0; i--)
		{
			res+=tmp*(long long)(code[mes[i]]);
			tmp*=base;
		}
		cout << res << endl;
	}

    return 0;
}
