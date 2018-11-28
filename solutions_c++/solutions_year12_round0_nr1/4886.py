#include<cstdio>
#include<cstring>
#include<string>
#include<iostream>
using namespace std;
char a[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
	freopen("A-small-attempt0.in","r",stdin); 
	freopen("A-small-attempt0.txt","w",stdout);
    int test,i,j,k;
	char c;
	i=1;
	scanf("%d",&test);
	getchar(c);
	while(i<=test)
	{
		char b[110],res[110];
	 
		gets(b);
		for(j=0;j<strlen(b);j++)
		{
			if(b[j]!=' ')
			{
			k=b[j]-97;
			res[j]=a[k];
			}
			else
				res[j]=' ';
		}
		res[j]='\0';
		printf("Case #%d: %s\n",i,res);
		i++;
	}
	return 0;
}
