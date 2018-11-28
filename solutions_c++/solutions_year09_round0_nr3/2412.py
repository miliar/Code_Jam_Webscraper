#include <cstdio>
#include <string>
#include <iostream>
using namespace std;
bool b[100];
int ans;
string s;
string w;
void analyzing(){
	int u1=0;
	int u2=0;
	while (u1 < s.length() && u2 < w.length()){
		if (!b[u1])
			++u1;
		else
			if (s[u1] != w[u2])
				return;
			else
				++u1,++u2;
	}
	if (u2 == w.length())
		++ans,ans%=10000;
}
void gen(int pos,int n,int k){
	if (!k){
		analyzing();
	}
	else
		if ((k > 0) && (k <= n-pos) && (pos <= n)){
			int i=n-1;
			while (i >= pos){
				b[i]=1;
				gen(i+1,n,k-1);
				b[i]=0;
				--i;
			}
		}
}
int main(){
	int n;
	w="welcome to code jam";
	scanf("%d\n",&n);
	for (int test=1; test<=n; ++test){
		getline(cin,s);
		for (int i=0; i<s.length(); ++i)
			b[i]=0;
		ans=0;
		gen(0,s.length(),w.length());
		printf("Case #%d: %04d\n",test,ans);
		
	}
	return 0;
}
