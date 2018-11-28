#include<iostream>
#include<string>
using namespace std;



int main(){
char trans[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int n;
cin>>n;
string s1;
getline(std::cin,s1);
for(int i=0;i<n;i++)
{

	string s;
	getline(std::cin,s);
	for(int j=0;j<s.length();j++)
	{
		if(s[j]==' ') continue;
		s[j]=trans[(int)s[j]-97];
	}
	cout<<"Case #"<<i+1<<":"<<" "<<s<<endl;
}
return 0;
}

