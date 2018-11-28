#include <iostream>
#include <cstring>

using namespace std;

int main()
{
	int i,j,t;
	char convert[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	char test[120];
	cin>>t;
	t++;
	cout<<"Case #"<<1<<": ";
	for(i=0;i<t;i++)
	{	
		cin.getline(test,102);
		for(j=0;j<strlen(test);j++)
		{
			if(test[j]!=' ')
				test[j]=convert[test[j]-'a'];
		}
		if(i>=2 && i<=t)
		cout<<"\n"<<"Case #"<<i<<": ";
		
		cout<<test;
		
	}
	return 0;
}
