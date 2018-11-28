#include <stdio.h>
#include <map>
#include <iostream>
using namespace std;
map<char,int> mp;
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w+",stdout);
	int T;
	int siz;
	unsigned long long res;
	char str[1024];
	scanf("%d\n",&T);
	for(int i=1;i<=T;i++){
		siz=0;
		mp.clear();
		gets(str);
		for(int j=0;str[j];j++){
			if(j==0){
				mp[str[j]]=1;
			}else
				if(mp.count(str[j])==0)
				{
					mp[str[j]]=siz;
					if(!siz) siz=2;
					else siz++;
				}
		}
		res=0;
		if(!siz)siz=2;
		for(int jk=0;str[jk];jk++)
			res=(res*siz+mp[str[jk]]);
		cout << "Case #"<< i << ": " << res << "\n";
	}
	return 0;
}