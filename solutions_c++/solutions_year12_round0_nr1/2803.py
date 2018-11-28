#include <iostream>
#include <string>
using namespace std;

int main()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);

  char a[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

 
  int t=3;
  int i,j;
  scanf("%d\n",&t);

 
  for(i=0;i<t;i++)
  {
	char str[105];
	char tt;
	cin.getline(str, 105);
	printf("Case #%d: ",i+1); 
	for(j=0;j<strlen(str);j++)
	{
		if(str[j]>='a'&&str[j]<='z')
		{
			printf("%c",a[str[j]-'a']);
		}
		else
		{
			printf("%c",str[j]);
		}
	}
	printf("\n");
  }

	return 0;
}