// joy
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<map>
using namespace std;

/*
y,h,e,s,o,c,v,x,d,u,i,g,l,b,k,r,z,t,n,w,j,p,f,m,a,q
*/
char a[100]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
	int CN=0;
	int T;cin>>T;getchar();
	
	while(T--)
	{
		string s;
		getline(cin,s);
		
		string ans=s;
		for(int i=s.size()-1;i>=0;i--)
		{
			if(s[i]==' ') continue;
			ans[i]=a[s[i]-'a'];
		}
		
		cout<<"Case #"<<++CN<<": "<<ans<<endl;
	}
	
	
	return 0;
}


