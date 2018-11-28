#include <iostream>
#include <string>
using namespace std;

char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
	freopen("f:\\A.in","r",stdin);
	freopen("f:\\A.out","w",stdout);
	int t;
	cin>>t;
	getchar();
	for (int i = 1; i <= t; i++)
	{
		char s[101];
		
		gets(s);
		cout<<"Case #"<<i<<": ";
		size_t len = strlen(s);
		for (size_t j = 0; j < len; j++)
		{
			if (s[j] == ' ')
				cout<<" ";
			else
				cout<<map[s[j]-'a'];
		}
		cout<<endl;
	}

	//system("pause");
}