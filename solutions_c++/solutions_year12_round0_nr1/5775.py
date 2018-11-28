#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>

using namespace std;

int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int arr[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int t;
	scanf("%d\n",&t);
	for(int it=0;it<t;++it){
		string str;
		getline(cin,str);
		for(int i=0;i<(int)str.size();++i){
			if(str[i]==32) continue;
			str[i]=arr[str[i]-'a'];
		}
		printf("Case #%d: %s\n",it+1,str.c_str());
	}
}
