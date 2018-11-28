#include <iostream>
#include <string.h>

using namespace std;

char m[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b',
				'k','r','z','t','n','w','j','p','f','m','a','q'};

int main(void)
{
	int t;
	cin>>t;
	cin.ignore();
	for(int i=0;i<t;i++)
	{
		char s[101];
		cin.getline(s,101,'\n');
		int l=strlen(s);
		char ans[l+1];
	//	cout<<l<<endl;
	//	cout<<strlen(s)<<endl;
		for(int k=0;k<l;k++)
		{
			if(s[k]==' ')
				ans[k]=' ';
			else
				ans[k]=m[s[k]-97];
//			cout<<ans[k];
		}
//		cout<<"end"<<endl;
		ans[l]='\0';
		cout<<"Case #"<<i+1<<": "<<ans<<endl;	
	}
	return 0;
}

