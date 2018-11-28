#include<iostream>
#include<string>
using namespace std;
char a[26] = { 'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q' };
char ans[31][101];
int len[31];
int main()
{
	int T,j;char ch;
	cin>>T;	string str;
	getline(cin,str);
	for(int i=0; i<T; i++)
	{
		getline(cin,str);len[i]=0;
		for(int j=0; j<str.size();j++)
		{
			if(str[j]==' ') ans[i][j]=' ';
			else ans[i][j] = a[str[j] - 97];
			len[i]++;
		}
	}
	for(int i=0; i<T;i++)
	{
		cout<<"Case #"<<(i+1)<<": ";
		for(int j=0; j<len[i];j++)
		cout<<ans[i][j];
		cout<<endl;
	}
}
