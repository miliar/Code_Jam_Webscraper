#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int a[]={'y'-'a','h'-'a','e'-'a','s'-'a','o'-'a','c'-'a','v'-'a',
'x'-'a','d'-'a','u'-'a','i'-'a','g'-'a','l'-'a','b'-'a','k'-'a',
'r'-'a','z'-'a','t'-'a','n'-'a','w'-'a','j'-'a','p'-'a','f'-'a',
'm'-'a','a'-'a','q'-'a'};
char s[1000000];

int main()
{
   freopen("A-small-attempt1.in","r",stdin);
   freopen("out.txt","w",stdout);
	int t,n,cas=0;
	scanf("%d\n",&t);
	//getchar();
	while(t--)
	{
	    gets(s);
	    cas++;
	    n=strlen(s);
	    printf("Case #%d: ",cas);
	    for(int i=0;i<n;i++)
	    {
	        if(s[i]==' ')
                printf(" ");
            else
                printf("%c",a[s[i]-'a']+'a');
	    }
	    printf("\n");
	}
    return 0;
}
