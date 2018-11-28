#include <iostream>
#include <fstream>
#include <utility>

#include <queue>
#include <string>
#include <stack>
#include <map>

using namespace std;

int T;
char sour[100];
int base;
int len;


long long ans;
void find_base();
void eval();
map <char,int> m;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	gets(sour);
	sscanf(sour,"%d",&T);
	for (int i=0;i<T;i++) {
		gets(sour);
		ans=0;
		find_base();
		eval();
		printf("Case #%d: %lld\n",i+1,ans);
	}
	return 0;
}
void find_base()
{
	int b=0;
	m.clear();
	len=strlen(sour);
	m[sour[0]]=1;
	for (int i=1;i<len;i++){
		char ch=sour[i];
		if(m.find(ch)==m.end()){
			m[ch]=b;
			b++;
			if(b==1)
				b++;
		}
	}
	base=m.size();
	if(base==1)
		base=2;
}
void eval()
{
	for(int i=0;i<len;i++){
		ans*=base;
		ans+=m[sour[i]];
	}
}
