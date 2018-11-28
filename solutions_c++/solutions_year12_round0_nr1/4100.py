#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

char cto[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main(){
	
	freopen("A-small-attempt0.in","r",stdin);
	freopen("a.out","w",stdout);

	int n;

	cin>>n;
	cin.get();
	for (int i=1;i<=n;i++){
		char g[101];
		cin.getline(g,101);
		cout<<"Case #"<<i<<": ";
		for (int j=0;j<strlen(g);j++){
			if (g[j]!=' '){
				cout<<cto[g[j]-'a'];
			}else{
				cout<<' ';
			}
		}
		cout<<endl;
	}
	return 0;
}
