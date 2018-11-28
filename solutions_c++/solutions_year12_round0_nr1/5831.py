#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <map>
using namespace std;
typedef pair <char,char>pcc;
int main()
{
	char kase[100],decrypt[1000];
	char mapping[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	gets(kase);
	int T=atoi(kase);
	for(int kase=1;kase<=T;++kase)
	{
		printf("Case #%d: ",kase); 
		gets(decrypt);
		for(int i=0;i<strlen(decrypt);++i)
		{
			if(decrypt[i]==' ')
			{
			cout<<" ";
			}
			else
			{
			cout<<mapping[(int)decrypt[i]-'a'];
			}
			
		}
		cout<<endl;
	}
	//system("pause");
	return 0;
}