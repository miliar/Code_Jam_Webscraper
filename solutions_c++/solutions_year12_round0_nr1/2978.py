#include <algorithm>
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

char str0[50]={'y','h','e','s','o','c','v',
				'x','d','u','i','g','l','b',
				'k','r','z','t','n','w',
				'j','p','f','m','a','q'};

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int n;
	char str[200];
	cin>>n;
	cin.getline(str,200);
	for(int t=1;t<=n;t++)
	{
		memset(str,0,sizeof(str));
		cin.getline(str,200);
		cout<<"Case #"<<t<<": ";
		for(int i=0;str[i];i++)
			if(str[i]!=' ')
				cout<<str0[str[i]-'a'];
			else
				cout<<' ';
		cout<<endl;	
	}
	return 0;
}
