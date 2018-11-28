#include <iostream>
using namespace std;
int main()
{
	int n;
	cin>>n;
	char ori[150];
	cin.getline(ori,150);
	char word[150];
	char mapping[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	for (int i=1;i<=n;i++)
	{
		cin.getline(ori,150);
		memset(word,0,sizeof(word));
		int len=strlen(ori);
		for (int j=0;j<len;j++)
			if (ori[j]==' ')
				word[j]=' ';
			else
				word[j]=mapping[ori[j]-'a'];
		cout<<"Case #"<<i<<": "<<word<<endl;
	}
	return 0;
}