#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
int main()
{   
	char a[101];
	char b[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int test,j=1;
	cin>>test;
	cin.ignore();
	while(test>0)
	{
	gets(a);
	 int i=0;
	while(a[i] != '\0')
	{  
		if(a[i]!=' ')
		{
		  a[i] = b[ a[i]- 'a'];
		}
		i++;
   }
    test--;
    printf("Case #%d: %s\n",j,a);
    j++;
   }
   //system("pause");
   return 0;
}
