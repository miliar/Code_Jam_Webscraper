#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	char a[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r', 'z','t','n','w','j','p','f','m','a','q'};
	int t,i;
	char s[120];
	char fal;
	cin>>t;
	scanf("%c",&fal);
	int T=t;
	while(t--)
	{
		cin.getline (s,120);
		printf("Case #%d: ",T-t);
		for(i=0;i<strlen(s);i++)
			if(s[i]-'a'<26 && s[i]-'a'>=0)
				cout<<a[s[i]-'a'];
			else 
				cout<<s[i];
		cout<<endl;
	
	}
return 0;
}
