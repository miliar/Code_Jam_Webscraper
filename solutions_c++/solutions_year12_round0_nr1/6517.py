#include<iostream>
#include<string>

using namespace std;


int main()	{
	int i,T;
	char GO[] = {' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	char G[] =  {' ','y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
	cin>>T;
	
	string s;
	getline(cin,s);
	getline(cin,s);
	for(i=0;i<T;i++)	{
	cout<<"Case #"<<i+1<<": ";
	
	
	int k=0,j=0;
	for(k=0;k<s.length();k++)	{
		while(s[k] != G[j])	{
			j++;
		}
		cout<<GO[j];
		j=0;
	}
	
	getline(cin,s);
	cout<<endl;
		
	}
	return 0;
}
	
