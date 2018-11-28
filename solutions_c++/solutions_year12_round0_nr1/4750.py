#include<iostream>
#include<string>
using namespace std;
char tab[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
	int ca,i,len,test;
	char s[110];

	freopen("A1.in","r",stdin);
	freopen("A.out","w",stdout);
    cin>>ca; getchar();

	test=0;
	while(ca--)
	{
      gets(s);
	  len=strlen(s);
	  printf("Case #%d: ",++test);
	  for(i=0;i<len;i++)
	  {
		 if(s[i]==' ') printf(" ");
		 else printf("%c",tab[s[i]-'a']);
	  }
	  printf("\n");
	}
	//system("pause");
	return 0;
}