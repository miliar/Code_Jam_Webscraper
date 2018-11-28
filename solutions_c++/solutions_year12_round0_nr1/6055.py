#include<iostream>
#include<sstream>
#include<vector>
using namespace std;
int main()
{
int Cases;
cin>>Cases;
cin.ignore();
char v[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
for(int Case=1;Case<=Cases;Case++)
{
	string s,ret="";
	getline(cin,s);
	int len=s.length();
	for(int i=0;i<len;i++)
	{
		if(s[i]==' ')
		ret+=' ';
		else ret+=v[s[i]-'a'];
	}
	cout<<"Case #"<<Case<<": "<<ret<<endl;
}
return 0;
}
