#include<string>
#include<iostream>
#include<istream>
#include<string.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	char c[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	cin.get();
	for(int j=1;j<=t;j++)
	{
		char s1[102];
		string s2="";
		cin.getline(s1,102);
		for(int i=0;i<strlen(s1);i++)
			if(s1[i]==' ')
				s2 +=' ';
			else
				s2+= c[s1[i]-'a'];
		cout<<"Case #"<<j<<": "<<s2<<endl;
		
	}
}
