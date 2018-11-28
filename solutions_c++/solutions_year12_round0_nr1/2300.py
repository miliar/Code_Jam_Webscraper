#include <iostream>
#include <string>
#include <cstdio>
#include <vector>

using namespace std;

int i,j,k,l,m,n,t;
char map[26]={'y','h','e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
char ch[1000];

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>t;
	gets(ch);
	for (int ii=1;ii<=t;ii++){
		cout<<"Case #"<<ii<<": ";
		gets(ch);
		string s = ch;
		n = s.length();
		for (i=0;i<n;i++)
		  if (s[i]!=' ') s[i]=map[s[i]-'a'];
		cout<<s<<"\n";	
	}
	return 0;
}
