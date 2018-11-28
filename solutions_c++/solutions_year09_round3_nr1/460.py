#include<iostream>
#include<map>
#include<cstring>
using namespace std;
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int test;
	cin>>test;
	char s[100];
	gets(s);
	for(int t= 0;t<test;t++)
	{
		gets(s);
		long long ans = 0;
		int a[26] = {0};
		int b[10] = {0};
		for(int i = 0;i<26;i++)
			a[i] = -1;
		for(int i = 0; i< 10; i++)
			b[i] = -1;
		int base  = 0;
		for(int i = 0;i<strlen(s);i++)
			if(s[i] >='0' && s[i]<='9')
				b[s[i]-'0'] = 0;
			else
				a[s[i]-'a'] = 0;
		for(int i = 0;i<26;i++)
			if(!a[i])
				base++;
		for(int i = 0;i<10;i++)
			if(!b[i])
				base++;
		if(base<=1)
			base = 2;
		map<int, int> m;
		m[s[0]] = 2;
		int used = 1;
		for(int i = 0;i<strlen(s);i++)
			if(!m[s[i]])
			{
				if(used==1)
				{
					m[s[i]] = used;
					used +=2;
				}
				else
				{
					m[s[i]] = used;
					used++;
				}
			}
		for(int i = 0;i<strlen(s);i++)
		{
			ans*=base;
			ans+=m[s[i]]-1;
			
		}
		cout<<"Case #"<<t+1<<": "<<ans<<endl;
		
					
				
				
	}
	
	return 0;
}
